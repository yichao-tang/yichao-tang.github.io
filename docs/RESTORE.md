# Restore the website before the October 29, 2026 refresh

The starting version is preserved at:

- Commit: `47fc8df8d18645beb9663a11f18d4005a1e7e503`
- Backup branch: [`backup/pre-homepage-refresh-2026-10-29`](https://github.com/yichao-tang/yichao-tang.github.io/tree/backup/pre-homepage-refresh-2026-10-29)
- [Download the original source ZIP](https://github.com/yichao-tang/yichao-tang.github.io/archive/47fc8df8d18645beb9663a11f18d4005a1e7e503.zip)

The backup branch points to the exact original commit. Leave it unchanged.

## Before this refresh is merged

The production site continues to use `main`. Close the refresh pull request to
discard the proposed redesign; no production rollback is needed.

## After this refresh is merged

For a simple undo immediately after merging, use **Revert** on the merged pull
request, review the resulting pull request, then merge it. This keeps Git history.

To return to the exact saved source after later edits, start with a clean clone
and create a restore branch. The following restores the saved files in a new
commit; it does not force-push or rewrite history:

```powershell
git fetch origin
git switch -c restore/homepage-2026-10-29 origin/main
git restore --source=47fc8df8d18645beb9663a11f18d4005a1e7e503 --staged --worktree -- .
git diff --cached --stat
git commit -m "Restore homepage to the saved October 29, 2026 version"
git push -u origin restore/homepage-2026-10-29
```

Open a pull request from the restore branch to `main` and review it before merging.
That full restore intentionally removes changes introduced after the saved version.

## Content preservation

The refresh keeps these original source files byte-for-byte:

- `_pages/includes/archive/intro-2026-10-29.md` (the original `_pages/includes/intro.md`)
- `_pages/includes/pub_short.md`
- `_pages/includes/archive/projects-2026-10-29.md` (the original `_pages/includes/projects.md`)
- `_pages/includes/awards.md`
- `_pages/includes/others.md`

The main navigation contains Homepage, Publications, and About Me. The homepage
directly introduces the current appointment, research interests, postdoctoral and
Ph.D. background, academic exchange, and email, followed by five selected
publications. `/publications/` contains all 15 publications in a title-first
layout, rendered from the unchanged `pub_short.md`. The build checks every title,
author list, venue/year, and Paper/Code link against that source with
`python3 _tools/check_publications.py _site`. `/about/` contains the complete
biography, research projects, awards, and education. The biography uses a single
Fudan college name in each language, as confirmed by the author. The current
projects include contains seven entries:
the five original projects, General Program project 62672118 immediately above
62572125, and project 62066014 immediately after 62172165. Their dates and status
are retained as provided.

Compatibility routes remain directly accessible without occupying the main
navigation: `/experience/` retains all projects, awards, and education;
`/profile-2026-10-29/` retains the complete original combination, including the
original biography and five-project snapshots in `includes/archive/`. `/about.html`
continues to redirect to `/about/`.

The five old root-page fragments are handled by a fixed compatibility mapping:
`/#about-me` opens `/about/`; `/#-publications` opens `/publications/`; and
`/#-projects`, `/#-awards`, and `/#-education` open the matching heading on
`/about/`. Unknown fragments are left unchanged. These redirects do not add
duplicate navigation links to the homepage body.

All 15 publications, 7 current research projects, 4 awards, and 3 education entries
remain. The frozen original profile continues to contain the original 5 projects.
Existing HTML comments remain comments rather than being promoted to public text.

## English and Chinese pages

The right-hand language links switch between corresponding primary pages:

| English | Chinese |
| --- | --- |
| `/` | `/zh/` |
| `/publications/` | `/zh/publications/` |
| `/about/` | `/zh/about/` |

These are static pages with ordinary links; switching does not depend on browser
language detection or a translation service. The original English profile is a
frozen archive and does not declare a Chinese counterpart. Its language control
leads to the current Chinese About page.

Interface labels and the route mapping live in `_data/i18n.yml`. Chinese paper
summaries and image descriptions are paired with the original fields in
`_data/selected_publications.yml`. Both full publication lists render the same
original bibliography: titles, authors, venues, years, and links remain in their
published language. Chinese project titles and award names use the author's
confirmed wording. Update the paired biography and project files together.

Run `python3 _tools/check_localization.py _site` after building to check the six
routes, metadata, language links, shared publication fields, separate email
paragraphs, and profile record counts. For a build under a path prefix, add
`--baseurl /preview`.
