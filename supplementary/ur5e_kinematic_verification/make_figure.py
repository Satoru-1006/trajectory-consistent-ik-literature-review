#!/usr/bin/env python3
"""Figure 2 of the review, generated from results/*.json (run ur5e_minimal.py first)."""
import json, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

avail = {f.name for f in fm.fontManager.ttflist}
for fam in ('Arial', 'Helvetica', 'Liberation Sans', 'DejaVu Sans'):
    if fam in avail: break
plt.rcParams.update({'font.family': fam, 'font.size': 7, 'axes.labelsize': 7, 'axes.titlesize': 7.5, 'legend.fontsize': 6.3,
                     'xtick.labelsize': 6.5, 'ytick.labelsize': 6.5, 'axes.linewidth': 0.6, 'xtick.major.width': 0.6, 'ytick.major.width': 0.6,
                     'xtick.major.size': 2.5, 'ytick.major.size': 2.5, 'lines.linewidth': 0.9, 'lines.markersize': 3.4,
                     'pdf.fonttype': 42, 'svg.fonttype': 'none', 'axes.grid': True, 'grid.linewidth': 0.3, 'grid.alpha': 0.5})
R = json.load(open('results/results.json'))['results']; W = json.load(open('results/wrist_curves.json'))
STY = {'M1': dict(color='#D55E00', ls='--', marker='o', mfc='white', label='M1 nearest solution'),
       'M2': dict(color='#0072B2', ls='-.', marker='s', mfc='white', label='M2 graph search'),
       'M3': dict(color='#000000', ls='-', marker='^', mfc='#000000', label='M3 differential IK')}
def series(path, key, scale=1.0):
    out = {}
    for m in ('M1', 'M2', 'M3'):
        rows = [r for r in R if r['path'] == path and r['method'] == m]
        out[m] = ([r['N'] for r in rows if r['found']], [r[key]*scale for r in rows if r['found']])
    return out
def style(ax, title):
    ax.set_title(title, loc='left', fontweight='bold', pad=3)
    ax.tick_params(which='both', direction='out')
fig, axs = plt.subplots(2, 3, figsize=(7.2, 4.5)); a = axs.ravel()
Ns = [5, 10, 20, 50, 100, 200]
def curve_panel(ax, path, key, scale, tol, tolabel, ylab, floor=None):
    for m, (x, y) in series(path, key, scale).items():
        y = np.maximum(y, floor) if floor else y
        ax.plot(x, y, **STY[m], zorder=3 if m == 'M3' else 2, markevery=1)
    ax.axhline(tol, color='0.35', lw=0.8, ls=':'); ax.text(205, tol*1.25, tolabel, ha='right', va='bottom', fontsize=6.2, color='0.2')
    ax.set_xscale('log'); ax.set_yscale('log'); ax.set_xticks(Ns); ax.set_xticklabels([str(n) for n in Ns])
    ax.set_xlabel('Number of waypoints N'); ax.set_ylabel(ylab)
curve_panel(a[0], 'regular', 'curve_pos_dev', 1e3, 1.0, 'tolerance 1 mm', 'Position deviation of reconstructed curve (mm)')
style(a[0], '(a) Regular line')
a[0].set_ylim(1e-4, 3e1)
curve_panel(a[1], 'wrist', 'curve_pos_dev', 1e3, 1.0, 'tolerance 1 mm', 'Position deviation of reconstructed curve (mm)')
style(a[1], '(b) Wrist-crossing line')
a[1].set_ylim(1e-4, 3e1)
a[1].text(5.6, 10.0, 'M2: no admissible path at N = 5', fontsize=6.2, color=STY['M2']['color'], va='bottom')
curve_panel(a[2], 'wrist', 'curve_rot_dev', 1.0, 1e-3, 'tolerance 10$^{-3}$ rad', 'Orientation deviation of reconstructed curve (rad)', floor=1e-9)
style(a[2], '(c) Wrist-crossing line'); a[2].set_ylim(1e-9, 1e-1)
a[2].text(5.3, 2e-9, 'values below 10$^{-8}$ rad are numerical noise', fontsize=5.8, color='0.3')
# joint panels
s = np.linspace(0, 1, 2001); ref = np.array(W['ref_q'])
for ax, j, lab, title in ((a[3], 3, 'Joint $q_4$ (rad)', '(d) Wrist-crossing line, N = 5'), (a[4], 5, 'Joint $q_6$ (rad)', '(e) Wrist-crossing line, N = 5')):
    ax.plot(s, ref[:, j], color='0.55', lw=1.4, label='dense reference lift (2001 waypoints)', zorder=1)
    for m in ('M1', 'M3'):
        Q = np.array(W[m]); ax.plot(np.linspace(0, 1, len(Q)), Q[:, j], **STY[m], zorder=3)
    style(ax, title); ax.set_xlabel('Path parameter s'); ax.set_ylabel(lab)
a[3].set_ylim(-0.66, 0.32); a[4].set_ylim(-0.66, 0.32)
a[3].text(0.03, 0.93, 'M2: no admissible path', transform=a[3].transAxes, fontsize=6.2, color=STY['M2']['color'], va='top')
a[4].text(0.03, 0.93, 'M2: no admissible path', transform=a[4].transAxes, fontsize=6.2, color=STY['M2']['color'], va='top')
# clearance panel
for path, ls_off, lab in (('regular', 0, 'regular line'), ('wrist', 1, 'wrist-crossing line')):
    for m in ('M1', 'M2', 'M3'):
        rows = [r for r in R if r['path'] == path and r['method'] == m and r['found']]
        a[5].plot([r['N'] for r in rows], [r['clr_curve']*1e3 for r in rows], color=STY[m]['color'], marker=STY[m]['marker'], mfc=STY[m]['mfc'],
                  ls='none', ms=3.4 + 1.6*ls_off, alpha=0.9)
a[5].axhline(10, color='0.35', lw=0.8, ls=':'); a[5].text(205, 10.4, '$c_{\\min}$ = 10 mm', ha='right', va='bottom', fontsize=6.2, color='0.2')
a[5].set_xscale('log'); a[5].set_xticks(Ns); a[5].set_xticklabels([str(n) for n in Ns]); a[5].set_ylim(0, 25)
a[5].set_xlabel('Number of waypoints N'); a[5].set_ylabel('Minimum clearance on curve (mm)'); style(a[5], '(f) Clearance, both lines')
a[5].text(6, 1.5, 'all points at 20.0 mm: closest\napproach is at an end waypoint', fontsize=6, color='0.2')
h = [plt.Line2D([], [], **{k: v for k, v in STY[m].items() if k != 'label'}, label=STY[m]['label']) for m in STY]
h.append(plt.Line2D([], [], color='0.55', lw=1.4, label='dense reference lift'))
fig.legend(handles=h, loc='lower center', ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.005), handlelength=2.4, columnspacing=1.6)
fig.tight_layout(rect=(0, 0.045, 1, 1), h_pad=1.2, w_pad=0.8)
for ext in ('pdf', 'svg'): fig.savefig(f'results/figure2.{ext}', bbox_inches='tight')
fig.savefig('results/figure2.png', dpi=600, bbox_inches='tight'); print('font:', fam)
