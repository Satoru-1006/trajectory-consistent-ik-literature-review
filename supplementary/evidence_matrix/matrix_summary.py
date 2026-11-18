#!/usr/bin/env python3
"""Counts, paper lists and the global heat map of the evidence matrix.
Input : matrix_coding.csv (100 coded references: 73 class M, 7 class R, 20 class B; see coding_rules.md)
Output: counts_with_lists.csv (every count with its paper list), heatmap_cells.csv (every heat-map number with its paper list),
        figure3.pdf / figure3.svg / figure3.png (600 dpi)
Usage : python3 matrix_summary.py
"""
import csv, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

rows = list(csv.DictReader(open('matrix_coding.csv', encoding='utf-8-sig')))
for r in rows: r['ref'] = int(r['ref'])
M = [r for r in rows if r['class'] == 'M']
lab = lambda r: f"{r['ref']} {r['short']}"
out = []
def add(stat, desc, sel, denom):
    out.append(dict(statistic=stat, description=desc, n=len(sel), denominator=denom, papers='; '.join(lab(r) for r in sel)))
for c, d in (('M', 'matrix (pathwise IK or trajectory tracking)'), ('R', 'review'), ('B', 'background')):
    add('class_' + c, d, [r for r in rows if r['class'] == c], len(rows))
add('M_title_only', 'matrix papers without a reading note (all codes unverified)', [r for r in M if r['title_only'] == 'True'], len(M))
for fld, vals in (('verification', ['samples', 'edges_grid', 'curve', 'timed', 'none', 'unverified']),
                  ('constraint_finest', ['samples', 'edges', 'curve', 'timed', 'none', 'unverified']),
                  ('evidence', ['none', 'simulation', 'hardware_qualitative', 'hardware_quantitative', 'unverified']),
                  ('reconstruction_stated', ['yes', 'no', 'unverified']),
                  ('branch', ['yes', 'no', 'unverified']), ('singularity', ['yes', 'no', 'unverified']),
                  ('constraints_integrated', ['yes', 'no', 'unverified']), ('dynamic', ['yes', 'no', 'unverified']),
                  ('real_robot', ['none', 'qualitative', 'quantitative', 'unverified'])):
    for v in vals: add(f'{fld}={v}', f'matrix papers with {fld} = {v}', [r for r in M if r[fld] == v], len(M))
add('verification=discrete (samples or edges/grid)', 'own evaluation examines samples, time steps, edges or grids only', [r for r in M if r['verification'] in ('samples', 'edges_grid')], len(M))
add('real_robot=hardware', 'hardware evidence (qualitative or quantitative)', [r for r in M if r['real_robot'] in ('qualitative', 'quantitative')], len(M))
tri = lambda r, ok: all(r[k] in ok for k in ('branch', 'singularity', 'constraints_integrated'))
for tag, ok in (('strict', ('yes',)), ('possible', ('yes', 'unverified'))):
    a = [r for r in M if tri(r, ok)]
    b = [r for r in a if r['verification'] in ('curve', 'timed')]
    c = [r for r in b if r['real_robot'] in ('qualitative', 'quantitative')]
    desc = 'all coded yes' if tag == 'strict' else 'yes or unverified (upper bound)'
    add(f'intersection_{tag}_branch+singularity+constraints', f'branch, singularity and constraints_integrated: {desc}', a, len(M))
    add(f'intersection_{tag}_+curve_or_timed', 'and verification on the curve or timed motion', b, len(M))
    add(f'intersection_{tag}_+hardware', 'and hardware evidence', c, len(M))
