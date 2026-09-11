# When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations

## Authors

1. **Ghassan Malkawi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `gmalkawi@hct.ac.ae`
2. **Ahmed Abdelaziz Elsayed** — Department of Computer Engineering and Computational Sciences, Canadian University Dubai, Dubai, United Arab Emirates — `ahmed.elsayed@cud.ac.ae`
3. **Asem Omari** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aomari@hct.ac.ae`
4. **Azmi Alazzam** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aalazzam@hct.ac.ae`
5. **Said Badreddine** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `sbadreddine@hct.ac.ae`
6. **Shaima Alharthi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `H00543372@hct.ac.ae`

## Research question

AI-exposure measures can disagree about which occupations should receive priority. This study asks two applied questions: which occupations remain Top-25 priorities across all admitted AI-exposure specifications, and, if one fixed Top-25 list is required, which list best controls the worst relative loss across those specifications?

The application covers **661 U.S. occupations** and **18 coherent AI-exposure specifications**.

## Main findings

At `k = 25`:

- **14 occupations** appear in every coherent Top-25 list.
- **23 additional occupations** are design-sensitive: they appear in at least one, but not every, coherent Top-25 list.
- **624 occupations** remain outside every coherent Top-25 in the admitted family.
- The coherent intersection/union sizes are **14 / 37**.
- The independent interval box is more conservative, with **4 guaranteed / 87 possible** members.
- The baseline composite has minimum coherent-scenario capture **93.70%** and maximum relative regret **6.30%**.
- The relative-minimax fixed list raises minimum capture to **96.52%** and lowers maximum relative regret to **3.48%**.
- Under the independent box, the baseline has slightly smaller exact absolute regret (**0.0181**) than the relative-minimax list (**0.0195**). Robustness therefore depends on both the uncertainty set and the decision criterion.

The exact 14 stable occupations are provided in the reproducibility archive and in the Supplementary Material.

## Exact transition-boundary convention

The nested-support analysis uses retained width `g`. Best rank uses the strict comparison `ell_j > u_i`, whereas pessimistic worst rank uses the non-strict comparison `u_j >= ell_i`. Therefore each reported `g*` is a **transition boundary**. The associated post-contraction state applies immediately below that boundary (`g < g*`), not automatically at equality.

- `g* = 0.5743200867`: immediately below, the guaranteed set has 14 members and equals the coherent intersection.
- `g* = 0.4346510223`: immediately below, the possible set has 37 members; 32 identities are shared with the 37-member coherent union.
- `g* = 0.0787564209`: immediately below, the point-core Top-25 is fully identified.

If an auxiliary path parameter is used, the manuscript writes `g = phi(alpha)`, with `phi` a strictly decreasing endpoint-preserving homeomorphism. Such a parameter is not a probability or confidence level.

## Reproducing the results

The reproducibility archive contains the exact 661x18 priority matrix, interval/core ledger, scenario register, executable code, generated outputs, reference outputs, and SHA-256 manifest. The default solve uses theorem-equivalent lossless screening; the optional unscreened run solves all 661 item binaries. In the packaged environment both return zero reported MIP gap and the same 25-member selection.

## Repository contents

- `paper/` — final main manuscript and supplementary material.
- `source/` — final LaTeX source plus the complete source archive.
- `reproducibility/` — reproduction instructions/code plus the complete reproducibility archive.
- `MATH_AND_NOTATION_CHANGES.md` — mathematical/notation corrections made in the author revision without changing the numerical results.
- `FINAL_QA_REPORT.md` — final production checks and artifact hashes.

## Interpretation boundary

The paper provides a **screening and decision certificate** over declared uncertainty structures. It does **not** estimate selection probability, validate AI exposure as a causal construct, forecast displacement, estimate worker-transition probability, establish individual eligibility, or predict program success.
