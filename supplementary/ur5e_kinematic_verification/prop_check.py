#!/usr/bin/env python3
"""Numerical check of the sufficient condition of Section 5.1 (R60) against the UR5e run.

Written BEFORE it was run; no thresholds, tolerances or N values of ur5e_minimal.py are changed or tuned.
Proposition (joint-linear interpolation between waypoints q_k, q_{k+1}, h_k = ||q_{k+1}-q_k||_2):
  (i) task deviation: if e(q) is the C^2 task-error map (orthogonal position error to the task line, or the rotation vector to the target
      orientation) with |e(q_k)|, |e(q_{k+1})| <= eps_w, then on the segment |e(q(t))| <= eps_w + M_k h_k^2 / 8,
      M_k >= sup over the segment of the operator norm of the second derivative D^2 e.
  (ii) clearance: if c is the capsule-obstacle clearance and L bounds the speed of every capsule end point per rad of joint motion, then
      c(q(t)) >= min(c(q_k), c(q_{k+1})) - L h_k / 2 on the segment.
M_k is estimated numerically (finite-difference Hessian at the sub-samples of each segment, per-point bound sqrt(sum_i ||H_i||_2^2)):
a sampled estimate, not an interval-certified constant. L is the sampled maximum of the end-point Jacobian norm.
Usage: python3 prop_check.py   (needs ur5e_minimal.py in the same folder; writes results/prop_check.json, results/prop_check.csv, prop_check_log.txt)
"""
import json, csv, os, sys, time
import numpy as np
import ur5e_minimal as U

H_FD = 1e-4

def e_pos_fn(pth):
    d = pth['d']/np.linalg.norm(pth['d']); P0 = pth['P0']
    return lambda q: (np.eye(3) - np.outer(d, d)) @ (U.fk(q)[:3, 3] - P0)
def e_rot_fn(pth):
    return lambda q: U.rotvec_err(U.fk(q)[:3, :3], pth['R'])

def hess_bound(f, q):
    """sqrt(sum_i ||H_i||_2^2) with H_i the Hessian of component i of f at q (central finite differences)."""
    n = 6; E = np.eye(n)*H_FD; m = len(f(q)); Hs = np.zeros((m, n, n))
    for i in range(n):
        for j in range(i, n):
            v = (f(q+E[i]+E[j]) - f(q+E[i]-E[j]) - f(q-E[i]+E[j]) + f(q-E[i]-E[j]))/(4*H_FD**2)
            Hs[:, i, j] = v; Hs[:, j, i] = v
    return float(np.sqrt(sum(np.linalg.norm(Hs[k], 2)**2 for k in range(m))))

def end_points(q):
    fr = U.fk_frames(q); pts = [fr[i][:3, 3] for i in range(2, 7)]; pts.append(fr[6][:3, 3] + U.TOOL_TIP*fr[6][:3, 2]); return np.concatenate(pts)
def lip_clear(q):
    """max over capsule end points of the spectral norm of their position Jacobian (rad -> m), finite differences."""
    E = np.eye(6)*H_FD; J = np.zeros((18, 6))
    for i in range(6): J[:, i] = (end_points(q+E[i]) - end_points(q-E[i]))/(2*H_FD)
    return max(np.linalg.norm(J[3*k:3*k+3], 2) for k in range(6))

