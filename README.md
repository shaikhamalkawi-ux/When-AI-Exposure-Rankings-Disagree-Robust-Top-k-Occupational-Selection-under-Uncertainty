# When AI Exposure Rankings Disagree

## Paper
**When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations**

This repository contains the submission-final author version, Supplementary Material, LaTeX sources, deterministic figure builder, compiled PDFs, and the public derived ledgers for the Consensus-Frequency sanity-check benchmark.

### Authors
1. Ghassan Malkawi — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — gmalkawi@hct.ac.ae
2. Ahmed Abdelaziz Elsayed — Department of Computer Engineering and Computational Sciences, Canadian University Dubai, Dubai, United Arab Emirates — ahmed.elsayed@cud.ac.ae
3. Asem Omari — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — aomari@hct.ac.ae
4. Azmi Alazzam — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — aalazzam@hct.ac.ae
5. Said Badreddine — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — sbadreddine@hct.ac.ae
6. Shaima Alharthi — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — H00543372@hct.ac.ae

### Main applied findings
- 661 U.S. occupations and 18 coherent AI-exposure specifications.
- At k=25: 14 occupations occur in every coherent Top-25; 37 occur in at least one.
- The independent interval box yields 4 guaranteed and 87 possible Top-25 members.
- Relative minimax raises worst-scenario capture from 93.70% (baseline composite) to 96.52%.
- The resulting list is for screening and further assessment, not a displacement forecast, worker-transition probability, or program-success prediction.

### Compact Consensus-Frequency benchmark
A transparent comparator selects the 25 occupations that appear most often in the 18 scenario-specific Top-25 lists. This is an occurrence-frequency rank-aggregation benchmark, not a probability model.

Verified values:
- Mean capture: 97.00%.
- Minimum capture: 95.89%.
- Maximum relative regret: 4.11%.
- Exact independent-box absolute regret: 0.01952.
- Overlap with relative minimax: 24/25.

Relative minimax remains 96.99% mean capture, 96.52% minimum capture, 3.48% maximum relative regret, and 0.01945 exact box regret. The interpretation is deliberately narrow: the frequency benchmark has a marginally higher mean capture, while relative minimax provides stronger protection on the worst-case relative-capture/regret criterion it explicitly optimizes. No universal-dominance claim is made.

### Final mathematical/editorial closure
The author version includes: exact endpoint/tie semantics for support-contraction boundaries; separate retained-width g and optional phi(alpha) reparameterization; the ordered guaranteed-set insertion argument in Theorem 1; explicit construction of the frozen modifier from exposure and five O*NET skills; a definition of the indicator function; explicit positivity of V_t* before capture normalization; exact V_k box-regret notation; complete binary constraints in the absolute-minimax sensitivity; SOC codes for the 14 coherent-stable occupations; and cleaned symbol roles for exposure-channel, selected-mass, proof-item, and support-width notation.

The nonessential underdefined SIPP diagnostic was removed rather than overinterpreted. The Main uses 30/30 references, all cited in IEEE first-appearance order. The Supplement uses 5/5 references, all cited.

### Figures
The plots retain bold titles, axes, tick text, legends, and annotations inside four-sided frames. Manuscript captions describe only the scientific content; production-formatting instructions were removed from all three captions.

### Reproducibility
The `reproducibility/` directory exposes the complete consensus list, its scenario-by-scenario capture/regret ledger, machine-readable summary values, and a benchmark note. The complete downloadable author package additionally carries the frozen 661x18 priority matrix, interval/core ledger, relative-minimax selection, and deterministic benchmark script used to regenerate these outputs.

### Current build
- Main manuscript: 5 pages.
- Supplement: 3 pages.
- Combined: 8 pages.
- GitHub Actions rebuild: PASS.
- Undefined citations/references: 0.
- Overfull boxes: 0.
- Type-3 fonts: 0; PDF fonts embedded.

GitHub Actions regenerates the three manuscript figures, compiles `source/main.tex` and `source/supplement.tex`, and writes current PDFs under `paper/`.
