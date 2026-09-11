from pathlib import Path

def rep(s,a,b):
    return s.replace(a,b)

p=Path('source/main.tex')
s=p.read_text()
s=rep(s,'least sensitive to admitted measurement design.','least sensitive to the admitted measurement-design family.')
s=rep(s,'0.0195 versus 0.0181','0.01945 versus 0.01810')
s=rep(s,'\\caption{Membership envelopes across evaluated selection sizes. All plot text is bold and all four spines are shown to keep the comparison visually bounded. Coherent specifications move occupational scores together; the independent box permits coordinatewise adversarial movement.}', '\\caption{Membership envelopes across evaluated selection sizes. Coherent specifications move occupational scores together, whereas the independent box permits coordinatewise adversarial movement.}')
s=rep(s,'\\caption{Three reported exact Top-25 contraction boundaries. All annotations are bold and kept inside the four-sided plotting frame. The post-contraction state is interpreted according to the tie convention in the text.}', '\\caption{Three reported exact Top-25 contraction boundaries. Points mark structural transition values; post-contraction membership follows the stated tie convention.}')
s=rep(s,'\\caption{Robustness trade-off at $k=25$. Labels, tick values, and axes are bold and fully contained within a four-sided frame. Lower is better on both axes; baseline and relative-minimax lists are non-dominating across uncertainty structures.}', '\\caption{Robustness trade-off at $k=25$. Lower values are preferred on both axes; the baseline and relative-minimax lists are non-dominating across the two uncertainty structures.}')
s=rep(s,'$a_i^{(c)}\\in[0,1]$ be the frozen normalized exposure value for channel $c$', '$a_i^{(r)}\\in[0,1]$ be the frozen normalized exposure value for channel $r$')
s=rep(s,'q_i^{(c,w)}=a_i^{(c)}','q_i^{(r,w)}=a_i^{(r)}')
s=rep(s,'p_i^t=s_iq_i^{(c,w)}','p_i^t=s_iq_i^{(r,w)}')
s=rep(s,'with $t=(c,w)$.','with $t=(r,w)$.')
needle='with $t=(r,w)$. The paper treats the normalized exposure and skill inputs as frozen primitive inputs to the decision layer; it does not re-estimate their upstream measurement models.'
repl='with $t=(r,w)$. The factor $1-h_i^{(w)}$ is a declared screening transformation: a larger retained-skill aggregate lowers the modifier within this construction, but it is not causal evidence that skills protect a worker from AI exposure or displacement. The paper treats the normalized exposure and skill inputs as frozen primitive inputs to the decision layer; it does not re-estimate their upstream measurement models.'
s=rep(s,needle,repl)
if 'Here $\\ind\\{\\cdot\\}$ denotes the indicator function.' not in s:
    s=rep(s,'\\end{align}\nThe endpoint realizations are feasible','\\end{align}\nHere $\\ind\\{\\cdot\\}$ denotes the indicator function. The endpoint realizations are feasible',1)
