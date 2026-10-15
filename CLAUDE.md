# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal site for Sam Finard, served by GitHub Pages at samfinard.github.io. It is a Jekyll site built on a trimmed-down fork of the Academic Pages theme (itself a fork of Minimal Mistakes). The site has three things: an About page, a set of Data Structures & Algorithms notes, and a Resources page. A push to `master` deploys only if CI passes (Pages deploys from GitHub Actions, not from the branch).

## Commands

```bash
bundle install                              # Ruby deps (github-pages gem pins Jekyll + plugins)
bundle exec jekyll serve -l -H localhost    # local server with livereload; restart after _config.yml edits

npm install && npm run build:js             # rebuild assets/js/main.min.js (only needed after editing assets/js/)
npm run watch:js                            # rebuild on JS changes

uv run pytest                               # source checks (pytest in a uv env, no Jekyll needed)
uv run pytest -k test_nav_target_exists     # a single test (links/nav targets are parametrized per item)
```

CI (`.github/workflows/test.yml`) runs on every push and PR: the `tests/` source checks (`uv run --locked pytest`, so commit `uv.lock` with any dependency change), then `jekyll build`, then `htmlproofer _site --disable-external` to catch broken internal links and images. Its `deploy` job publishes `_site` only for pushes to `master` that pass. Local system Ruby on this machine is 2.6, which is too old for `github-pages`, so the full build is only verified in CI.

Markdown lint config is in `.markdownlint.yaml`. It turns off line length (MD013), duplicate headings (MD024), ordered-list numbering (MD029), and first-line-heading (MD041).

## How content is wired

- **Top-level pages** are in `pages/` and get their URL from a `permalink` in front matter: `about.md` → `/`, `dsa.md` → `/dsa/`, `resources.md` → `/resources/`.
- **The header nav** comes from `_data/navigation.yml`: Resume (`/files/resume.pdf`), DSA, Resources. To update the resume, replace `files/resume.pdf`.
- **DSA articles** (`dsa/*.md`) and **finance notes** (`finance/*.md`) have **no front matter**. Pages link to them with relative `.md` paths, for example `[Stack](../dsa/stack.md)`. This works because GitHub Pages turns on `jekyll-optional-front-matter`, `jekyll-relative-links`, and `jekyll-default-layout` by default, and the `github-pages` gem does the same locally. Keep using relative `.md` links, not hand-written `.html` URLs.
- **New DSA articles** start from `dsa/template.md` (excluded from the build): problem, intuitive pseudocode, Python (plus C/C++ if it helps), runtime/space analysis, and a memory aid. A published `dsa/*.md` must be linked from `pages/dsa.md` or the tests fail, so keep work-in-progress stubs (like `dsa/B_tree.md`) in `exclude:` until they're linked.
- **Math** is written as `$...$` inline LaTeX and rendered by MathJax v3, loaded once in `_includes/head/custom.html`; the `window.MathJax` config there enables the `$...$` delimiters.
- **Author sidebar** content (bio, employer, email, GitHub, LinkedIn, avatar `images/headshot.jpeg`) comes from the `author:` block in `_config.yml`. `_includes/author-profile.html` renders only those fields, so adding a new kind of link (e.g. Twitter) means editing the include too.
- **Layouts:** `default` (wraps everything, via `compress`), `single` (articles) and `archive` (index pages). The theme's collections, comments, analytics, social sharing, breadcrumbs, read time, academicons and `_data/ui-text.yml` were removed on purpose; UI labels are plain English in the includes. Don't add them back.

## Gotchas

- Every `.md` file outside the `exclude:` list in `_config.yml` is published, even with no front matter. Add non-site docs and drafts to `exclude:`. Tests fail if a published page is empty.
- `.gitignore` excludes private job-search files (`job_tracker.*` and `private/`). They must never be committed, because everything in this repo is published.
- `README.md` holds only a short to-do list (homepage bio and photo; a tag-sorted, date-ordered DSA article list).