def main():
    t0 = time.time(); log = []
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s); log.append(s)
    paths = U.build_paths(); rows = []; summary = {}
    for name, pth in paths.items():
        Qref = U.dense_reference(pth); center, _, _ = U.place_obstacle(Qref)
        ep, er = e_pos_fn(pth), e_rot_fn(pth)
        # global estimates of M and L on the dense reference lift (every 20th of 2001 points)
        Mp = max(hess_bound(ep, q) for q in Qref[::20]); Mr = max(hess_bound(er, q) for q in Qref[::20]); Lc = max(lip_clear(q) for q in Qref[::20])
        qlen = float(np.sum(np.linalg.norm(np.diff(Qref, axis=0), axis=1)))
        summary[name] = dict(M_pos=Mp, M_rot=Mr, L_clear=Lc, ref_joint_path_length_2norm=qlen)
        P(f'[{name}] on reference lift: M_pos {Mp:.3f} m/rad^2, M_rot {Mr:.3f} rad/rad^2, L_clear {Lc:.3f} m/rad, joint path length {qlen:.3f} rad')
        for N in U.N_LIST:
            Ts, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N)
            nsub = 10 if N <= 50 else 2
            for mname, fn in (('M1', U.m1_nearest), ('M2', U.m2_graph), ('M3', U.m3_dls)):
                Q = fn(Ts, pth['q_init'])
                if Q is None: continue
                epsp = max(np.linalg.norm(ep(q)) for q in Q); epsr = max(np.linalg.norm(er(q)) for q in Q)
                bp = br = bc = 0.0; mp = mr = 0.0; cl_meas = np.inf; cl_bound = np.inf; ok = True; hmax = 0.0; worst = {}
                for k in range(N-1):
                    h = float(np.linalg.norm(Q[k+1]-Q[k])); hmax = max(hmax, h)
                    pts = [Q[k] + (j/nsub)*(Q[k+1]-Q[k]) for j in range(nsub+1)]
                    Mp_k = max(hess_bound(ep, q) for q in pts); Mr_k = max(hess_bound(er, q) for q in pts)
                    Lk = max(lip_clear(q) for q in pts)
                    dp = max(np.linalg.norm(ep(q)) for q in (Q[k] + (j/10)*(Q[k+1]-Q[k]) for j in range(11)))
                    dr = max(np.linalg.norm(er(q)) for q in (Q[k] + (j/10)*(Q[k+1]-Q[k]) for j in range(11)))
                    cm = min(U.clearance(q, center) for q in (Q[k] + (j/10)*(Q[k+1]-Q[k]) for j in range(11)))
                    c_nodes = min(U.clearance(Q[k], center), U.clearance(Q[k+1], center))
                    Bp = epsp + Mp_k*h*h/8; Br = epsr + Mr_k*h*h/8; Bc = c_nodes - Lk*h/2
                    ok = ok and (Bp >= dp) and (Br >= dr) and (Bc <= cm)
                    bp = max(bp, Bp); br = max(br, Br); mp = max(mp, dp); mr = max(mr, dr)
                    cl_bound = min(cl_bound, Bc); cl_meas = min(cl_meas, cm)
                rows.append(dict(path=name, N=N, method=mname, max_step_2norm=hmax, dev_pos_measured=mp, dev_pos_bound=bp, ratio_pos=bp/max(mp, 1e-300),
                                 dev_rot_measured=mr, dev_rot_bound=br, ratio_rot=br/max(mr, 1e-300),
                                 clr_measured=cl_meas, clr_lower_bound=cl_bound, bound_holds=bool(ok)))
                r = rows[-1]
                P(f"  {name:8s} N={N:3d} {mname}: h {hmax:.3f} | pos meas {mp*1e3:.4f} mm bound {bp*1e3:.3f} mm | rot meas {mr:.2e} bound {br:.2e} rad | clr meas {cl_meas*1e3:.2f} bound {cl_bound*1e3:.2f} mm | holds {ok}")
        # step size the sufficient condition asks for, against the thresholds of ur5e_minimal.py
        hreq_pos = float(np.sqrt(8*(U.TOL_POS - 2e-9)/Mp)); hreq_rot = float(np.sqrt(8*(U.TOL_ROT - 2e-7)/Mr)); hreq_c = 2*(0.02 - U.C_MIN)/Lc
        summary[name].update(h_required_pos=hreq_pos, h_required_rot=hreq_rot, h_required_clearance=hreq_c,
                             N_sufficient=int(np.ceil(qlen/min(hreq_pos, hreq_rot)))+1, N_sufficient_clearance=int(np.ceil(qlen/hreq_c))+1)
        P(f"[{name}] required h: pos {hreq_pos:.4f} rad, rot {hreq_rot:.4f} rad, clearance {hreq_c:.4f} rad -> N >= {summary[name]['N_sufficient']} (pose), N >= {summary[name]['N_sufficient_clearance']} (clearance)")
    os.makedirs('results', exist_ok=True)
    json.dump(dict(summary=summary, rows=rows, H_FD=H_FD), open('results/prop_check.json', 'w'), indent=1)
    with open('results/prop_check.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    P(f'all bounds hold: {all(r["bound_holds"] for r in rows)} ({len(rows)} cases), {time.time()-t0:.1f} s')
    open('prop_check_log.txt', 'w').write('\n'.join(log) + '\n')

if __name__ == '__main__':
    main()