s=rep(s,'The fixed-list decision is a finite robust/minmax-regret problem over declared coherent scenarios','The fixed-list decision is a finite minimax-regret selection problem over the declared coherent scenarios')
s=rep(s,'and define $V_t^\\star=V_k(p^t)$. For binary selection','and define $V_t^\\star=V_k(p^t)$. For all admitted scenarios, $V_t^\\star>0$. For binary selection')
s=rep(s,'objective $F(m_1,\\ldots,m_T)$ that is coordinatewise nonincreasing in scenario-wise selected masses $m_t=\\sum_i p_i^t x_i$','objective $F(M_1(x),\\ldots,M_T(x))$ that is coordinatewise nonincreasing in scenario-wise selected masses $M_t(x)=\\sum_i p_i^t x_i$')
s=rep(s,"If the next $g\\in G$ is absent from a size-$k$ optimum, then at most $k-1$ competitors satisfy $u_j\\ge\\ell_g$, so the list contains some $h$ with $u_h<\\ell_g$. Any guaranteed item $g'$ inserted earlier satisfies $\\ell_{g'}\\ge\\ell_g$ and therefore $u_{g'}\\ge\\ell_{g'}\\ge\\ell_g$, so it cannot be this $h$. Replacing $h$ by $g$ thus preserves all earlier insertions", "If the next $a\\in G$ is absent from a size-$k$ optimum, then at most $k-1$ competitors satisfy $u_j\\ge\\ell_a$, so the list contains some $h$ with $u_h<\\ell_a$. Any guaranteed item $a'$ inserted earlier satisfies $\\ell_{a'}\\ge\\ell_a$ and therefore $u_{a'}\\ge\\ell_{a'}\\ge\\ell_a$, so it cannot be this $h$. Replacing $h$ by $a$ thus preserves all earlier insertions")
s=rep(s,'At $k=25$ the screen fixes 4 occupations in and 574 impossible occupations out without changing the coherent optimum.','At $k=25$ the screening rule fixes 4 occupations as included and excludes 574 occupations as impossible members without changing the coherent optimum.')
s=rep(s,'Here possibility theory is only optional coordinate language; the data identify support and a point core, not a calibrated possibility distribution.','Possibility theory is used only as optional parameterization language; the data identify support and a point core, not a calibrated possibility distribution.')
if 'We denote each reported structural transition boundary by $g^\\star$.' not in s:
    s=rep(s,'Rank vectors are piecewise constant.','Rank vectors are piecewise constant. We denote each reported structural transition boundary by $g^\\star$.')
if 'Consensus frequency & 97.00\\%' not in s:
    old='''\\section{Application Results}\nTable~\\ref{tab:performance} compares three fixed lists. The relative-minimax list improves the minimum coherent-scenario capture to 96.52\\%, from 93.70\\% for the baseline composite and 88.35\\% for scale only. Its exact box absolute regret is 0.0195, slightly larger than the baseline's 0.0181, so no list is unconditionally ``most robust'' without naming the uncertainty structure and criterion.\n\n\\begin{table}[t]\n\\caption{Fixed-list performance at $k=25$ over 18 primitive scenarios.}\n\\label{tab:performance}\n\\centering\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrr}\n\\toprule\nRule & Mean cap. & Min. cap. & Max rel. regret & Box abs. regret\\\\\n\\midrule\nScale only & 93.02\\% & 88.35\\% & 11.65\\% & .0238\\\\\nBaseline composite & 96.14\\% & 93.70\\% & 6.30\\% & .0181\\\\\nRelative minimax & 96.99\\% & 96.52\\% & 3.48\\% & .0195\\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nCriterion normalization also matters.'''
    new='''\\section{Application Results}\nTable~\\ref{tab:performance} compares the three primary fixed-list rules and one transparent consensus benchmark. The relative-minimax list improves the minimum coherent-scenario capture to 96.52\\%, from 93.70\\% for the baseline composite and 88.35\\% for scale only. Its exact box absolute regret is 0.01945, slightly larger than the baseline's 0.01810, so no list is unconditionally ``most robust'' without naming the uncertainty structure and criterion.\n\nAs a descriptive rank-aggregation benchmark, let $T_t=\\operatorname{Top}_{25}(p^t)$ and define\n\\begin{equation}\nf_i=\\sum_{t=1}^{18}\\ind\\{i\\in T_t\\}.\n\\label{eq:consensus}\n\\end{equation}\nThe Consensus-Frequency list contains the 25 occupations with the largest $f_i$; because the 18 scenarios are declared designs rather than probability-weighted draws, $f_i$ is an occurrence count, not a selection probability. This simple benchmark is included only as a sanity check against broader rank/list-aggregation ideas \\cite{dwork2001,fagin2003}.\n\n\\begin{table}[t]\n\\caption{Fixed-list performance at $k=25$ over 18 primitive scenarios.}\n\\label{tab:performance}\n\\centering\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrr}\n\\toprule\nRule & Mean cap. & Min. cap. & Max rel. regret & Box abs. regret\\\\\n\\midrule\nScale only & 93.02\\% & 88.35\\% & 11.65\\% & .02380\\\\\nBaseline composite & 96.14\\% & 93.70\\% & 6.30\\% & .01810\\\\\nConsensus frequency & 97.00\\% & 95.89\\% & 4.11\\% & .01952\\\\\nRelative minimax & 96.99\\% & 96.52\\% & 3.48\\% & .01945\\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe Consensus-Frequency list overlaps the relative-minimax solution in 24 of 25 occupations and has a marginally higher mean capture (97.00\\% versus 96.99\\%), but its minimum capture is lower (95.89\\% versus 96.52\\%), corresponding to a larger maximum relative regret (4.11\\% versus 3.48\\%). Thus frequency aggregation closely reproduces the central list, while relative minimax provides stronger protection on the worst-case relative-capture criterion it explicitly optimizes; this is not a claim of universal dominance. Detailed scenario-by-scenario performance, the full 25-member list, and the one-item disagreement are retained in the reproducibility addendum; the one-item disagreement is also stated in the Supplement.\n\nCriterion normalization also matters.'''
    if old not in s:
        raise SystemExit('Main Application Results block not found')
    s=s.replace(old,new)
