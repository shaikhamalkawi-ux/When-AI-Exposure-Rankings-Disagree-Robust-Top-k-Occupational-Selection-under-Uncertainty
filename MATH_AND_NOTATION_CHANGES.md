# Mathematical and notation closure

No dataset, 661x18 scenario matrix, selected list, optimization result, table value, or scientific conclusion was changed in this closure.

1. **Breakpoint endpoint semantics.** Reported g* values are transition boundaries. Because best rank uses a strict comparison and worst rank a non-strict comparison, the post-contraction state is applied for g < g* rather than asserted at equality.
2. **Reparameterization symbol.** Retained support width remains g; the optional homeomorphism is phi, with g=phi(alpha), phi(0)=1, and phi(1)=0.
3. **Theorem 1.** The objective is a minimization objective F(m_1,...,m_T) coordinatewise nonincreasing in scenario-wise selected masses. Each dominance exchange strictly increases every scenario-wise selected mass; finiteness of size-k lists excludes cycling.
4. **Exact box regret.** For X={i:x_i=1}, the corner expression is V_k(v(X)) - sum_{i in X} ell_i, avoiding Top-k identity ambiguity under ties.
5. **Relative minimax notation.** V_t*=V_k(p^t), capture C_t(x), relative regret R_t(x)=1-C_t(x), and 0<=rho<=1 are explicit.
6. **Nested support.** ell_i<=c_i<=u_i is stated because the point core is one primitive scenario.
7. **Notation consistency.** Main and Supplement use indicator-sum rank notation and the main uses R_{>=0}^n.
8. **Absolute minimax criterion.** R_t^abs(x)=V_t* - sum_i p_i^t x_i is explicitly defined; the 23/25 overlap is identified relative to the relative-minimax list.
9. **Applied positioning.** The title, abstract, Results First section, stability table, and practical interpretation lead with the 661-occupation / 18-specification application. The Supplement lists all 14 occupations present in every coherent Top-25.
