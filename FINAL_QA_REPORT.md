# Final QA report

## Production checks

- Local final main manuscript: **6 pages**.
- Local final Supplementary Material: **4 pages**.
- Local main + supplement combined: **10 pages**.
- Publication-facing PDFs are searchable and render cleanly.
- No Type 3 fonts are present; all listed fonts are embedded Type 1 fonts.
- LaTeX compilation completed with no undefined references/citations and no overfull boxes.
- Author order, affiliations, and emails were checked against the supplied author metadata.
- The manuscript title and applied framing are consistent across main paper, supplement, and repository documentation.
- Publication-facing source contains no anonymous-manuscript label or internal version/QA language.

## Scientific/numerical checks

- Fresh screened objective: **0.034762467515120**; reported MIP gap **0.0**.
- Fresh unscreened objective: **0.034762467515120**; reported MIP gap **0.0**.
- Screened and unscreened selected 25-member sets: **identical**.
- Current selection set equals the archived baseline selection set: **PASS**.
- Fixed-list performance values equal the archived baseline to better than `1e-12`: **PASS**.
- Coherent Top-25 intersection/union: **14 / 37**.
- Occupational stability partition: **14 / 23 / 624**.
- Independent-box guaranteed/possible: **4 / 87**.
- Transition-boundary semantics were corrected without changing the numerical boundary values.

## Local release SHA-256

- Main PDF: `3adc97f424a435eae513481b0f64ce8232c26b4d2f14ca836092b946a54ae0c4`
- Supplement PDF: `81d39ea1f94278f71cd856bc1a950c969686218d36ae3970b6f157d0f766766a`
- Combined PDF: `986e8978268c0ff7f80ac3829fda7213929cda5cfb8127f83e08f8b602fa4bee`

The GitHub workflow independently recompiles the same source and writes its own `GITHUB_BUILD_SHA256.txt`; byte-level PDF hashes can differ across TeX environments even when the source and reported results are unchanged.