s=rep(s,'and solve $\\min_{x:\\sum_i x_i=k}\\max_t R_t^{\\mathrm{abs}}(x)$.','and solve $\\min_{x:\\,\\sum_i x_i=k,\\ x_i\\in\\{0,1\\}}\\max_t R_t^{\\mathrm{abs}}(x)$.')
if 'The 24/25 overlap with the simple Consensus-Frequency benchmark' not in s:
    s=rep(s,'For analysts or institutions that require one fixed screening list, the relative-minimax solution is a defensible compromise because it maximizes the worst retained share of scenario-optimal priority mass across the declared designs.','For analysts or institutions that require one fixed screening list, the relative-minimax solution is a defensible compromise because it maximizes the worst retained share of scenario-optimal priority mass across the declared designs. The 24/25 overlap with the simple Consensus-Frequency benchmark shows that this solution is not driven by an idiosyncratic list, while the lower worst-case regret identifies the specific protection gained from minimax optimization.')
s=rep(s,'Relative minimax raises worst-scenario capture from 93.70\\% to 96.52\\% compared with the baseline composite, without claiming universal robustness.','Relative minimax raises worst-scenario capture from 93.70\\% to 96.52\\% compared with the baseline composite and retains 24/25 occupations from the Consensus-Frequency benchmark, without claiming universal robustness.')
s=rep(s,'\\begin{thebibliography}{28}','\\begin{thebibliography}{30}')
s=rep(s,'\\begin{thebibliography}{31}','\\begin{thebibliography}{30}')
s=rep(s,'\\bibitem{oecd2008} OECD and Joint Research Centre, \\emph{Handbook on Constructing Composite Indicators: Methodology and User Guide}. OECD Publishing, 2008.','\\bibitem{oecd2008} OECD and Joint Research Centre, \\emph{Handbook on Constructing Composite Indicators: Methodology and User Guide}. OECD Publishing, 2008, doi: 10.1787/9789264043466-en.')
s=rep(s,'\\bibitem{ide2016} J. Ide and A. Sch\\"obel, ``Robustness for uncertain multi-objective optimization,'' \\emph{OR Spectrum}, vol. 38, pp. 235--271, 2016.','\\bibitem{ide2016} J. Ide and A. Sch\\"obel, ``Robustness for uncertain multi-objective optimization: a survey and analysis of different concepts,'' \\emph{OR Spectrum}, vol. 38, pp. 235--271, 2016, doi: 10.1007/s00291-015-0418-7.')
s=rep(s,'\\bibitem{conde2004} E. Conde, ``An improved algorithm for selecting $p$ items with uncertain returns,'' \\emph{Mathematical Programming}, vol. 100, no. 2, pp. 345--353, 2004.','\\bibitem{conde2004} E. Conde, ``An improved algorithm for selecting $p$ items with uncertain returns according to the minmax-regret criterion,'' \\emph{Mathematical Programming}, vol. 100, no. 2, pp. 345--353, 2004, doi: 10.1007/s10107-003-0474-7.')
s=s.replace('\\bibitem{lin2010} S. Lin, ``Rank aggregation methods,'' \\emph{WIREs Computational Statistics}, vol. 2, no. 5, pp. 555--570, 2010, doi: 10.1002/wics.111.\n','')
if '\\bibitem{dwork2001}' not in s:
    needle='\\bibitem{dubois2016} D. Dubois and H. Prade, ``Practical methods for constructing possibility distributions,'' \\emph{International Journal of Intelligent Systems}, vol. 31, no. 3, pp. 215--239, 2016, doi: 10.1002/int.21782.\n'
    add=needle+'\\bibitem{dwork2001} C. Dwork, R. Kumar, M. Naor, and D. Sivakumar, ``Rank aggregation methods for the Web,'' in \\emph{Proc. 10th Int. World Wide Web Conf. (WWW)}, 2001, pp. 613--622, doi: 10.1145/371920.372165.\n\\bibitem{fagin2003} R. Fagin, R. Kumar, and D. Sivakumar, ``Comparing top $k$ lists,'' \\emph{SIAM Journal on Discrete Mathematics}, vol. 17, no. 1, pp. 134--160, 2003, doi: 10.1137/S0895480102412856.\n'
    s=s.replace(needle,add)
