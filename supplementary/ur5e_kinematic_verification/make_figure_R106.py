#!/usr/bin/env python3
"""Figure 11 of the review (panels a-g), generated from results/*.json (run ur5e_minimal.py and extra_tests.py first)."""
import json, numpy as np
import ur5e_minimal as U
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
fig = plt.figure(figsize=(7.2, 6.5)); gs = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1.02]); a = [fig.add_subplot(gs[i//3, i%3]) for i in range(6)]; ag = fig.add_subplot(gs[2, :])
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
# clearance panel (f): original placement (flat at 20 mm) and adversarial placement (M3, regular line)
EX = json.load(open('results/extra_tests.json'))['A']; adv = [r for r in EX if r['path'] == 'regular'][0]
for path, ls_off in (('regular', 0), ('wrist', 1)):
    for m in ('M1', 'M2', 'M3'):
        rows = [r for r in R if r['path'] == path and r['method'] == m and r['found']]
        a[5].plot([r['N'] for r in rows], [r['clr_curve']*1e3 for r in rows], color='0.55', marker=STY[m]['marker'], mfc='white',
                  ls='none', ms=3.0 + 1.4*ls_off, alpha=0.9)
a[5].plot([r['N'] for r in adv['by_N']], [r['curve']*1e3 for r in adv['by_N']], color='#CC0000', marker='D', ms=3.6, lw=0.9, label='adversarial placement, curve', zorder=4)
a[5].plot([r['N'] for r in adv['by_N']], [r['wp']*1e3 for r in adv['by_N']], color='#CC0000', marker='D', mfc='white', ms=3.6, lw=0.7, ls='--', label='adversarial placement, waypoints', zorder=4)
a[5].axhline(10, color='0.35', lw=0.8, ls=':'); a[5].text(16, 8.6, '$c_{\\min}$ = 10 mm', ha='left', va='top', fontsize=6.2, color='0.2')
a[5].set_xscale('log'); a[5].set_xticks(Ns); a[5].set_xticklabels([str(n) for n in Ns]); a[5].set_ylim(0, 30)
a[5].set_xlabel('Number of waypoints N'); a[5].set_ylabel('Minimum clearance (mm)'); style(a[5], '(f) Clearance versus N')
a[5].text(205, 21.2, 'original placement (gray): 20.0 mm for all\nmethods and lines; does not discriminate', fontsize=5.6, color='0.3', va='bottom', ha='right')
a[5].legend(loc='lower right', frameon=False, fontsize=5.6, handlelength=1.8, borderaxespad=0.2)
# panel (g): clearance profile along the joint-linear curve, adversarial placement
c = np.array(adv['center']); pth = U.build_paths()['regular']; Qref = U.dense_reference(pth)
sref = np.linspace(0, 1, len(Qref)); cref = np.array([U.clearance(q, c) for q in Qref])*1e3
ag.plot(sref, cref, color='0.55', lw=1.4, label='dense reference lift (2001 waypoints)', zorder=1)
cols = {5: '#CC0000', 10: '#E69F00', 20: '#000000'}
for N in (5, 10, 20):
    Ts, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N); Q = U.m3_dls(Ts, pth['q_init'])
    ss, cc = [], []
    for k in range(N-1):
        for j in range(61 if k == N-2 else 60):
            ss.append((k + j/60)/(N-1)); cc.append(U.clearance(Q[k] + (j/60)*(Q[k+1]-Q[k]), c)*1e3)
    ag.plot(ss, cc, color=cols[N], lw=1.0, label=f'joint-linear curve, N = {N}', zorder=3)
    ag.plot(np.linspace(0, 1, N), [U.clearance(q, c)*1e3 for q in Q], ls='none', marker='o', mfc='white', mec=cols[N], ms=4.0, zorder=4)
ag.axhline(10, color='0.35', lw=0.8, ls=':'); ag.text(0.775, 10.5, '$c_{\\min}$ = 10 mm', ha='right', va='bottom', fontsize=6.2, color='0.2')
ag.set_xlabel('Path parameter s'); ag.set_ylabel('Minimum link clearance (mm)'); style(ag, '(g) Clearance along the curve, adversarial obstacle (regular line, M3)')
ag.set_xlim(0.22, 0.78); ag.set_ylim(0, 50)
ag.text(0.5, 2.0, 'circles: waypoints (all clear); N = 5 and N = 10 curves dip below the margin between waypoints', ha='center', fontsize=6.0, color='0.2')
h = [plt.Line2D([], [], **{k: v for k, v in STY[m].items() if k != 'label'}, label=STY[m]['label']) for m in STY]
h.append(plt.Line2D([], [], color='0.55', lw=1.4, label='dense reference lift (b-e)'))
fig.legend(handles=h, loc='lower center', ncol=4, frameon=False, bbox_to_anchor=(0.5, -0.005), handlelength=2.4, columnspacing=1.6)
ag.legend(loc='upper center', ncol=4, frameon=False, fontsize=5.8, handlelength=1.8, columnspacing=1.2)
fig.tight_layout(rect=(0, 0.035, 1, 1), h_pad=1.2, w_pad=0.8)
for ext in ('pdf', 'svg'): fig.savefig(f'results/figure11_R106.{ext}', bbox_inches='tight')
fig.savefig('results/figure11_R106.png', dpi=600, bbox_inches='tight'); print('font:', fam)
