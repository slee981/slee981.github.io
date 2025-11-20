# CLAUDE.md

This is Stephen M. Lee's personal portfolio and technical blog at https://stephenlee.info.

## Project Overview

**Type**: Jekyll static site (GitHub Pages)
**Purpose**: Professional portfolio + technical blog with deep-dive articles on data science, econometrics, physics, and engineering
**Theme**: jekyll-theme-cadre (custom)

## Technology Stack

- **Jekyll** 4.2.0 - Static site generator
- **Ruby/Bundler** - Dependency management
- **Markdown** (kramdown) - Content format with KaTeX/LaTeX math support
- **SASS** - CSS preprocessing

### Key Jekyll Plugins
- `jekyll-feed` - RSS/Atom feeds
- `jekyll-paginate` - Pagination
- `jekyll-seo-tag` - SEO metadata
- `jekyll-sitemap` - Sitemap generation

## Project Structure

```
slee981.github.io/
├── _posts/              # Blog posts (markdown with frontmatter)
├── _data/
│   ├── navigation.yml   # Main nav menu config
│   └── social.yml       # Social media links
├── _sass/               # Theme SCSS customizations
│   └── cadre/
├── assets/
│   ├── images/          # Profile pics, post images
│   ├── papers/          # PDF research papers
│   ├── resume/          # Resume files
│   └── css/
├── Root pages:
│   ├── index.html       # Blog archive (landing page)
│   ├── work.html        # Portfolio showcase
│   ├── about.html       # About page
│   ├── categories.html  # Posts by category
│   └── tags.html        # Posts by tag
├── _config.yml          # Jekyll site configuration
├── Gemfile              # Ruby dependencies
└── Makefile             # Build automation
```

## Content Structure

### Blog Posts (_posts/)
- Filename format: `YYYY-MM-DD-title.md`
- Categories: Technical/Engineering, Data Science/ML, Econometrics/Statistics, Networks, Physics/Sports
- Heavy use of LaTeX/KaTeX for mathematical notation
- Posts often include code examples and detailed explanations

### Frontmatter Template
```yaml
---
layout: post
title: "Post Title"
categories: [category1, category2]
tags: [tag1, tag2]
toc: true   # Optional: enables table of contents
katex: true # Optional: enables KaTeX rendering (NOT 'math: true')
---
```

### Mathematical Notation (KaTeX)

**IMPORTANT**: Math rendering requires specific formatting:

1. **Frontmatter**: Use `katex: true` (NOT `math: true`)
2. **Display equations**: Use `$$` on separate lines before and after
   ```markdown
   $$
   E = mc^2
   $$
   ```
3. **Inline equations**: Use `$$` for inline variables (e.g., `$$x$$`, `$$\alpha$$`, `$$R^2$$`)
   - Example: "The coefficient $$\alpha$$ determines the viewing distance $$L$$"

**Do NOT use single `$` for inline math** - the theme requires `$$` for both display and inline equations.

## Local Development

```bash
make start    # Install dependencies + serve locally
make build    # Build production site
```

### Python Scripts

Python scripts in `code/` directory require activating the virtual environment first:

```bash
source .pyenv/bin/activate  # Activate venv
python3 code/script_name.py # Run script
```

## Deployment

- **Platform**: GitHub Pages
- **Domain**: stephenlee.info (via CNAME)
- **Branch**: `gh-pages` (deployment target)
- **Workflow**: Commit to master → `make build` → push `_site/` to gh-pages

## Key Features

- Mathematical content support (KaTeX/LaTeX)
- Table of contents generation (`toc: true` in frontmatter)
- Google Analytics integration
- Custom Cadre theme with SCSS overrides
- Multi-discipline content (economics, data science, physics, engineering)

## Common File Locations

- **Add new post**: `_posts/YYYY-MM-DD-title.md`
- **Site config**: `_config.yml`
- **Navigation menu**: `_data/navigation.yml`
- **Social links**: `_data/social.yml`
- **Theme styles**: `_sass/cadre/`
- **Static assets**: `assets/images/`, `assets/papers/`
- **Built site**: `_site/` (git-ignored)

## Notes

- Posts often contain complex mathematical notation and code examples
- Content style: educational deep-dives with technical rigor
- Some posts cross-posted from older blog "Sparkling Correlation"
- Site actively maintained with regular updates
