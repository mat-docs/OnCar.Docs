# System Monitor Documentation

Source for the System Monitor documentation site, built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

This content was split out of [ATLAS.Site](https://github.com/mat-docs/ATLAS.Site). The ATLAS site redirects its old System Monitor URLs here.

## Setup

Install Python 3.8 or later, which should come with `pip`.

From the project directory, create a virtual environment:

    python -m venv .venv

Then install dependencies:

    pip install -r requirements.txt

Preview the docs locally:

    mkdocs serve

On Windows:

    python -m mkdocs serve --livereload

## Layout

The site structure mirrors the legacy System Monitor help file (`SystemMonitor.chm`): one page per help topic, with the same hierarchy, names and order, in a single sidebar tree. **Keep it that way.** Users rely on the familiar structure. Add new topics inside the existing books rather than creating new top-level sections.

| Path | Contents |
|------|----------|
| `docs/index.md` | Introduction (home page) |
| `docs/<book>/...` | One folder per CHM book: `getting-started`, `project-management`, `using-system-monitor`, `tuning`, `ecu-control`, `history-report`, `testbed-operation`, `data-display`, `data-acquisition`, `pcu-dashboard-configuration`, `developer-functions`, `activex-automation`, `configuration-api`, `hardware`, `technical-support` |
| `docs/**/assets/` | Screenshots and diagrams for the pages in that folder |
| `docs/blog/posts/` | System Monitor release notes |
| `hooks/llms_txt.py` | Build hook that emits `/llms.txt` and `/llms-full.txt` |
| `review/` | Audit reports: source review, CHM migration check, and the rebuild (`review/restructure/README.md`) |

## Contribution guidelines

- Write for System Monitor users; prefer screenshots for UI workflows. Keep images in an `assets/` folder next to the page that uses them.
- Use relative links between pages on this site, and absolute `https://atlas.motionapplied.com/...` links for ATLAS content.
- Add every new page to `nav` in `mkdocs.yml`, in the CHM book it belongs to.
- Verify every menu path, label, default and limit against the System Monitor source for the release you are documenting.
- Release notes go in `docs/blog/posts/` with `date.created`, `categories: [Releases]` and `tags: [System Monitor]` front matter.
- If you rename or move a page, add a redirect in `netlify.toml`.
