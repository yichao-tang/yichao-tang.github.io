# Publication figures

All five selected papers use complete original figures extracted from the
author-supplied PDFs. The manuscripts themselves are not included in the site.
Only surrounding page furniture, body text, and separate captions are outside
the crops. No scientific elements, labels, arrows, results, or colors have been
redrawn, removed, or generated.

Each homepage thumbnail is a proportionally resized 1200-pixel-wide WebP. The
larger PNG linked from the thumbnail preserves the original figure crop at high
resolution. Display uses `object-fit: contain`, without stretching or cropping
the figure to fill its reserved display area.

Coordinates below are PDF points, origin at the top-left: `[left, top, right,
bottom]`. PDF page numbers are one-based.

| Paper | Figure / PDF page | Crop | Render DPI | WebP dimensions |
| --- | --- | --- | --- | --- |
| QS-QIM-RRW | Fig. 4 / page 6 | [75.96, 200.04, 273.96, 313.08] | 600 | 1200 x 685 |
| GenPTW | Fig. 1 / page 1 | [319, 232, 558, 344] | 450 | 1200 x 562 |
| DNLMark | Fig. 1 / page 3 | [77.94, 69.84, 536.04, 263.88] | 400 | 1200 x 508 |
| FrPCET-RRW | Fig. 4 / page 7 | [33.84, 63.90, 297.90, 253.98] | 400 | 1200 x 864 |
| STDM-RRW | Fig. 3 / page 8 | [327, 52, 548, 274] | 450 | 1200 x 1205 |

## Sources and figure selection

- **QS-QIM-RRW:** author's final submitted version of [the T-IFS paper](https://ieeexplore.ieee.org/document/11753674). Figure 4 shows decoding-region equalization and the resulting quantization strips. It is more compact than the full embedding/extraction flowcharts.
- **GenPTW:** author's camera-ready version of [the AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/37412). Figure 1 illustrates generation/embedding, editing, provenance extraction, and tamper localization.
- **DNLMark:** author's copy of [the ICASSP paper](https://ieeexplore.ieee.org/document/11464215). Figure 1 retains the complete architecture, including the image-noise and latent-noise branches and the frozen/trainable legend.
- **FrPCET-RRW:** author's published copy of [the T-MM paper](https://ieeexplore.ieee.org/document/11207540/). Figure 4 shows watermark extraction and the separate intact-image reconstruction path.
- **STDM-RRW:** author's published copy of [the T-IFS paper](https://ieeexplore.ieee.org/document/10458701). Figure 3 shows extraction after attacks and recovery of the original image only when unattacked. An [author-hosted copy](https://www.comp.hkbu.edu.hk/~ymc/papers/journal/TIFS3372811.pdf) is also public.

The short contribution sentences in `_data/selected_publications.yml` paraphrase
the corresponding abstracts, method descriptions, contribution lists and
conclusions. They introduce no numerical or universal robustness claims.
