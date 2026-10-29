# Publication figures

All five selected papers use original figures or a complete original subfigure extracted from the
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
| GenPTW | Fig. 2 / page 4 | [52, 52, 560, 252] | 450 | 1200 x 472 |
| DNLMark | Fig. 1 / page 3 | [77.94, 69.84, 536.04, 263.88] | 400 | 1200 x 508 |
| FrPCET-RRW | Fig. 2 / page 5 | [43.92, 64.98, 279, 358.02] | 400 | 1200 x 1496 |
| STDM-RRW | Fig. 2(b) / page 6 | [324, 132.96, 567.96, 321.96] | 600 | 1200 x 930 |

## Sources and figure selection

- **QS-QIM-RRW:** author's final submitted version of [the T-IFS paper](https://ieeexplore.ieee.org/document/11753674). Figure 4 shows decoding-region equalization and the resulting quantization strips. It is more compact than the full embedding/extraction flowcharts.
- **GenPTW:** author's camera-ready version of [the AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/37412). Figure 2 shows the attention and spatial fusion modules, plus the joint extraction and localization branches.
- **DNLMark:** author's copy of [the ICASSP paper](https://ieeexplore.ieee.org/document/11464215). Figure 1 retains the complete architecture, including the image-noise and latent-noise branches and the frozen/trainable legend.
- **FrPCET-RRW:** author's published copy of [the T-MM paper](https://ieeexplore.ieee.org/document/11207540/). Figure 2 shows all four optimized-QIM cases, illustrating the smaller quantization error from choosing adjacent intervals.
- **STDM-RRW:** author's published copy of [the T-IFS paper](https://ieeexplore.ieee.org/document/10458701). Complete original panel 2(b) shows the proposed multi-level quantizer and all four embedding-strength levels. An [author-hosted copy](https://www.comp.hkbu.edu.hk/~ymc/papers/journal/TIFS3372811.pdf) is also public.

The generic receiver/reconstruction diagrams from the earlier preview are no
longer selected. Figure identifiers remain here for provenance, with no added
figure captions below the homepage thumbnails.

The short contribution sentences in `_data/selected_publications.yml` paraphrase
the corresponding abstracts, method descriptions, contribution lists and
conclusions. They introduce no numerical or universal robustness claims.
