# Publication metrics: release record, 2026-10-29

The author approved this version for publication on 2026-10-29. The preceding
live version is frozen at `046a74a5ca147699c02f0541ab9897b01a1a1e2b` on
`backup/pre-publication-metrics-2026-10-29`; see [restore instructions](RESTORE.md).

## Display and scope

Both languages and both publication views use the same venue records in
`_data/publication_venues.yml`. The displayed format is:

`IEEE T-MM, 2025 · CCF A · JCR Q1 · JIF percentile: 98.0`

The publication year is the paper's year. Metric editions are independent of
that year: CCF uses the 2026 seventh edition; JCR uses the 2026 release of 2025
data. These are current venue labels, not historical publication-year ratings.
CCF labels are omitted for unlisted venues. JCR/JIF labels apply to journals.
Missing labels are omitted without a dash or placeholder.

For journals in multiple JCR categories, select the category with the highest
JIF percentile, and use that same category's JIF quartile. Do not substitute
JCI percentiles, Scopus/CiteScore categories or CAS divisions. The category,
edition and rank are available in the native hover description; there is no
metrics footnote on the public pages.

All original citation text, authors, years and links remain in
`_pages/includes/pub_short.md`. Publications visibly retains each complete
original venue/year; only Home uses the existing short venue names. The original
profile archive remains unchanged. `check_publications.py` compares all visible
original citation fields while excluding the appended metric labels.

## CCF

[Official 2026 directory announcement](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml)
and its downloadable seventh-edition directory were checked.

- A: TIFS, TMM, AAAI.
- B: TCSVT, Information Sciences, ICASSP.
- C: IEEE CEC.
- Unlisted: CRESS, Computing, IEEE Access, Journal of Computational Science,
  IJCSM, IJCINI, IEEE SSCI. Computing is not Discover Computing.

## JCR sources and calculation

