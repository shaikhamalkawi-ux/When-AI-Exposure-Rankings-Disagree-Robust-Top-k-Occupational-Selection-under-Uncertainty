from pathlib import Path


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f"missing pattern: {label}")
    return text.replace(old, new, 1)

# Main manuscript closure.
p = Path('source/main.tex')
s = p.read_text()
s = replace_once(
    s,
    'Here possibility theory is only optional coordinate language: the empirical object is a finite priority support plus a declared point core, not a calibrated possibility distribution.',
    'Possibility theory is used only as optional parameterization language: the empirical object is a finite priority support plus a declared point core, not a calibrated possibility distribution.',
    'possibility wording',
)
s = replace_once(
    s,
    'As a descriptive rank-aggregation benchmark, let $T_t=\\operatorname{Top}_{25}(p^t)$ and define',
    'As a descriptive rank-aggregation benchmark, let $T_t=\\operatorname{Top}_{25}(p^t)$ denote the set of the 25 occupations with the largest priorities under scenario $t$, and define',
    'Top25 definition',
)
s = replace_once(
    s,
    'The Consensus-Frequency list contains the 25 occupations with the largest $f_i$; because the 18 scenarios are declared designs rather than probability-weighted draws, $f_i$ is an occurrence count, not a selection probability. This simple benchmark is included only as a sanity check against broader rank/list-aggregation ideas \\cite{dwork2001,fagin2003}.',
    'The Consensus-Frequency list contains the 25 occupations with the largest $f_i$. The 25th-ranked count is 9 and the 26th-ranked count is 8, so no frequency tie occurs at the membership cutoff; ascending SOC is retained only as a fixed deterministic tie-break for equal counts away from the cutoff. Because the 18 scenarios are declared designs rather than probability-weighted draws, $f_i$ is an occurrence count, not a selection probability. This simple benchmark is included only as a sanity check against broader rank/list-aggregation ideas \\cite{dwork2001,fagin2003}.',
    'consensus tie rule',
)
s = s.replace('Consensus frequency & 97.00\\% & 95.89\\% & 4.11\\% & .01952\\\\', 'Consensus-Frequency & 97.00\\% & 95.89\\% & 4.11\\% & .01952\\\\')
s = replace_once(
    s,
    'The 24/25 overlap with the simple Consensus-Frequency benchmark shows that this solution is not driven by an idiosyncratic list, while the lower worst-case regret identifies the specific protection gained from minimax optimization.',
    'The 24/25 overlap with the simple Consensus-Frequency benchmark indicates close agreement between the two lists, while the lower worst-case regret identifies the specific protection provided by the minimax criterion.',
    'practical interpretation wording',
)
s = replace_once(
    s,
    '\\caption{Robustness trade-off at $k=25$. Lower values are preferred on both axes; the baseline and relative-minimax lists are non-dominating across the two uncertainty structures.}',
    '\\caption{Robustness trade-off at $k=25$. Lower values are preferred on both axes. Consensus-Frequency lies close to relative minimax but has higher coherent worst-case regret; the baseline composite retains the smallest independent-box regret.}',
    'Figure 3 caption',
)
p.write_text(s)

# Supplement closure.
p = Path('source/supplement.tex')
s = p.read_text()
s = s.replace('\\usepackage[margin=0.7in]{geometry}', '\\usepackage[margin=0.58in]{geometry}')
s = s.replace('\\begin{document}\\maketitle', '\\begin{document}\\maketitle\\small')
s = s.replace('Consensus frequency&97.00\\%&95.89\\%&4.11\\%&0.01952\\\\', 'Consensus-Frequency&97.00\\%&95.89\\%&4.11\\%&0.01952\\\\')
s = replace_once(
    s,
    'For the consensus-frequency benchmark, $f_i=\\sum_{t=1}^{18}\\mathbf{1}\\{i\\in T_t\\}$ counts appearances in scenario-specific Top-25 lists; the 25 largest counts are selected, with ascending SOC only as a tie-break. The cutoff is strict (9 versus 8 appearances), so the tie rule does not affect membership. The list overlaps relative minimax in 24/25 occupations: consensus includes Hosts and Hostesses (35-9031), whereas minimax includes Amusement and Recreation Attendants (39-3091). Table~3 reports the direct recomputation; exact outputs are retained in the reproducibility addendum. Counts are design occurrences, not probabilities.',
    'For the Consensus-Frequency benchmark, let $T_t=\\operatorname{Top}_{25}(p^t)$ denote the 25 occupations with the largest priorities under scenario $t$. Then $f_i=\\sum_{t=1}^{18}\\mathbf{1}\\{i\\in T_t\\}$ counts appearances across the 18 scenario-specific Top-25 lists. The 25 largest counts are selected; the cutoff is strict (9 appearances for the 25th occupation versus 8 for the 26th), so no frequency tie occurs at the membership cutoff. Ascending SOC is retained only as a fixed deterministic tie-break for equal counts away from the cutoff. The list overlaps relative minimax in 24/25 occupations: consensus includes Hosts and Hostesses (35-9031), whereas minimax includes Amusement and Recreation Attendants (39-3091). Table~3 reports the direct recomputation; exact outputs are retained in the reproducibility addendum. Counts are design occurrences, not probabilities.\n\n\\noindent\\textbf{Consensus-Frequency Top-25 SOC membership.} 11-1021, 13-2011, 29-1141, 35-3031, 37-2011, 41-2011, 41-2031, 41-4012, 43-3031, 43-4171, 43-6014, 43-9061, 53-3032, 53-7065, 13-1111, 43-1011, 13-1071, 15-1232, 33-9032, 35-2014, 35-9031, 41-1011, 43-5071, 43-6013, and 49-9071. The complete labeled list is supplied in \\texttt{consensus\\_frequency\\_selection.csv}. The relative-minimax list contains the same 24 shared occupations, replacing Hosts and Hostesses, Restaurant, Lounge, and Coffee Shop (35-9031) with Amusement and Recreation Attendants (39-3091).',
    'supplement consensus closure',
)
s = s.replace('Consensus-frequency list&Occurrence-based aggregation over the 18 admitted Top-25 lists&Probability of selection or worst-case optimum\\\\', 'Consensus-Frequency list&Occurrence-based aggregation over the 18 admitted Top-25 lists&Probability of selection or worst-case optimum\\\\')
p.write_text(s)

# Figure 3 gets the consensus point.
p = Path('source/build_figures.py')
s = p.read_text()
old = """pts = [\n    ('Scale only', 0.0238, 0.1165, (-10, -14), 'right'),\n    ('Baseline composite', 0.0181, 0.0630, (7, 8), 'left'),\n    ('Relative minimax', 0.0195, 0.0348, (7, 8), 'left'),\n]\n"""
new = """pts = [\n    ('Scale only', 0.02380, 0.1165, (-10, -14), 'right'),\n    ('Baseline composite', 0.01810, 0.0630, (7, 8), 'left'),\n    ('Consensus-Frequency', 0.01952, 0.0411, (8, 11), 'left'),\n    ('Relative minimax', 0.01945, 0.0348, (-8, -12), 'right'),\n]\n"""
s = replace_once(s, old, new, 'Figure 3 points')
p.write_text(s)