p.write_text(s)

p=Path('source/supplement.tex')
s=p.read_text()
s=rep(s,'$a_i^{(c)}\\in[0,1]$ denote frozen normalized exposure for channel $c$', '$a_i^{(r)}\\in[0,1]$ denote frozen normalized exposure for channel $r$')
s=rep(s,'q_i^{(c,w)}=a_i^{(c)}','q_i^{(r,w)}=a_i^{(r)}')
s=rep(s,'p_i^t=s_iq_i^{(c,w)}','p_i^t=s_iq_i^{(r,w)}')
if 'The factor $1-h_i^{(w)}$ is a declared screening transformation' not in s:
    s=rep(s,'The equal-five construction uses all five skills;','The factor $1-h_i^{(w)}$ is a declared screening transformation: a larger retained-skill aggregate lowers the modifier within this construction, but this does not establish a causal protective effect of skills. The equal-five construction uses all five skills;')
if 'Here $\\ind\\{\\cdot\\}$ denotes the indicator function.' not in s:
    s=rep(s,'Possible membership is $r_i^{\\min}\\le k$ and guaranteed membership is $r_i^{\\max}\\le k$.','Here $\\ind\\{\\cdot\\}$ denotes the indicator function. Possible membership is $r_i^{\\min}\\le k$ and guaranteed membership is $r_i^{\\max}\\le k$.')