[Clarivate's definition](https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351666061457-Glossary)
defines the JIF percentile from rank R and category size N:

`100 * (N - R + 0.5) / N`, rounded to one decimal for this display.

This is not `100 - R/N*100`; the half-rank term matters. In particular, a
rounded percentile of 75.0 can still accompany Q2 at rank 37/146. Quartiles
must follow the published JIF quartile, not a threshold applied after rounding.

The [Romanian UEFISCDI government JCR table](https://uefiscdi.gov.ro/resource-832709-JCR-2025.iunie-2026.site.pdf)
and [publication page](https://uefiscdi.gov.ro/scientometrie-reviste) identify
2025 data released in June 2026. The table independently confirms journal
quartiles. Rank/percentile evidence below varies in strength and is recorded
explicitly; it is not represented as a direct authenticated JCR export.

| Venue | Selected JIF category | Rank / N | Quartile | Percentile | Evidence |
| --- | --- | --- | --- | --- | --- |
| TIFS | Computer Science, Theory & Methods | 10/146 | Q1 | 93.5 | UAM official university record directly states rank/year/category; PNU cross-check |
| TMM | Computer Science, Software Engineering | 3/128 | Q1 | 98.0 | June 2026 snapshot: PNU university Top 2.34% cross-check plus third-party category transcription |
| TCSVT | Engineering, Electrical & Electronic | 13/369 | Q1 | 96.6 | Two official university announcements directly state rank/year/category |
| Information Sciences | Computer Science, Information Systems | 49/267 | Q1 | 81.8 | PNU university Top 18.35% and N=267 uniquely imply rank 49; third-party rank cross-check |
| Computing | Computer Science, Theory & Methods | 41/146 | Q2 | 72.3 | Third-party direct transcription; UPM official indexed records corroborate rank/category/year |
| IEEE Access | Engineering, Electrical & Electronic | 124/369 | Q2 | 66.5 | HIT university library explicitly lists all three category ranks and percentiles |
| Journal of Computational Science | Computer Science, Theory & Methods | 37/146 | Q2 | 75.0 | Multiple third-party rank transcriptions; government table independently confirms Q2 |
| IJCSM | Engineering, Multidisciplinary | 151/178 | Q4 | 15.4 | Government table resolves N=178 ranked journals; rank 151 is transcribed by AbleSci |
| IJCINI | Computer Science, Artificial Intelligence | 202/210 | Q4 | 4.0 | Multiple third-party JIF-rank transcriptions; government table independently confirms Q4 |

### Source links

- TIFS: [UAM](https://portalcientifico.uam.es/es/ipublic/item/10497477),
  [PNU](https://scholar.pusan.ac.kr/journals/17896/).
- TMM: [PNU researcher's publications](https://scholar.pusan.ac.kr/publications/?scholar_id=1106),
  [IEEE June 2026 report](https://innovate.ieee.org/ieee-journals-continue-to-excel-in-citation-rankings/),
  [third-party full category table](https://www.akaturk.com/journals/16211?lang=en).
- TCSVT: [Hongik University](https://www.hongik.ac.kr/kr/newscenter/news.do?articleNo=158529&mode=view),
  [Ewha University](https://ee.ewha.ac.kr/ewhaeleca/information/news.do?articleNo=783527&mode=view).
- Information Sciences: [PNU](https://scholar.pusan.ac.kr/journals/13889/),
  [CEU category list](https://investigacionusp.ceu.es/en/ipublic/source/5571),
  [LetPub rank cross-check](https://www.letpub.tw/index.php?journalid=3567&page=journalapp&view=detail).
- Computing: [Dizin](https://dizin.docent.com.tr/en/dergiler/0010485X),
  [UPM](https://portalcientifico.upm.es/es/ipublic/item/10380729),
  [second UPM indexed record](https://upm.scimarina.org/en/ipublic/item/10413387).
- IEEE Access: [HIT library, July 2026](https://www.hit.ac.il/students/libary/%D7%A4%D7%A8%D7%A1%D7%95%D7%9E%D7%99-%D7%97%D7%95%D7%A7%D7%A8%D7%99-hit-%D7%97%D7%95%D7%93%D7%A9-%D7%99%D7%95%D7%9C%D7%99-2026/),
  [IEEE official bibliometrics](https://ieeeaccess.ieee.org/about/bibliometrics/).
- Journal of Computational Science: [LetPub](https://apa.letpub.com/index.php?journalid=9509&page=journalapp&view=detail),
  [AbleSci](https://www.ablesci.com/journal/detail?id=DbP0Vp),
  [Akaturk 2025 table](https://akaturk.com/journals/19700174607?lang=en).
- IJCSM conflicting totals: [AbleSci](https://www.ablesci.com/journal/detail?id=5OoNa5),
  [LetPub](https://www.letpub.com/journal-selector/journal/15604).
- IJCINI: [LetPub](https://www.letpub.com/journal-selector/journal/17944),
  [Akaturk 2025 table](https://akaturk.com/journals/19700186872?lang=en).

## Release snapshot and reload limitation

[Clarivate's 2026 update log](https://journalcitationreports.zendesk.com/hc/en-gb/articles/47808147130129-2026)
records an October 14 reload. TMM is explicitly pinned to the June snapshot:
some current third-party pages instead give software engineering 3/130 and
98.1, or telecommunications rank 7 instead of IEEE's June rank 6. A direct JCR
profile/export is needed to establish whether these are reload changes or
transcription errors. Do not describe 98.0 as an authenticated October value.

The government June PDF independently resolves two category-total conflicts:
Software Engineering, pages 184–190, contains 128 records with JIF quartiles;
Engineering, Multidisciplinary, pages 326–331, contains 179 records, of which
one has JIF=N/A and only 178 are ranked. The latter supports IJCSM 151/178 and
15.4, rather than using all 179 directory records as the ranking denominator.
The per-page ranked counts are 19+19+19+19+19+19+14=128 and
29+33+29+32+30+25=178, respectively.

No numeric placeholder or verification-status note is displayed on the website.
