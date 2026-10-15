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

- **Top-level pages** are in `pages/` and get their URL from a `permalink` in front matter: `about.md` → `/`, `dsa.md` → `/dsa/`, `resources.md` → `/resources/`. `_config.yml` includes `_pages`, but this repo uses `pages/`.
- **The header nav** comes from `_data/navigation.yml`: Resume (`/files/resume.pdf`), DSA, Resources. To update the resume, replace `files/resume.pdf`.
- **DSA articles** (`dsa/*.md`) and **finance notes** (`finance/*.md`) have **no front matter**. Pages link to them with relative `.md` paths, for example `[Stack](../dsa/stack.md)`. This works because GitHub Pages turns on `jekyll-optional-front-matter`, `jekyll-relative-links`, and `jekyll-default-layout` by default, and the `github-pages` gem does the same locally. Keep using relative `.md` links, not hand-written `.html` URLs.
- **New DSA articles** start from `dsa/template.md`: problem, intuitive pseudocode, Python (plus C/C++ if it helps), runtime/space analysis, and a memory aid. Then add a link to the article from the topic outline in `pages/dsa.md`. Many entries there are still plain text with no link yet.
- **Math** is written as `$...$` inline LaTeX and rendered by MathJax. Two copies are loaded: v2 in `_includes/head.html`, which sets the `$` delimiters, and v3 in `_includes/head/custom.html`.
- **Author sidebar** content (bio, employer, email, GitHub, LinkedIn, avatar `images/headshot.jpeg`) comes from the `author:` block in `_config.yml`. Edit it there, not in `_includes/author-profile.html`.
- **Layouts:** the only ones left are `default`, `single`, `archive`, `archive-taxonomy`, and `compress`. The theme's collections (publications, talks, teaching, portfolio), their layouts, and the `markdown_generator/` scripts were removed on purpose. Don't add them back.

## Gotchas

- Every `.md` file outside the `exclude:` list in `_config.yml` is published, even with no front matter (e.g. `dsa/template.md`, `finance/curve.md`). Add non-site docs to `exclude:`. `CLAUDE.md`, `tests/`, `pyproject.toml` and `uv.lock` are excluded.
- `.gitignore` excludes private job-search files (`job_tracker.*` and `private/`). They must never be committed, because everything in this repo is published.
- `README.md` holds only a short to-do list (homepage bio and photo; a tag-sorted, date-ordered DSA article list).
