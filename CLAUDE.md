# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal academic portfolio website built with Jekyll and the Academic Pages theme, hosted on GitHub Pages at samfinard.github.io. The site showcases work in Computer Science, Data Structures & Algorithms, and Finance.

## Development Commands

### Local Development
```bash
# Install Ruby dependencies
bundle install

# Serve site locally with live reload
bundle exec jekyll serve -l -H localhost

# Note: _config.yml changes require server restart
```

### JavaScript Build
```bash
# Install Node dependencies
npm install

# Build minified JS (uglifies jQuery and custom scripts)
npm run build:js

# Watch for JS changes and rebuild
npm run watch:js
```

## Site Architecture

### Jekyll Collections & Content Structure

The site uses Jekyll collections defined in `_config.yml`:
- **publications**: Academic papers and journal articles
- **talks**: Conference presentations
- **teaching**: Teaching materials
- **portfolio**: Project showcases

Content organization:
- `pages/`: Main site pages (About, DSA, Resources)
- `dsa/`: Data Structures & Algorithms articles following `template.md` structure
- `finance/`: Finance-related content (terminology, curves)
- `markdown_generator/`: Python scripts to generate markdown from TSV/BibTeX data

### Content Templates

DSA articles follow this structure (see `dsa/template.md`):
1. Problem description
2. Pseudocode/intuitive explanation
3. Python code (C++ if applicable)
4. Runtime/space complexity analysis
5. Memory aids (external references, use cases)

### Layout System

- `_layouts/`: Page templates (single, archive, talk, etc.)
- `_includes/`: Reusable components (header, footer, author profile, SEO, analytics)
- `_sass/`: SCSS stylesheets compiled to CSS

Key includes:
- `author-profile.html`: Sidebar with bio and social links
- `seo.html`: Meta tags for search engines
- `analytics.html`: Analytics provider integration

### Navigation & Configuration

- `_data/navigation.yml`: Header navigation menu structure
- `_config.yml`: Central configuration for site metadata, author info, collections, plugins

Site navigation order: Resume → DSA → Resources

### Author Profile Configuration

The author profile sidebar is controlled by `_config.yml` under the `author:` section. To modify social links or biographical info, edit this section rather than the includes directly.

## Content Development Workflow

When adding new DSA content:
1. Use `dsa/template.md` as the starting structure
2. Include practical examples with runtime analysis
3. Link from `pages/dsa.md` main index
4. Follow existing pattern: problem → code → analysis → memory aid

When modifying publications/talks:
1. Edit TSV files in `markdown_generator/`
2. Run corresponding Python script or Jupyter notebook to regenerate markdown
3. Commit both TSV and generated markdown

## Theme Details

Based on Academic Pages (fork of Minimal Mistakes Jekyll theme). Key customizations are in:
- Author profile fields in `_config.yml`
- Navigation structure in `_data/navigation.yml`
- Custom SCSS in `_sass/`

## GitHub Pages Deployment

- Site deploys automatically on push to master branch
- Uses `github-pages` gem for GitHub Pages compatibility
- Plugins: jekyll-feed, jekyll-sitemap, jekyll-paginate, jekyll-redirect-from

## Important Notes

- Jekyll server must be restarted after `_config.yml` changes
- JavaScript changes require running `npm run build:js` to minify
- All content pages use YAML front matter with layout, title, permalink, and author_profile settings
