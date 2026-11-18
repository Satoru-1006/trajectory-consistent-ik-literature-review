#!/usr/bin/env python3
"""Figure 11 of the review (R110): UR5e set-up of the kinematic experiment in 3-D. Uses the same kinematics, paths, dense reference lifts
and obstacle placements as ur5e_minimal.py (results/results.json 'setup'); no number is typed in by hand. Output: results/figure11_setup_R110.{pdf,svg,png}"""
import json, numpy as np
import ur5e_minimal as U
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
names = {f.name for f in fm.fontManager.ttflist}
fam = next(n for n in ['Arial', 'Helvetica', 'Liberation Sans', 'DejaVu Sans'] if n in names)
plt.rcParams.update({'font.family': fam, 'font.size': 7, 'pdf.fonttype': 42, 'svg.fonttype': 'none', 'axes.linewidth': 0.6})
S = json.load(open('results/results.json'))['setup']; paths = U.build_paths()
COL = {'link': '#0072B2', 'ref': '#000000', 'obs': '#D55E00'}
ALPHA = {0: 0.30, 1: 0.55, 2: 0.85}
def draw_arm(ax, q, alpha):
    for (a, b, r) in U.capsule_points(q):
        ax.plot(*zip(a, b), color=COL['link'], lw=1.6 + 55*r, alpha=alpha, solid_capstyle='round')
    fr = U.fk_frames(q)
    ax.plot(*zip(np.zeros(3), fr[1][:3, 3], fr[2][:3, 3]), color=COL['link'], lw=3.0, alpha=alpha, solid_capstyle='round')
def sphere(ax, c, r):
    u, v = np.mgrid[0:2*np.pi:24j, 0:np.pi:12j]
    ax.plot_surface(c[0] + r*np.cos(u)*np.sin(v), c[1] + r*np.sin(u)*np.sin(v), c[2] + r*np.cos(v), color=COL['obs'], alpha=0.55, linewidth=0, shade=True)
def panel(ax, name, title, view, lims, lab_s):
    pth = paths[name]; Qref = U.dense_reference(pth); n = len(Qref)
    P0 = pth['P0']; d = pth['d']/np.linalg.norm(pth['d']); L = pth['L']
    ax.plot(*zip(P0, P0 + L*d), color=COL['ref'], lw=1.6, zorder=10)
    draw_arm(ax, Qref[(n-1)//2], 0.9)
    for k, idx in enumerate((0, (n-1)//2, n-1)):
        p = U.fk(Qref[idx])[:3, 3]; ax.scatter(*p, color='k', s=10, zorder=11)
        if k != 1: ax.text(p[0], p[1], p[2] + 0.04, lab_s[k], fontsize=6.5, ha='center', zorder=12)
    c = np.array(S[name]['obstacle_center']); sphere(ax, c, U.OBST_RADIUS)
    ax.scatter(0, 0, 0, marker='s', color='k', s=18); ax.text(0.0, 0.0, -0.07, 'base', fontsize=6.5, ha='center')
    ax.set_xlim(*lims[0]); ax.set_ylim(*lims[1]); ax.set_zlim(*lims[2]); ax.set_box_aspect((lims[0][1]-lims[0][0], lims[1][1]-lims[1][0], lims[2][1]-lims[2][0]))
    ax.view_init(*view); ax.set_xlabel('x (m)', labelpad=-4); ax.set_ylabel('y (m)', labelpad=-4); ax.set_zlabel('z (m)', labelpad=-4)
    ax.tick_params(labelsize=5.5, pad=-3); ax.set_title(title, loc='left', fontweight='bold', fontsize=7.5)
    for a_ in (ax.xaxis, ax.yaxis, ax.zaxis): a_.pane.set_facecolor((1, 1, 1, 0)); a_.pane.set_edgecolor('0.8'); a_._axinfo['grid']['linewidth'] = 0.3
fig = plt.figure(figsize=(7.2, 3.3))
a1 = fig.add_subplot(1, 2, 1, projection='3d'); a2 = fig.add_subplot(1, 2, 2, projection='3d')
panel(a1, 'regular', '(a) Regular line (0.5 m)', (22, -52), ((-0.15, 0.55), (-0.3, 0.65), (0.0, 0.7)), ('s = 0', '', 's = 1'))
panel(a2, 'wrist', '(b) Wrist-crossing line (0.2 m)', (22, -38), ((-0.65, 0.05), (-0.4, 0.3), (0.0, 0.7)), ('s = 0', '', 's = 1'))
from matplotlib.lines import Line2D
fig.legend(handles=[Line2D([], [], color=COL['link'], lw=3, label='UR5e link capsules at the midpoint of the reference lift (s = 0.5; q$_5$ = 0 in b)'),
                    Line2D([], [], color=COL['ref'], lw=1.6, label='reference line'),
                    Line2D([], [], marker='o', ls='none', color=COL['obs'], alpha=0.7, label='spherical obstacle, r = 0.05 m')],
           loc='lower center', ncol=3, frameon=False, fontsize=6.3, bbox_to_anchor=(0.5, -0.01))
fig.subplots_adjust(left=0.0, right=1.0, top=0.95, bottom=0.08, wspace=0.0)
for ext in ('pdf', 'svg'): fig.savefig(f'results/figure11_setup_R110.{ext}', bbox_inches='tight')
fig.savefig('results/figure11_setup_R110.png', dpi=600, bbox_inches='tight'); print('font', fam)
