#!/usr/bin/env python3
from pathlib import Path
import matplotlib.pyplot as plt

FIG = Path(__file__).resolve().parent / 'figures'
FIG.mkdir(exist_ok=True)

# Locked membership counts reported in the paper.
k = [10, 25, 50, 100]
coh_i = [7, 14, 32, 68]
coh_u = [16, 37, 73, 135]
box_g = [2, 4, 14, 27]
box_p = [43, 87, 159, 244]
plt.figure(figsize=(7.2, 4.6))
plt.plot(k, coh_i, marker='o', label='Coherent intersection')
plt.plot(k, coh_u, marker='o', label='Coherent union')
plt.plot(k, box_g, marker='o', label='Box guaranteed')
plt.plot(k, box_p, marker='o', label='Box possible')
plt.xlabel('Selection size k')
plt.ylabel('Occupations')
plt.legend(ncol=2, fontsize=8)
plt.tight_layout()
plt.savefig(FIG/'membership.png', dpi=220)
plt.close()

# Only the three exact reported transition boundaries are plotted; this is not
# an interpolation of unreported intermediate contraction states.
events = [
    (0.4256799133, 14, 'Guaranteed = 14'),
    (0.5653489777, 37, 'Possible = 37'),
    (0.9212435791, 25, 'Full 25/25 identification'),
]
plt.figure(figsize=(7.2, 4.3))
for x, y, label in events:
    plt.scatter([x], [y], s=45, label=label)
    plt.annotate(f'g*={1-x:.6f}', (x,y), xytext=(5,5), textcoords='offset points', fontsize=8)
plt.xlabel('Support contraction 1 - g')
plt.ylabel('Reported Top-25 structural count')
plt.xlim(0,1)
plt.ylim(0,45)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(FIG/'contraction_events.png', dpi=220)
plt.close()

# Locked fixed-list performance values.
pts = [
    ('Scale only', 0.0238, 0.1165),
    ('Baseline composite', 0.0181, 0.0630),
    ('Relative minimax', 0.0195, 0.0348),
]
plt.figure(figsize=(5.5, 4.2))
for label, x, y in pts:
    plt.scatter([x], [y])
    plt.annotate(label, (x,y), xytext=(5,5), textcoords='offset points', fontsize=8)
plt.xlabel('Exact box absolute regret')
plt.ylabel('Maximum coherent relative regret')
plt.tight_layout()
plt.savefig(FIG/'tradeoff.png', dpi=220)
plt.close()
