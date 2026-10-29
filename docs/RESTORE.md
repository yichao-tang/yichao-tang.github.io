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

- `_pages/includes/intro.md`
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
`python3 _tools/check_publications.py _site`. `/about/` contains the full original biography,
research projects, awards, and education. The current projects include contains
six entries: the five original projects and the added General Program project
62672118, placed immediately above project 62572125. Its dates and `Ongoing`
status are retained as provided.

Compatibility routes remain directly accessible without occupying the main
navigation: `/experience/` retains all projects, awards, and education;
`/profile-2026-10-29/` retains the complete original combination, including the
five-project snapshot from `includes/archive/projects-2026-10-29.md`. `/about.html`
continues to redirect to `/about/`.

The five old root-page fragments are handled by a fixed compatibility mapping:
`/#about-me` opens `/about/`; `/#-publications` opens `/publications/`; and
`/#-projects`, `/#-awards`, and `/#-education` open the matching heading on
`/about/`. Unknown fragments are left unchanged. These redirects do not add
duplicate navigation links to the homepage body.

All 15 publications, 6 current research projects, 4 awards, and 3 education entries
remain. The frozen original profile continues to contain the original 5 projects.
Existing HTML comments remain comments rather than being promoted to public text.
