# Publication ordering and research topics — October 30, 2026

The author approved direct publication on October 30, 2026, and subsequently
chose restoration of the original research-topic groups without a sorting
explanation on the public pages.
Existing CCF labels, JCR quartiles and **JIF percentiles** are retained. The
previous live source is frozen at `9490f57168592bd28a7fe2f3a43fbf398f298d6d` on
`backup/pre-topic-groups-2026-10-30`; see [restore steps](RESTORE.md).

## Display policy

- Home retains the same five selected papers, figures, summaries and links.
  Its order is QS-QIM-RRW, DNLMark, GenPTW, FrPCET-RRW, STDM-RRW.
- Both Publications pages contain all 17 papers in the original three research
  topics. Each topic is ordered by the displayed citation year, descending,
  then by the verified publication/platform date for papers in the same year.
  The navigation links point to the three topic headings. There are no year
  headings, year navigation or sorting-explanation paragraphs on the public page.
  Topic links use native anchors and CSS scroll margin to clear the sticky
  masthead. Other smooth scrolling and all figure-zoom code are unchanged.
- The source bibliography remains `_pages/includes/pub_short.md`. Dates and
  display order live in `_data/publication_chronology.json`; Chinese-language
  citation translations remain in `_data/publication_translations.json`.
- The final JoCS paper has no verified exact online date. It stays last in
  Evolutionary Computation, retaining its 2018 citation year. Its `sort_date` is null.
  No date is inferred from its DOI registration or author upload timestamp.
- The frozen original-profile page, all archive source files, the two PI
  projects, awards, education, image assets and zoom code are preserved.

## Citation years

No demonstrable year error was found in the original citation records. These
valid differences are preserved rather than silently rewriting bibliography:

| Paper | Citation year retained | Sort date | Reason |
| --- | --- | --- | --- |
| SLMark | 2025 | 2026-04-01 | CRESS 2025; IEEE Xplore added it in 2026 |
| PHT-RRW | 2024 | 2023-10-18 | Journal volume year differs from first online year |
| SSCI elite-learning paper | 2019 | 2020-02-20 | SSCI 2019; IEEE Xplore added it in 2020 |
| FrPCET-RRW | 2025 | 2025-10-20 | Existing year is the verified first publication year; final volume is 2026 |
| PZMs-RRW | 2022 | 2022-10-25 | Existing year is the verified first publication year; final issue is 2023 |

For IEEE conferences, Date Added to IEEE Xplore records platform availability,
not acceptance or the event date. IJCINI uses the publisher's publication date
2021-10-01; the page does not separately identify an online-first date. The
publisher date is preferred over conflicting Crossref print metadata.

## Verified dates and primary sources

| Paper | Sort date | Primary evidence |
| --- | --- | --- |
| QS-QIM-RRW | 2026-10-26 | [IEEE Date of Publication](https://ieeexplore.ieee.org/document/11753674) |
| JPEG robust reversible watermarking | 2026-10-21 | [Publisher online date](https://www.joca.cn/EN/10.11772/j.issn.1001-9081.2026091086) |
| Camera imaging style protection | 2026-05-12 | [Publisher online date](https://www.cjig.cn/zh/article/doi/10.11834/jig.260043/) |
| DNLMark | 2026-04-21 | [IEEE Date Added](https://ieeexplore.ieee.org/abstract/document/11464215) |
| SLMark | 2026-04-01 | [IEEE Date Added](https://ieeexplore.ieee.org/abstract/document/11452609/) |
| GenPTW | 2026-03-14 | [AAAI Published date](https://ojs.aaai.org/index.php/AAAI/article/view/37412) |
| FrPCET-RRW | 2025-10-20 | [IEEE Date of Publication](https://ieeexplore.ieee.org/abstract/document/11207540/) |
| STDM-RRW | 2024-03-04 | [IEEE Date of Publication](https://ieeexplore.ieee.org/document/10458701) |
| PHT-RRW | 2023-10-18 | [Publisher article](https://www.sciencedirect.com/science/article/abs/pii/S0020025523013713); Available online in the original publisher PDF |
| PZMs-RRW | 2022-10-25 | [IEEE Date of Publication](https://ieeexplore.ieee.org/document/9928284/) |
| Global-detection PSO, IJCINI | 2021-10-01 | [Publisher publication-date metadata](https://www.igi-global.com/article/a-dynamic-multi-swarm-particle-swarm-optimization-with-global-detection-mechanism/294566) |
| Pigeon-inspired optimization, IJCSM | 2021-08-02 | [Publisher Published online](https://www.inderscience.com/info/e_inarticle.php?artid=116762) |
| Elite-learning PSO, SSCI | 2020-02-20 | [IEEE Date Added](https://ieeexplore.ieee.org/document/9002680/) |
| Global PSO, Computing | 2020-01-04 | [Springer Published date](https://link.springer.com/article/10.1007/s00607-019-00782-9) |
| Elite-learning PSO, IEEE Access | 2019-12-19 | [IEEE Date of Publication](https://ieeexplore.ieee.org/document/8936982/) |
| Global PSO, CEC | 2019-08-08 | [IEEE Date Added](https://ieeexplore.ieee.org/document/8790324/) |
| Firefly/PSO hybrid, JoCS | Exact online day unverified | [Journal issue: May 2018](https://www.sciencedirect.com/science/article/abs/pii/S1877750317303538) |
