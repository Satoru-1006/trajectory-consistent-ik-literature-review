#!/usr/bin/env python3
"""Where along the dense reference lift is the clearance smallest?  (diagnostic only; uses run results' setup)"""
import json, numpy as np, ur5e_minimal as u
res = json.load(open('results/results.json')); out = {}
for name, pth in u.build_paths().items():
    Q = u.dense_reference(pth); c = np.array(res['setup'][name]['obstacle_center'])
    clr = np.array([u.clearance(q, c) for q in Q]); s = np.linspace(0, 1, len(Q))
    out[name] = dict(min_clearance=float(clr.min()), s_at_min=float(s[clr.argmin()]), max_clearance=float(clr.max()),
                     s_at_max=float(s[clr.argmax()]), clearance_at_s0=float(clr[0]), clearance_at_s1=float(clr[-1]), clearance_at_s05=float(clr[len(clr)//2]))
    print(name, out[name])
json.dump(out, open('results/reference_clearance_profile.json', 'w'), indent=1)
