#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'reproducibility' / 'data'
FIG = Path(__file__).resolve().parent / 'figures'
FIG.mkdir(exist_ok=True)

# Figure 1: membership envelopes across evaluated selection sizes.
k = np.array([10, 25, 50, 100])
coh_i = np.array([7, 14, 32, 68])
coh_u = np.array([16, 37, 73, 135])
box_g = np.array([2, 4, 14, 27])
box_p = np.array([43, 87, 159, 244])
plt.figure(figsize=(7.2, 4.6))
plt.plot(k, coh_i, marker='o', label='Coherent intersection')
plt.plot(k, coh_u, marker='o', label='Coherent union')
plt.plot(k, box_g, marker='o', label='Box guaranteed')
plt.plot(k, box_p, marker='o', label='Box possible')
plt.xlabel('Selection size k')
plt.ylabel('Occupations')
plt.legend(ncol=2)
plt.tight_layout()
plt.savefig(FIG/'beyond_membership_frontier.png', dpi=220)
plt.close()

# Load exact priority matrix/core for contraction counts.
M = pd.read_csv(DATA/'BeyondAIR_Primitive_Scenario_Priority_Matrix_661x18.csv', encoding='utf-8-sig')
L = pd.read_csv(DATA/'BeyondAIR_Interval_Core_Ledger_661.csv', encoding='utf-8-sig')
meta = {'SOC','Occupation','Employment','Scale_share'}
scenarios = [c for c in M.columns if c not in meta]
P = M[scenarios].to_numpy(float)
ell = P.min(axis=1)
u = P.max(axis=1)
c = L['core_priority_AIOE_equal5'].to_numpy(float)

def rank_counts(g):
    lo = c - g*(c-ell)
    hi = c + g*(u-c)
    best = 1 + (lo[:,None] > hi[None,:]).sum(axis=0)
    worst = (hi[:,None] >= lo[None,:]).sum(axis=0)
    return int((worst <= 25).sum()), int((best <= 25).sum())

grid = np.linspace(1, 0, 1201)
counts = np.array([rank_counts(g) for g in grid])
contraction = 1-grid
plt.figure(figsize=(7.8, 4.5))
plt.step(contraction, counts[:,0], where='post', label='Guaranteed Top-25')
plt.step(contraction, counts[:,1], where='post', label='Possible Top-25')
plt.axhline(14, linestyle='--', linewidth=1, label='Coherent intersection cardinality = 14')
plt.axhline(37, linestyle=':', linewidth=1, label='Coherent union cardinality = 37')
plt.xlabel('Support contraction 1 - g')
plt.ylabel('Number of occupations')
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(FIG/'beyond_possibilistic_contraction.png', dpi=220)
plt.close()

# Figure 3: coherent regret vs independent-box absolute regret.
perf = pd.read_csv(ROOT/'reproducibility'/'generated'/'fixed_list_performance.csv')
labels = {'Scale only':'Scale only','Baseline composite':'Baseline composite','Relative minimax':'Relative minimax'}
plt.figure(figsize=(5.4, 4.2))
for _, r in perf.iterrows():
    x = r['box_absolute_regret']
    y = r['maximum_relative_regret']
    plt.scatter([x],[y])
    plt.annotate(labels.get(r['rule'], r['rule']), (x,y), xytext=(4,4), textcoords='offset points', fontsize=8)
plt.xlabel('Exact independent-box absolute regret')
plt.ylabel('Maximum coherent relative regret')
plt.tight_layout()
plt.savefig(FIG/'beyond_tradeoff.png', dpi=220)
plt.close()
