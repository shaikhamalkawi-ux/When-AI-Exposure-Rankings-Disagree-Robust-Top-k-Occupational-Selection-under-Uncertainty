# Mathematical and notation corrections in the author revision

This revision changes presentation and notation but does **not** change the underlying 661 x 18 data, the selected 25-member relative-minimax list, any reported capture/regret value, or the three numerical support-contraction boundary values.

1. **Tie-sensitive transition boundaries.** The best-rank certificate uses a strict `>` comparison and the pessimistic worst-rank certificate uses a non-strict `>=` comparison. The reported `g*` values are therefore described as transition boundaries; post-contraction set identities/counts apply on the `g < g*` side.
2. **No symbol overloading.** `g` is retained support width. A decreasing reparameterization is written as `phi`, with `g = phi(alpha)`.
3. **Safe-screening theorem.** The objective is stated as a minimization objective that is coordinatewise nonincreasing in scenario-wise selected mass. The proof now states that the exchange step strictly increases the scenario-mass vector, avoiding an unnecessary claim that the objective value must improve strictly.
4. **Fixed-list box regret.** The exact formula is written with `V_k(v(X))`, avoiding set-identity ambiguity when the maximizing corner contains ties.
5. **Core containment.** The text states explicitly that `ell_i <= c_i <= u_i` because the declared core is one of the primitive scenarios.
6. **Relative-minimax notation.** Scenario capture is explicitly defined, the regret relation `R_t = 1 - C_t` is stated, and `0 <= rho <= 1` is included.
7. **Absolute coherent comparator.** The criterion-sensitivity section explicitly defines the unnormalized absolute-regret objective and clarifies that table overlap is with the relative-minimax list.
8. **Nonnegative orthant notation.** The priority vectors are written in `R_{>=0}^n` to avoid convention-dependent interpretation of `R_+^n`.

Fresh screened and unscreened runs reproduce the same selected set and the same substantive numerical results as the archived baseline.
