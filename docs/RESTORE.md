# Website restore points

## Before the chronological-publications release of October 30, 2026

The author approved chronological ordering and direct publication on October 30,
2026, retaining the existing JIF percentiles. The previous live bilingual site
is preserved exactly at:

- Commit: `d947d8d23323640da7567afe58f17df4a4441cd2`
- Backup branch: [`backup/pre-chronological-order-2026-10-30`](https://github.com/yichao-tang/yichao-tang.github.io/tree/backup/pre-chronological-order-2026-10-30)
- [Download that source ZIP](https://github.com/yichao-tang/yichao-tang.github.io/archive/d947d8d23323640da7567afe58f17df4a4441cd2.zip)

Leave this backup branch unchanged. Local copies outside the working checkout
are `homepage-before-chronological-order-2026-10-30.zip` and the verified,
complete-history `homepage-before-chronological-order-2026-10-30.bundle`.
All earlier backup branches and archives below remain available.

For an immediate undo, use **Revert** on the merged chronological-publications
pull request, then merge the resulting restore pull request. For an exact
restore after subsequent changes, use a clean checkout and a new branch:

```powershell
git fetch origin
git switch -c restore/pre-chronological-order-2026-10-30 origin/main
git restore --source=d947d8d23323640da7567afe58f17df4a4441cd2 --staged --worktree -- .
git diff --cached --stat
git commit -m "Restore bilingual homepage before chronological publication ordering"
git push -u origin restore/pre-chronological-order-2026-10-30
```

Open and merge a pull request to `main`, then wait for GitHub Pages deployment.
This preserves Git history and requires no force push. An exact restore also
removes later source changes.

## Before the two-paper and PI-project update of October 30, 2026

The author approved this bilingual content update for publication on
October 30, 2026. It adds two papers and limits the current project lists to
the two Principal Investigator projects. The live version immediately before
this update is preserved exactly at:

- Commit: `972fc301363441c9be20aafd500c82f0057e7e82`
- Backup branch: [`backup/pre-two-papers-2026-10-30`](https://github.com/yichao-tang/yichao-tang.github.io/tree/backup/pre-two-papers-2026-10-30)
- [Download that source ZIP](https://github.com/yichao-tang/yichao-tang.github.io/archive/972fc301363441c9be20aafd500c82f0057e7e82.zip)

Leave this backup branch unchanged. A source ZIP and a verified, complete-history
Git bundle are also saved outside the working checkout as
`homepage-before-two-papers-2026-10-30.zip` and
`homepage-before-two-papers-2026-10-30.bundle`. Earlier backup branches and
archives below remain unchanged.

For an immediate undo, use **Revert** on the merged two-paper/PI-project pull
request, then merge the resulting restore pull request. To restore the exact
snapshot after subsequent changes, use a clean checkout and a new branch:

```powershell
git fetch origin
git switch -c restore/pre-two-papers-2026-10-30 origin/main
git restore --source=972fc301363441c9be20aafd500c82f0057e7e82 --staged --worktree -- .
git diff --cached --stat
git commit -m "Restore bilingual homepage before the two-paper and PI-project update"
git push -u origin restore/pre-two-papers-2026-10-30
```

Open and merge a pull request to `main`, then wait for GitHub Pages deployment.
This preserves Git history and requires no force push. Restoring this exact
snapshot also removes later source changes.

## Before the publication metrics and figure-zoom release

The previous live bilingual website is preserved exactly at:

- Commit: `046a74a5ca147699c02f0541ab9897b01a1a1e2b`
- Backup branch: [`backup/pre-publication-metrics-2026-10-29`](https://github.com/yichao-tang/yichao-tang.github.io/tree/backup/pre-publication-metrics-2026-10-29)
- [Download that source ZIP](https://github.com/yichao-tang/yichao-tang.github.io/archive/046a74a5ca147699c02f0541ab9897b01a1a1e2b.zip)

Leave the backup branch unchanged. It preserves both languages before adding
CCF/JCR/JIF labels and the revised image interaction. A complete Git bundle and
source ZIP were also saved outside the working checkout, alongside the earlier
original-profile backups.

For an immediate undo, use **Revert** on the merged publication-metrics pull
request and merge the resulting restore pull request. To restore the exact
snapshot after subsequent edits, use a clean checkout and a new branch:

```powershell
git fetch origin
git switch -c restore/pre-publication-metrics origin/main
git restore --source=046a74a5ca147699c02f0541ab9897b01a1a1e2b --staged --worktree -- .
git diff --cached --stat
git commit -m "Restore bilingual homepage before publication metrics and zoom changes"
git push -u origin restore/pre-publication-metrics
```

Open and merge a pull request to `main`, then wait for GitHub Pages deployment.
This uses a normal commit and does not rewrite history or require a force push.
The exact-snapshot method intentionally also removes later source changes.

## Original homepage before the October 29, 2026 refresh

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
- `_pages/includes/archive/pub-short-2026-10-29.md` (the original `_pages/includes/pub_short.md`)
- `_pages/includes/archive/projects-2026-10-29.md` (the original `_pages/includes/projects.md`)
- `_pages/includes/awards.md`
- `_pages/includes/others.md`

The main navigation contains Homepage, Publications, and About Me. The homepage
directly introduces the current appointment, research interests, postdoctoral and
Ph.D. background, academic exchange, and email, followed by five selected
publications. `/publications/` contains all 17 publications in a title-first
layout, rendered from `pub_short.md`; the original 15 citations remain intact.
Display order and year navigation follow the audited
`_data/publication_chronology.json`; see [date rules](PUBLICATION-CHRONOLOGY.md).
The two Chinese papers display publisher-supplied Chinese titles, authors and
full journal names on `/zh/publications/`. The build checks every title,
author list, venue/year, and Paper/Code link against that source with
`python3 _tools/check_publications.py _site`. `/about/` contains the complete
biography, research projects, awards, and education. The biography uses a single
Fudan college name in each language, as confirmed by the author. The current
projects include contains only the author's two Principal Investigator projects,
62502093 and 2024075, as requested on October 30, 2026. Their dates and status are
retained as provided. Earlier participating projects remain recoverable from Git
history and the saved backups.

Compatibility routes remain directly accessible without occupying the main
navigation: `/experience/` uses the current projects, awards, and education;
`/profile-2026-10-29/` retains the complete original combination, including the
original biography and five-project snapshots in `includes/archive/`. `/about.html`
continues to redirect to `/about/`.

The five old root-page fragments are handled by a fixed compatibility mapping:
`/#about-me` opens `/about/`; `/#-publications` opens `/publications/`; and
`/#-projects`, `/#-awards`, and `/#-education` open the matching heading on
`/about/`. Unknown fragments are left unchanged. These redirects do not add
duplicate navigation links to the homepage body.

There are 17 current publications, 2 current research projects, 4 awards, and 3
education entries. The frozen original profile retains the original 15 papers
and 5 projects.
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
bibliography. `_data/publication_translations.json` supplies the original Chinese
titles, author names and journal names of the two Chinese-language papers for
the Chinese page. Existing English-language citations remain unchanged.
Chinese project titles and award names use the author's
confirmed wording. Update the paired biography and project files together.

Run `python3 _tools/check_localization.py _site` after building to check the six
routes, metadata, language links, shared publication fields, separate email
paragraphs, and profile record counts. For a build under a path prefix, add
`--baseurl /preview`.
