# When AI Exposure Rankings Disagree

## Paper
**When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations**

This repository contains the author version of the paper, supplementary material, LaTeX sources, deterministic figure builder, and compiled PDFs.

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

### Final mathematical closure
The author version incorporates the exact endpoint/tie semantics for support-contraction breakpoints; separates retained width g from the optional reparameterization phi; sharpens Theorem 1; uses the V_k corner expression for exact box regret; explicitly defines capture and relative/absolute regret; and states the point-core nesting condition.

### Build
GitHub Actions regenerates the three manuscript figures from the locked reported values, compiles `source/main.tex` and `source/supplement.tex`, and writes the PDFs under `paper/`.
