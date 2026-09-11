# When AI Exposure Rankings Disagree

## Paper
**When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations**

This repository contains the final author version, Supplementary Material, LaTeX sources, deterministic figure builder, and compiled PDFs.

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

### Final closure
The author version now includes: exact endpoint/tie semantics for support-contraction boundaries; separate retained-width g and optional phi(alpha) reparameterization; the ordered guaranteed-set insertion argument in Theorem 1; explicit construction of the frozen modifier q_i^t from exposure and five O*NET skills; exact V_k box-regret notation; explicit relative and absolute regret definitions; SOC codes for the 14 coherent-stable occupations; and citations renumbered in IEEE first-appearance order.

The nonessential underdefined SIPP diagnostic was removed from this conference paper rather than overinterpreted. The final Main uses 28/28 references, all cited. The Supplement uses 5/5 references, all cited.

### Figures
All manuscript figures use bold labels, titles, tick text, and annotations. All four plot spines are shown, and the annotations are positioned inside the plotting rectangle so labels such as `Scale only` and `g*=0.078756` are not clipped.

### Current build
- Main manuscript: 5 pages.
- Supplement: 3 pages.
- Combined: 8 pages.
- GitHub Actions rebuild: PASS.
- Undefined citations/references: 0.
- Overfull boxes: 0.
- Type-3 fonts: 0; PDF fonts embedded.

GitHub Actions regenerates the three manuscript figures, compiles `source/main.tex` and `source/supplement.tex`, and writes current PDFs under `paper/`.
