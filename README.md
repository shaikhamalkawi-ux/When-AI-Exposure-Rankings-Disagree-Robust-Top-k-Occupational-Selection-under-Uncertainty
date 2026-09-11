# When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations

This repository accompanies the paper **“When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations.”**

## Authors

1. **Ghassan Malkawi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `gmalkawi@hct.ac.ae`
2. **Ahmed Abdelaziz Elsayed** — Department of Computer Engineering and Computational Sciences, Canadian University Dubai, Dubai, United Arab Emirates — `ahmed.elsayed@cud.ac.ae`
3. **Asem Omari** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aomari@hct.ac.ae`
4. **Azmi Alazzam** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aalazzam@hct.ac.ae`
5. **Said Badreddine** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `sbadreddine@hct.ac.ae`
6. **Shaima Alharthi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `H00543372@hct.ac.ae`

## Applied question

AI-exposure measures can disagree about which occupations should receive priority. This study asks which occupations remain Top-25 priorities across the admitted AI-exposure specifications and, when one fixed Top-25 list is required, which list best protects worst-case priority capture.

The application covers **661 U.S. occupations** and **18 coherent AI-exposure specifications**.

## Main findings at k = 25

- **14 occupations** appear in every coherent Top-25 list.
- **23 additional occupations** are design-sensitive: they appear in at least one, but not every, coherent Top-25 list.
- **624 occupations** remain outside every coherent Top-25 in the admitted family.
- Coherent intersection / union: **14 / 37**.
- Independent-box guaranteed / possible: **4 / 87**.
- Baseline minimum coherent-scenario capture: **93.70%**.
- Relative-minimax minimum coherent-scenario capture: **96.52%**.
- Baseline exact independent-box absolute regret: **0.0181**.
- Relative-minimax exact independent-box absolute regret: **0.0195**.

Robustness therefore depends on both the uncertainty structure and the decision criterion.

## Exact transition-boundary convention

Best rank uses the strict comparison `ell_j > u_i`, whereas pessimistic worst rank uses the non-strict comparison `u_j >= ell_i`. Each reported retained-width value `g*` is therefore a **transition boundary**. When contraction proceeds from `g = 1` toward `g = 0`, the associated post-contraction membership state applies immediately below the boundary (`g < g*`).

An auxiliary path parameter is written `g = phi(alpha)`, with `phi` a strictly decreasing endpoint-preserving homeomorphism. It is not interpreted as a probability or confidence level.

## Repository contents

- `paper/When_AI_Exposure_Rankings_Disagree_Main.pdf` — author version of the main paper.
- `paper/When_AI_Exposure_Rankings_Disagree_Supplement.pdf` — supplementary material.
- `source/main.tex` and `source/supplement.tex` — LaTeX sources.
- `source/fig1_membership.png`, `source/fig2_contraction.png`, `source/fig3_tradeoff.png` — figures used in the manuscript.
- `MATH_AND_NOTATION_CHANGES.md` — mathematical/notation correction record.
- `FINAL_QA_REPORT.md` — production audit record.

## Reproducibility boundary

The paper describes a 661×18 primitive priority matrix, interval/core ledger, selected-list outputs, scenario-level capture/regret calculations, and solver metadata. The authoritative empirical calculation archive is not reconstructed from headline values here. It should be added only from the retained source archive so that no row-level object is reverse-engineered from published summaries.

## Interpretation boundary

The paper provides a **screening and decision certificate** over declared uncertainty structures. It does **not** estimate selection probability, validate AI exposure as a causal construct, forecast displacement, estimate worker-transition probability, establish individual eligibility, or predict program success.
