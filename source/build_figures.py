#!/usr/bin/env python3
from pathlib import Path
import matplotlib.pyplot as plt

FIG = Path(__file__).resolve().parent / 'figures'
FIG.mkdir(exist_ok=True)

plt.rcParams.update({
    'font.size': 10,
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
    'axes.linewidth': 1.25,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'xtick.major.size': 4,
    'ytick.major.size': 4,
    'legend.frameon': True,
})

def box_axes(ax):
    for side in ('left','right','top','bottom'):
        ax.spines[side].set_visible(True)
        ax.spines[side].set_linewidth(1.25)
    ax.tick_params(axis='both', width=1.2, labelsize=9)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontweight('bold')

# Figure 1: membership envelopes across evaluated selection sizes.
k = [10, 25, 50, 100]
coh_i = [7, 14, 32, 68]
coh_u = [16, 37, 73, 135]
box_g = [2, 4, 14, 27]
box_p = [43, 87, 159, 244]
fig, ax = plt.subplots(figsize=(7.3, 4.7))
ax.plot(k, coh_i, marker='o', linewidth=1.8, label='Coherent intersection')
ax.plot(k, coh_u, marker='o', linewidth=1.8, label='Coherent union')
ax.plot(k, box_g, marker='o', linewidth=1.8, label='Box guaranteed')
ax.plot(k, box_p, marker='o', linewidth=1.8, label='Box possible')
ax.set_xlabel('Selection size k', fontweight='bold')
ax.set_ylabel('Occupations', fontweight='bold')
ax.set_xlim(7, 103)
ax.set_ylim(0, 260)
ax.set_title('Membership envelopes across selection sizes', fontweight='bold')
box_axes(ax)
leg = ax.legend(loc='upper left', ncol=2, prop={'weight':'bold','size':8}, borderaxespad=0.7)
leg.get_frame().set_linewidth(1.0)
fig.tight_layout(pad=0.8)
fig.savefig(FIG/'membership.png', dpi=260, bbox_inches='tight')
plt.close(fig)

# Figure 2: exact reported transition boundaries only.
events = [
    (0.4256799133, 14, 'g*=0.574320', (8, 8), 'left'),
    (0.5653489777, 37, 'g*=0.434651', (8, -15), 'left'),
    (0.9212435791, 25, 'g*=0.078756', (-8, 8), 'right'),
]
fig, ax = plt.subplots(figsize=(7.2, 4.4))
for x, y, label, offset, ha in events:
    ax.scatter([x], [y], s=48, zorder=3)
    ax.annotate(label, (x, y), xytext=offset, textcoords='offset points',
                fontsize=9, fontweight='bold', ha=ha, va='center', clip_on=True)
ax.set_xlabel('Support contraction 1 - g', fontweight='bold')
ax.set_ylabel('Reported Top-25 structural count', fontweight='bold')
ax.set_xlim(0.35, 0.98)
ax.set_ylim(8, 43)
ax.set_title('Exact Top-25 contraction boundaries', fontweight='bold')
box_axes(ax)
fig.tight_layout(pad=0.8)
fig.savefig(FIG/'contraction_events.png', dpi=260, bbox_inches='tight')
plt.close(fig)

# Figure 3: coherent relative regret vs independent-box absolute regret.
pts = [
    ('Scale only', 0.0238, 0.1165, (-10, -14), 'right'),
    ('Baseline composite', 0.0181, 0.0630, (7, 8), 'left'),
    ('Relative minimax', 0.0195, 0.0348, (7, 8), 'left'),
]
fig, ax = plt.subplots(figsize=(5.7, 4.35))
for label, x, y, offset, ha in pts:
    ax.scatter([x], [y], s=52, zorder=3)
    ax.annotate(label, (x, y), xytext=offset, textcoords='offset points',
                fontsize=9, fontweight='bold', ha=ha, va='center', clip_on=True)
ax.set_xlabel('Exact box absolute regret', fontweight='bold')
ax.set_ylabel('Maximum coherent relative regret', fontweight='bold')
ax.set_xlim(0.0168, 0.0252)
ax.set_ylim(0.025, 0.128)
ax.set_title('Robustness trade-off at k=25', fontweight='bold')
box_axes(ax)
fig.tight_layout(pad=0.8)
fig.savefig(FIG/'tradeoff.png', dpi=260, bbox_inches='tight')
plt.close(fig)
