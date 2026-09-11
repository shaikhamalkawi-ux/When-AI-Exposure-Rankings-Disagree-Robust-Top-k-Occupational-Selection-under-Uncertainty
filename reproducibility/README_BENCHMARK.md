# Consensus-frequency benchmark addendum

This addendum documents the non-optimization comparator in the submission-final manuscript.

## Definition
For each occupation i, count how many of the 18 coherent scenario-specific Top-25 lists contain it:

`f_i = sum_t 1{i in Top25_t}`.

Select the 25 occupations with the largest counts. Equal counts are broken deterministically by ascending SOC code. In the retained data the membership cutoff is strict: the 25th occupation appears in 9 scenario Top-25 lists and the 26th appears in 8, so the tie-break does not affect membership.

The occurrence fraction `f_i/18` is a design-frequency summary, not a probability, because the 18 scenarios are declared constructions rather than random draws.

## Exact result
- Mean coherent-scenario capture: 0.9700497327168492
- Minimum coherent-scenario capture: 0.9589201511773436
- Maximum relative regret: 0.04107984882265636
- Exact independent-box absolute regret: 0.019521357256671597
- Overlap with relative minimax: 24/25
- Consensus-frequency only: 35-9031, Hosts and Hostesses, Restaurant, Lounge, and Coffee Shop
- Relative-minimax only: 39-3091, Amusement and Recreation Attendants
- Worst consensus-frequency scenario: Microsoft_ai_nonphysical__leave_learning_strategies_out

## Literature basis
The manuscript cites two rank-aggregation / Top-k comparison references only as background; it does not claim that either paper proposes this exact frequency rule.

1. C. Dwork, R. Kumar, M. Naor, and D. Sivakumar, "Rank aggregation methods for the Web," WWW, 2001. DOI: 10.1145/371920.372165.
2. R. Fagin, R. Kumar, and D. Sivakumar, "Comparing top k lists," SIAM Journal on Discrete Mathematics, 17(1), 134-160, 2003. DOI: 10.1137/S0895480102412856.

## Public derived ledgers
- `consensus_frequency_selection.csv`: complete 25-member consensus list and occurrence counts.
- `consensus_frequency_scenario_performance.csv`: all 18 scenario-specific capture/regret values.
- `consensus_frequency_summary.csv` / `.json`: headline metrics and the one-item disagreement.

The complete downloadable author package additionally carries the frozen 661x18 priority matrix, interval/core ledger, retained relative-minimax selection, and deterministic benchmark script used to regenerate these derived ledgers.
