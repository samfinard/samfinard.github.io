"""Source-level checks for the site. Run with: uv run pytest"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIRS = ["pages", "dsa", "finance"]

MD_LINK = re.compile(r"\]\(([^)\s]+)")
NAV_URL = re.compile(r"^\s*url:\s*(\S+)", re.MULTILINE)
AVATAR = re.compile(r'^\s*avatar\s*:\s*"([^"]+)"', re.MULTILINE)


def content_files():
    return sorted(p for d in CONTENT_DIRS for p in (ROOT / d).glob("*.md"))


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


def permalinks():
    return {fm["permalink"]: p for p in content_files() if "permalink" in (fm := front_matter(p))}


def is_external(target):
    return target.startswith(("http://", "https://", "mailto:", "#"))


def local_links():
    return [
        pytest.param(path, target, id=f"{path.relative_to(ROOT)}->{target}")
        for path in content_files()
        for target in MD_LINK.findall(path.read_text(encoding="utf-8"))
        if not is_external(target)
    ]


def nav_urls():
    nav = (ROOT / "_data" / "navigation.yml").read_text(encoding="utf-8")
    return [url for url in NAV_URL.findall(nav) if not is_external(url)]


@pytest.mark.parametrize("path, target", local_links())
def test_relative_link_resolves(path, target):
    local = target.split("#", 1)[0]
    resolved = ROOT / local.lstrip("/") if local.startswith("/") else path.parent / local
    assert resolved.exists(), f"{target} does not exist"


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
    avatar = AVATAR.search((ROOT / "_config.yml").read_text(encoding="utf-8")).group(1)
    assert (ROOT / "images" / avatar).is_file(), f"images/{avatar} missing"
