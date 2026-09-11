# Mathematical and notation closure

This pass does not change the dataset, the 661x18 scenario matrix, any selected list, optimization result, table value, or scientific conclusion. It closes mathematical wording and presentation points identified in the final review.

1. **Breakpoint endpoint semantics.** Retained-width values are described as transition boundaries. Because best rank uses `>` and pessimistic worst rank uses `>=`, post-contraction membership statements are evaluated immediately below `g*`, avoiding an equality claim at a rounded breakpoint.
2. **Reparameterization symbol.** Structural retained width remains `g`; the optional homeomorphism is now `phi`, with `g = phi(alpha)`, `phi(0)=1`, and `phi(1)=0`.
3. **Theorem 1.** The objective is stated as a minimization objective `F(m_1,...,m_T)` coordinatewise nonincreasing in scenario-wise selected masses. The proof now states that each exchange strictly increases every scenario-wise selected mass and that finiteness of size-k lists excludes cycling.
4. **Exact box regret.** For `X={i:x_i=1}`, the corner expression is written as `V_k(v(X)) - sum_{i in X} ell_i`, avoiding unnecessary Top-k identity notation under ties.
5. **Relative minimax notation.** `V_t^*=V_k(p^t)`, capture `C_t(x)`, relative regret `R_t(x)=1-C_t(x)`, and `0 <= rho <= 1` are explicit.
6. **Nested support.** The text states `ell_i <= c_i <= u_i` because the point core is one primitive scenario.
7. **Notation consistency.** Main and Supplement use indicator-sum rank notation; the main uses `R_{>=0}^n`; `p_i^t=s_i q_i^t` is explicit.
8. **Absolute-minimax criterion.** The criterion sensitivity explicitly defines `R_t^abs(x)=V_t^* - sum_i p_i^t x_i` and minimizes its worst scenario value. Table IV clarifies that overlap is with the relative-minimax list.
9. **Applied positioning.** The title, abstract, first results section, and discussion now lead with the 661-occupation / 18-specification application. A compact stability table is in the main paper, and the Supplement lists all 14 occupations present in every coherent Top-25.
