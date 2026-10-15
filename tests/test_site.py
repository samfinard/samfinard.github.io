"""Source-level checks for the site. Run with: uv run pytest"""

import re
from fnmatch import fnmatch
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = ["pages", "dsa", "finance"]
DSA_INDEX = ROOT / "pages" / "dsa.md"

MD_LINK = re.compile(r"\]\(([^)\s]+)")
NAV_URL = re.compile(r"^\s*url:\s*(\S+)", re.MULTILINE)
AVATAR = re.compile(r'^\s*avatar\s*:\s*"([^"]+)"', re.MULTILINE)
# The indented / blank / comment lines that follow a top-level `exclude:` key.
EXCLUDE_BLOCK = re.compile(r"^exclude:[ \t]*\n((?:[ \t]+.*\n|[ \t]*\n)*)", re.MULTILINE)
LIST_ITEM = re.compile(r"^[ \t]*-[ \t]*[\"']?([^\"'#\s]+)", re.MULTILINE)


def config_text():
    return (ROOT / "_config.yml").read_text(encoding="utf-8")


def excluded_patterns():
    block = EXCLUDE_BLOCK.search(config_text())
    return LIST_ITEM.findall(block.group(1)) if block else []


def is_excluded(path):
    """True if Jekyll's `exclude:` list keeps this file out of the build."""
    rel = path.resolve().relative_to(ROOT).as_posix()
    return any(
        fnmatch(rel, pattern) or rel.startswith(pattern.rstrip("/") + "/")
        for pattern in excluded_patterns()
    )


def content_files():
    return sorted(p for d in CONTENT_DIRS for p in (ROOT / d).glob("*.md"))


def published_files():
    return [p for p in content_files() if not is_excluded(p)]


def rel_id(path):
    return path.relative_to(ROOT).as_posix()


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    block = text[4:].split("\n---", 1)[0]
    return dict(
        (k.strip(), v.strip().strip("\"'"))
        for k, _, v in (line.partition(":") for line in block.splitlines())
        if v.strip()
    )


def body(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        text = text[4:].split("\n---", 1)[-1]
    return text


def permalinks():
    return {fm["permalink"]: p for p in content_files() if "permalink" in (fm := front_matter(p))}


def is_external(target):
    return target.startswith(("http://", "https://", "mailto:", "#"))


def resolve(path, target):
    local = target.split("#", 1)[0]
    return ROOT / local.lstrip("/") if local.startswith("/") else path.parent / local


def local_links():
    return [
        pytest.param(path, target, id=f"{rel_id(path)}->{target}")
        for path in published_files()
        for target in MD_LINK.findall(path.read_text(encoding="utf-8"))
        if not is_external(target)
    ]


def linked_from(page):
    return {
        resolve(page, target).resolve()
        for target in MD_LINK.findall(page.read_text(encoding="utf-8"))
        if not is_external(target)
    }


def published_dsa_articles():
    return [pytest.param(p, id=rel_id(p)) for p in published_files() if p.parent.name == "dsa"]


def nav_urls():
    nav = (ROOT / "_data" / "navigation.yml").read_text(encoding="utf-8")
    return [url for url in NAV_URL.findall(nav) if not is_external(url)]


@pytest.mark.parametrize("path, target", local_links())
def test_relative_link_resolves(path, target):
    resolved = resolve(path, target)
    assert resolved.exists(), f"{target} does not exist"
    assert not is_excluded(resolved), f"{target} is excluded from the build"


@pytest.mark.parametrize("path", [pytest.param(p, id=rel_id(p)) for p in published_files()])
def test_published_page_not_empty(path):
    assert body(path).strip(), f"{rel_id(path)} is published but empty; delete or exclude it"


@pytest.mark.parametrize("path", published_dsa_articles())
def test_dsa_article_linked_from_index(path):
    assert path.resolve() in linked_from(DSA_INDEX), (
        f"{rel_id(path)} is published but not linked from pages/dsa.md; "
        "link it there or add it to exclude: in _config.yml"
    )


def test_exclude_list_parsed():
    patterns = excluded_patterns()
    assert "tests" in patterns and "CLAUDE.md" in patterns, patterns


def test_permalinks_unique():
    seen = {}
    for path in content_files():
        link = front_matter(path).get("permalink")
        if link:
            assert link not in seen, f"{path.name} and {seen[link]} share {link}"
            seen[link] = path.name


@pytest.mark.parametrize("url", nav_urls())
def test_nav_target_exists(url):
    assert url in permalinks() or (ROOT / url.lstrip("/")).is_file(), f"no page or file for {url}"


def test_homepage_exists():
    assert "/" in permalinks()


def test_author_avatar_exists():
    avatar = AVATAR.search(config_text()).group(1)
    assert (ROOT / "images" / avatar).is_file(), f"images/{avatar} missing"
