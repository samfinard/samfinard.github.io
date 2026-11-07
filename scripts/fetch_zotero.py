"""Pull the Zotero library into _data/zotero.json for the Resources page.

Run in CI by .github/workflows/test.yml with a read-only key in the ZOTERO_API_KEY
secret. Locally:  ZOTERO_API_KEY=... uv run python scripts/fetch_zotero.py
Standard library only, so it needs no extra dependencies.

Reading-log fields live in each item's Extra field, one per line:
    Finished: 2024-06-18
    Summary: one-line takeaway
and finished items carry the tag "read".
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.zotero.org"
USER_ID = os.environ.get("ZOTERO_USER_ID", "12929164")
OUT = Path(__file__).resolve().parent.parent / "_data" / "zotero.json"

# Field that names where an item was published, in order of preference.
VENUE_FIELDS = [
    "publicationTitle", "proceedingsTitle", "bookTitle", "blogTitle", "websiteTitle",
    "institution", "publisher", "studio", "repository",
]
SKIP_TYPES = {"note", "annotation"}
EXTRA_LINE = re.compile(r"^(Finished|Summary):\s*(.+)$", re.MULTILINE | re.IGNORECASE)


def get_all(path, key):
    """GET every page of a Zotero API listing."""
    results, start = [], 0
    while True:
        sep = "&" if "?" in path else "?"
        req = urllib.request.Request(
            f"{API}/users/{USER_ID}/{path}{sep}limit=100&start={start}",
            headers={"Zotero-API-Key": key, "Zotero-API-Version": "3"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            page = json.load(resp)
            total = int(resp.headers.get("Total-Results", len(page)))
        results.extend(page)
        start += len(page)
        if not page or start >= total:
            return results


def person(c):
    return c.get("name") or " ".join(p for p in (c.get("firstName"), c.get("lastName")) if p)


def authors(creators):
    names = [person(c) for c in creators if c.get("creatorType") in ("author", "editor", "director", "presenter")]
    names = names or [person(c) for c in creators]
    if len(names) > 3:
        return f"{names[0]} et al."
    return ", ".join(n for n in names if n)


def normalize(d):
    """Zotero API item `data` -> the small record the site renders."""
    extra = {k.lower(): v.strip() for k, v in EXTRA_LINE.findall(d.get("extra", ""))}
    year = re.search(r"\b(1[89]\d\d|20\d\d)\b", d.get("date", ""))
    doi = d.get("DOI", "")
    title = d.get("title") or d.get("filename") or "(untitled)"
    if d["itemType"] == "attachment":  # a loose PDF: tidy the file name into a title
        title = re.sub(r"\.pdf$", "", title, flags=re.I).replace("_", " ")
    return {
        "key": d["key"],
        "type": d["itemType"],
        "title": title,
        "authors": authors(d.get("creators", [])),
        "year": year.group(1) if year else "",
        "venue": next((d[f] for f in VENUE_FIELDS if d.get(f)), ""),
        "edition": d.get("edition", ""),
        "url": f"https://doi.org/{doi}" if doi else (d.get("url", "") if d["itemType"] != "attachment" else ""),
        # manual tags only; automatic ones (type 1, e.g. arXiv categories) are noise
        "tags": sorted({t["tag"] for t in d.get("tags", []) if t.get("type", 0) == 0}, key=str.lower),
        "collections": d.get("collections", []),
        "finished": extra.get("finished", ""),
        "summary": extra.get("summary", ""),
    }


def build(collections, items):
    """Collections + item `data` dicts (any order) -> the JSON written to _data/."""
    colls = sorted(
        ({"key": c["key"], "name": c["name"], "parent": c.get("parentCollection") or None} for c in collections),
        key=lambda c: c["name"].lower(),
    )
    recs = sorted(
        (normalize(d) for d in items if d["itemType"] not in SKIP_TYPES and not d.get("parentItem") and not d.get("deleted")),
        key=lambda r: r["title"].lower(),
    )
    keys = {c["key"] for c in colls}
    for r in recs:
        r["collections"] = [k for k in r["collections"] if k in keys]
    # count: distinct items in a collection and all of its subcollections
    children = {}
    for c in colls:
        children.setdefault(c["parent"], []).append(c["key"])

    def subtree(k):
        return [k] + [d for ch in children.get(k, []) for d in subtree(ch)]

    for c in colls:
        inside = set(subtree(c["key"]))
        c["count"] = sum(1 for r in recs if inside & set(r["collections"]))
    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "collections": colls,
        "items": recs,
    }


def main():
    key = os.environ.get("ZOTERO_API_KEY")
    if not key:
        sys.exit("ZOTERO_API_KEY is not set")
    collections = [c["data"] for c in get_all("collections", key)]
    items = [i["data"] for i in get_all("items/top?include=data", key)]
    data = build(collections, items)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(data['items'])} items in {len(data['collections'])} collections to {OUT}")


if __name__ == "__main__":
    main()
