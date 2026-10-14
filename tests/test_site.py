"""Source-level checks for the site. Run with: python3 -m unittest discover -s tests"""

import re
import unittest
from pathlib import Path

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


class TestSite(unittest.TestCase):
    def test_relative_links_resolve(self):
        for path in content_files():
            for target in MD_LINK.findall(path.read_text(encoding="utf-8")):
                if is_external(target):
                    continue
                with self.subTest(file=path.relative_to(ROOT), link=target):
                    local = target.split("#", 1)[0]
                    resolved = ROOT / local.lstrip("/") if local.startswith("/") else path.parent / local
                    self.assertTrue(resolved.exists(), f"{target} does not exist")

    def test_permalinks_unique(self):
        seen = {}
        for path in content_files():
            link = front_matter(path).get("permalink")
            if link:
                with self.subTest(permalink=link):
                    self.assertNotIn(link, seen, f"{path.name} and {seen.get(link)} share {link}")
                    seen[link] = path.name

    def test_nav_targets_exist(self):
        links = permalinks()
        nav = (ROOT / "_data" / "navigation.yml").read_text(encoding="utf-8")
        for url in NAV_URL.findall(nav):
            if is_external(url):
                continue
            with self.subTest(url=url):
                self.assertTrue(url in links or (ROOT / url.lstrip("/")).is_file(), f"no page or file for {url}")

    def test_homepage_exists(self):
        self.assertIn("/", permalinks())

    def test_author_avatar_exists(self):
        avatar = AVATAR.search((ROOT / "_config.yml").read_text(encoding="utf-8")).group(1)
        self.assertTrue((ROOT / "images" / avatar).is_file(), f"images/{avatar} missing")


if __name__ == "__main__":
    unittest.main()
