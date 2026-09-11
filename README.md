# When AI Exposure Rankings Disagree: Robust Top-25 Selection Across 661 U.S. Occupations

This repository accompanies the applied author version of the CAISAIS 2026 paper. The scientific numerical results remain those of the locked V6R1 lineage; this production pass improves application framing, author metadata, and exact mathematical/notation wording without changing the 661-occupation dataset, 18-scenario matrix, selected lists, solver results, or headline conclusions.

## Authors

1. **Ghassan Malkawi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `gmalkawi@hct.ac.ae`
2. **Ahmed Abdelaziz Elsayed** — Department of Computer Engineering and Computational Sciences, Canadian University Dubai, Dubai, United Arab Emirates — `ahmed.elsayed@cud.ac.ae`
3. **Asem Omari** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aomari@hct.ac.ae`
4. **Azmi Alazzam** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `aalazzam@hct.ac.ae`
5. **Said Badreddine** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `sbadreddine@hct.ac.ae`
6. **Shaima Alharthi** — Faculty of Computer Information Science, Higher Colleges of Technology, Al Ain, Abu Dhabi, United Arab Emirates — `H00543372@hct.ac.ae`

## Applied question

AI-exposure measures can disagree about which occupations should receive priority. The paper asks which occupations remain Top-25 priorities across admitted AI-exposure specifications and, when one fixed Top-25 list is required, which list best protects worst-case priority capture.

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

## Exact transition-boundary convention

Best rank uses the strict comparison `ell_j > u_i`, while pessimistic worst rank uses the non-strict comparison `u_j >= ell_i`. Reported retained-width values `g*` are therefore treated as **transition boundaries**. Post-contraction membership statements are evaluated immediately below a boundary (`g < g*`) rather than treating a rounded breakpoint as an interior state.

The auxiliary path parameter is written `g = phi(alpha)`, where `phi:[0,1]->[0,1]` is a strictly decreasing endpoint-preserving homeomorphism. It is not a probability or confidence level.

## Stable occupations across all 18 coherent Top-25 lists

General and Operations Managers; Accountants and Auditors; Registered Nurses; Waiters and Waitresses; Janitors and Cleaners, Except Maids and Housekeeping Cleaners; Cashiers; Retail Salespersons; Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products; Bookkeeping, Accounting, and Auditing Clerks; Receptionists and Information Clerks; Secretaries and Administrative Assistants, Except Legal, Medical, and Executive; Office Clerks, General; Heavy and Tractor-Trailer Truck Drivers; Stockers and Order Fillers.

## Repository contents

- `paper/When_AI_Exposure_Rankings_Disagree_Main.pdf` — compiled main paper.
- `paper/When_AI_Exposure_Rankings_Disagree_Supplement.pdf` — compiled Supplementary Material.
- `paper/When_AI_Exposure_Rankings_Disagree_Main_and_Supplement.pdf` — combined paper and supplement.
- `source/main.tex` and `source/supplement.tex` — LaTeX sources.
- `source/figures/` — reproducibly generated figures.
- `reproducibility/` — retained 661x18 matrix, interval/core ledger, executable code, generated/reference outputs, environment metadata, and checksums.
- `MATH_AND_NOTATION_CHANGES.md` — exact correction record.
- `FINAL_QA_REPORT.md` — mathematical and production audit.
- `CITATION.cff` — repository citation metadata.

## Reproduction

From the `reproducibility` directory run:

```bash
python reproduce_beyondair.py
python reproduce_beyondair.py --unscreened
```

In the verification run used for this author build, the theorem-equivalent screened and full 661-binary formulations both returned zero reported MIP gap and the same 25-member relative-minimax list. The objectives were `0.03476246751512021` and `0.03476246751512037`, respectively.

## Interpretation boundary

The paper provides a **screening and decision certificate** over declared uncertainty structures. It does **not** estimate selection probability, validate AI exposure as a causal construct, forecast displacement, estimate worker-transition probability, establish individual eligibility, or predict program success.