s=rep(s,"If the next $g\\in G$ is absent from a size-$k$ optimum, at most $k-1$ competitors satisfy $u_j\\ge\\ell_g$, so the list contains an $h$ with $u_h<\\ell_g$. Any guaranteed item $g'$ inserted earlier has $\\ell_{g'}\\ge\\ell_g$ and hence $u_{g'}\\ge\\ell_{g'}\\ge\\ell_g$, so it cannot be chosen as $h$. Replacing $h$ by $g$", "If the next $a\\in G$ is absent from a size-$k$ optimum, at most $k-1$ competitors satisfy $u_j\\ge\\ell_a$, so the list contains an $h$ with $u_h<\\ell_a$. Any guaranteed item $a'$ inserted earlier has $\\ell_{a'}\\ge\\ell_a$ and hence $u_{a'}\\ge\\ell_{a'}\\ge\\ell_a$, so it cannot be chosen as $h$. Replacing $h$ by $a$")
if 'Consensus frequency&97.00' not in s:
    start=s.index('\\section*{S5. Fixed-list verification and criterion sensitivity}')
    end=s.index('\\section*{S6. Nested-support sensitivity and exact boundary semantics}')
    new=r'''\section*{S5. Fixed-list verification, consensus benchmark, and criterion sensitivity}
\begin{table}[h]\centering\small
\caption{Fixed-list comparison at $k=25$ over 18 primitive scenarios.}
\begin{tabular}{lrrrr}\toprule Rule&Mean capture&Minimum capture&Max. rel. regret&Box regret\\\midrule
Scale only&93.02\%&88.35\%&11.65\%&0.02380\\
Baseline composite&96.14\%&93.70\%&6.30\%&0.01810\\
Consensus frequency&97.00\%&95.89\%&4.11\%&0.01952\\
Relative minimax&96.99\%&96.52\%&3.48\%&0.01945\\\bottomrule\end{tabular}
\end{table}
For the consensus-frequency benchmark, $f_i=\sum_{t=1}^{18}\ind\{i\in T_t\}$ counts appearances in scenario-specific Top-25 lists; the 25 largest counts are selected, with ascending SOC only as a deterministic tie-break. The cutoff is strict (9 versus 8 appearances), so the tie rule does not affect membership. The list overlaps relative minimax in 24/25 occupations: consensus includes Hosts and Hostesses, Restaurant, Lounge, and Coffee Shop (35-9031), whereas minimax includes Amusement and Recreation Attendants (39-3091). Exact scenario-by-scenario capture/regret and the complete 25-member list are retained in the reproducibility addendum. Counts are design occurrences, not probabilities.

The relative-minimax objective is $\max_t R_t(x)$ with $R_t(x)=1-\sum_i p_i^t x_i/V_t^\star$ and $V_t^\star>0$ for every admitted scenario. The absolute-minimax sensitivity instead defines
\[R_t^{\mathrm{abs}}(x)=V_t^\star-\sum_i p_i^t x_i,\qquad \min_{x:\,\sum_i x_i=k,\ x_i\in\{0,1\}}\max_tR_t^{\mathrm{abs}}(x).\]
Its list overlaps the relative-minimax list in 23/25 occupations, with minimum relative capture 94.79\% and maximum relative regret 5.21\%.

'''
    s=s[:start]+new+s[end:]
else:
    s=rep(s,'The relative-minimax objective is $\\max_t R_t(x)$ with $R_t(x)=1-\\sum_i p_i^t x_i/V_t^\\star$.','The relative-minimax objective is $\\max_t R_t(x)$ with $R_t(x)=1-\\sum_i p_i^t x_i/V_t^\\star$ and $V_t^\\star>0$ for every admitted scenario.')
    s=rep(s,'\\min_{x:\\sum_i x_i=k}\\max_tR_t^{\\mathrm{abs}}(x)','\\min_{x:\\,\\sum_i x_i=k,\\ x_i\\in\\{0,1\\}}\\max_tR_t^{\\mathrm{abs}}(x)')
if 'We denote each reported structural transition boundary by $g^\\star$.' not in s:
    s=rep(s,'These values are transition boundaries.','We denote each reported structural transition boundary by $g^\\star$. These values are transition boundaries.')
if 'Consensus-frequency list&Occurrence-based aggregation' not in s:
    s=rep(s,'Relative-minimax list&Best worst relative capture over declared scenarios&Optimal workforce policy\\\\\nBox regret','Relative-minimax list&Best worst relative capture over declared scenarios&Optimal workforce policy\\\\\nConsensus-frequency list&Occurrence-based aggregation over 18 admitted Top-25 lists&Probability of selection or worst-case optimum\\\\\nBox regret')
p.write_text(s)
