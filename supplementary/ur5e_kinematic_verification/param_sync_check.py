#!/usr/bin/env python3
"""R108: parameter-synchronous position error of the reconstructed curve (the UR5e Level 1 check in ur5e_minimal.py
records the orthogonal deviation from the line segment). Here, for the same joint sequences (same methods, N, seeds),
we also compute |FK(q_I(s)) - x(s)| with s = (k + j/SUBSAMPLES)/(N-1), plus the progress t(s) along the line and its monotonicity.
Nothing in ur5e_minimal.py is changed. Output: results/param_sync.json, param_sync_log.txt"""
import json, numpy as np
import ur5e_minimal as U
out=[]; log=[]
paths=U.build_paths()
for name,pth in paths.items():
    P0=pth['P0']; d=pth['d']/np.linalg.norm(pth['d']); L=pth['L']
    for N in U.N_LIST:
        Ts,_,_=U.make_line(pth['P0'],pth['d'],pth['L'],pth['R'],N)
        for mname,fn in (('M1',U.m1_nearest),('M2',U.m2_graph),('M3',U.m3_dls)):
            Q=fn(Ts,pth['q_init'])
            if Q is None: continue
            orth=0.0; sync=0.0; tprev=-1e9; mono=True; tmin=1e9; tmax=-1e9
            for k in range(N-1):
                for j in range(U.SUBSAMPLES+1):
                    s=(k+j/U.SUBSAMPLES)/(N-1)
                    q=Q[k]+(j/U.SUBSAMPLES)*(Q[k+1]-Q[k]); p=U.fk(q)[:3,3]
                    v=p-P0; t=v@d
                    orth=max(orth,np.linalg.norm(v-np.clip(t,0,L)*d))
                    sync=max(sync,np.linalg.norm(p-(P0+s*L*d)))
                    if t<tprev-1e-12: mono=False
                    tprev=t; tmin=min(tmin,t); tmax=max(tmax,t)
            r=dict(path=name,N=N,method=mname,orth_mm=orth*1e3,sync_mm=sync*1e3,monotone=bool(mono),t_min_mm=tmin*1e3,t_max_over_L=tmax/L)
            out.append(r)
            s=f"{name:8s} N={N:3d} {mname}: orth {orth*1e3:9.4f} mm  sync {sync*1e3:9.4f} mm  monotone {mono}  t_min {tmin*1e3:.3f} mm t_max/L {tmax/L:.6f}"
            print(s); log.append(s)
json.dump(out,open('results/param_sync.json','w'),indent=1)
open('param_sync_log.txt','w').write('\n'.join(log)+'\n')