with open('counts_with_lists.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# ---- heat map: rows = object examined by the source's own evaluation, columns = mechanism dimension
RO = [('samples', 'Samples or time steps'), ('edges_grid', 'Graph edges or grid'), ('curve', 'Reconstructed curve'),
      ('timed', 'Timed or executed motion'), ('none', 'None reported'), ('unverified', 'Unverified')]
CO = [('branch', 'Branch\nchoice', ('yes',)), ('singularity', 'Singu-\nlarity', ('yes',)),
      ('constraints_integrated', 'Con-\nstraints', ('yes',)), ('dynamic', 'Dynamic\nlimits', ('yes',)),
      ('real_robot', 'Real\nrobot', ('qualitative', 'quantitative'))]
RO = [ro for ro in RO if any(r['verification'] == ro[0] for r in M)]
cells = []; Z = []; U = []; N = []
for v, vl in RO:
    sel = [r for r in M if r['verification'] == v]; N.append(len(sel)); zr = []; ur = []
    for k, kl, ok in CO:
        y = [r for r in sel if r[k] in ok]; u = [r for r in sel if r[k] == 'unverified']
        zr.append(len(y)); ur.append(len(u))
        cells.append(dict(row=vl, column=kl.replace('\n', ' '), n_yes=len(y), n_unverified=len(u), row_total=len(sel),
                          papers_yes='; '.join(lab(r) for r in y), papers_unverified='; '.join(lab(r) for r in u)))
    Z.append(zr); U.append(ur)
with open('heatmap_cells.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(cells[0].keys())); w.writeheader(); w.writerows(cells)

fam = [f for f in ('Arial', 'Helvetica', 'Liberation Sans', 'DejaVu Sans') if f in {x.name for x in font_manager.fontManager.ttflist}][0]
plt.rcParams.update({'font.family': fam, 'font.size': 7, 'axes.linewidth': 0.8, 'svg.fonttype': 'none', 'pdf.fonttype': 42})
fig = plt.figure(figsize=(6.2, 3.3))
ax = fig.add_axes([0.295, 0.17, 0.355, 0.66]); bx = fig.add_axes([0.835, 0.17, 0.145, 0.66])
vmax = max(max(z) for z in Z)
im = ax.imshow(Z, cmap='YlGnBu', vmin=0, vmax=vmax + 4, aspect='auto')
ax.set_xticks(range(len(CO))); ax.set_xticklabels([c[1] for c in CO]); ax.xaxis.tick_top()
ax.set_yticks(range(len(RO))); ax.set_yticklabels([f'{r[1]} (n = {n})' for r, n in zip(RO, N)])
for i in range(len(RO)):
    for j in range(len(CO)):
        z = Z[i][j]; col = 'white' if z > (vmax + 4)*0.55 else 'black'
        ax.text(j, i - (0.1 if U[i][j] else 0), str(z), ha='center', va='center', color=col, fontsize=8, fontweight='bold')
        if U[i][j]: ax.text(j, i + 0.28, f'(+{U[i][j]})', ha='center', va='center', color=col, fontsize=6)
ax.set_xticks([x - 0.5 for x in range(1, len(CO))], minor=True); ax.set_yticks([y - 0.5 for y in range(1, len(RO))], minor=True)
ax.grid(which='minor', color='white', lw=1.2); ax.tick_params(which='both', length=0)
ax.set_xlabel('Cell: papers coded "yes"', labelpad=3)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title('(a) Evaluation object versus mechanism', loc='left', fontweight='bold', pad=22, fontsize=7.5)
# panel b
def cnt(tag, level):
    return [r for r in out if r['statistic'] == f'intersection_{tag}_{level}'][0]['n']
lv = ['branch+singularity+constraints', '+curve_or_timed', '+hardware']
names = ['Branch, singularity,\nconstraints all', '… plus curve or\ntimed check', '… plus\nhardware']
ys = [2, 1, 0]
vs = [cnt('strict', l) for l in lv]; vp = [cnt('possible', l) for l in lv]
bx.barh(ys, vs, height=0.5, color='#253494', edgecolor='black', lw=0.8)
for y, a in zip(ys, vs):
    bx.text(a + 0.4, y, str(a), va='center', fontsize=7, fontweight='bold')
bx.set_yticks(ys); bx.set_yticklabels(names); bx.set_xlim(0, 25); bx.set_xlabel(f'Number of papers (of {len(M)})')
bx.spines[['top', 'right']].set_visible(False); bx.tick_params(direction='out')
bx.set_title('(b) Intersection', loc='left', fontweight='bold', pad=22, fontsize=7.5)
for ext in ('pdf', 'svg'): fig.savefig(f'figure3.{ext}', bbox_inches='tight')
fig.savefig('figure3.png', dpi=600, bbox_inches='tight')
print('font', fam, 'M', len(M), 'rows', N)
for r in out[:3] + [x for x in out if x['statistic'].startswith('intersection')]: print(r['statistic'], r['n'], r['denominator'])
