#!/usr/bin/env python3
"""Supplementary tests for Section 5.1 (the thresholds of ur5e_minimal.py are unchanged).
Test A  (Level 2, adversarial obstacle): an obstacle is placed beside the joint-linear curve of M3 at the midpoint of the middle segment
        so that every waypoint clears c_min while the interpolated curve does not; the dense reference lift (2001 waypoints) must clear c_min too.
Test B  (M2 at the wrist singularity): distinguishes 'no continuous path exists' from 'the discrete candidate set cannot represent it':
        (i) edge limit sweep, (ii) candidates enriched with the exact self-motion family at the exactly singular waypoint (q6 sampled, q234 = sum - q6, q2 and q3 recomputed), (iii) waypoint counts.
Usage: python3 extra_tests.py    (needs ur5e_minimal.py in the same folder; writes results/extra_tests.json and extra_tests_log.txt)
"""
import json, numpy as np
import ur5e_minimal as U

log = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); log.append(s)

# ---------------------------------------------------------------- Test A
def adversarial(name, pth, Qref, N, delta=0.005, seed=20261105):
    Ts, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N)
    Q = U.m3_dls(Ts, pth['q_init'])
    k = (N-1)//2 if N % 2 == 1 else N//2 - 1               # segment around the path middle
    qm = Q[k] + 0.5*(Q[k+1]-Q[k])
    rng = np.random.default_rng(seed); best = None
    segs = U.capsule_points(qm)
    for trial in range(400):
        a, b, r = segs[int(rng.integers(0, 4))]               # one of the four link capsules
        p = a + rng.uniform(0.2, 0.8)*(b-a)
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        f = lambda t: U.clearance(qm, p + t*n) - delta
        lo, hi = 0.0, 0.6
        if not (f(lo) < 0 < f(hi)): continue
        for _ in range(50):
            m = 0.5*(lo+hi)
            if f(m) > 0: hi = m
            else: lo = m
        c = p + 0.5*(lo+hi)*n
        wp = min(U.clearance(q, c) for q in Q)
        ref = min(U.clearance(q, c) for q in Qref[::5])
        cur = min(U.clearance(Q[j] + (s/U.SUBSAMPLES)*(Q[j+1]-Q[j]), c) for j in range(N-1) for s in range(U.SUBSAMPLES+1))
        if wp >= U.C_MIN and ref >= U.C_MIN:
            score = wp - cur
            if best is None or score > best[0]: best = (score, c, wp, ref, cur)
    return Q, best

def run_A(out):
    P('== Test A: adversarial obstacle, Level 2 ==')
    paths = U.build_paths(); out['A'] = []
    for name, pth in paths.items():
        Qref = U.dense_reference(pth)
        Qn, best = adversarial(name, pth, Qref, 5)
        if best is None: P(f'[{name}] no adversarial placement found'); continue
        score, c, wp, ref, cur = best
        P(f'[{name}] N=5 (M3): waypoint clearance {wp*1e3:.2f} mm, dense-reference clearance {ref*1e3:.2f} mm, interpolated-curve clearance {cur*1e3:.2f} mm (c_min {U.C_MIN*1e3:.0f} mm) centre {np.round(c,4).tolist()}')
        rec = dict(path=name, center=c.tolist(), N5=dict(wp=wp, ref=ref, curve=cur), by_N=[])
        for N in U.N_LIST:
            Ts, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N)
            Q = U.m3_dls(Ts, pth['q_init'])
            wpN = min(U.clearance(q, c) for q in Q)
            curN = min(U.clearance(Q[j] + (s/U.SUBSAMPLES)*(Q[j+1]-Q[j]), c) for j in range(N-1) for s in range(U.SUBSAMPLES+1))
            P(f'   N={N:3d}: waypoints {wpN*1e3:7.2f} mm  curve {curN*1e3:7.2f} mm  waypoint check passes {wpN>=U.C_MIN}  curve check passes {curN>=U.C_MIN}')
            rec['by_N'].append(dict(N=N, wp=wpN, curve=curN))
        out['A'].append(rec)

# ---------------------------------------------------------------- Test B
def ik_family(T, q6s):
    """Exact singular self-motion family of the UR5e at q5 = 0: only q234 + q6 is fixed by the pose, so for every q6 the analytic IK is run with
    alpha = q234 = sum - q6 (the same position equations as ur5e_minimal.ik_all).  Returns the joint vectors for the given q6 values."""
    R = T[:3, :3]; p = T[:3, 3]
    p5 = p - U.DH_D[5]*R[:, 2]; rho = np.hypot(p5[0], p5[1])
    if rho < abs(U.DH_D[3]): return []
    phi = np.arctan2(p5[1], p5[0]); asn = np.arcsin(U.DH_D[3]/rho); sols = []
    for q1 in (phi + asn, phi + np.pi - asn):
        R01 = U.rz(q1) @ U.rx(np.pi/2); M = R01.T @ R
        ssum = np.arctan2(M[1, 0], M[0, 0]); p1 = R01.T @ (p - np.array([0, 0, U.DH_D[0]]))
        for q6 in q6s:
            alpha = ssum - q6; q5 = 0.0
            z4 = np.array([np.sin(alpha), -np.cos(alpha)]); z5 = np.array([-np.sin(q5)*np.cos(alpha), -np.sin(q5)*np.sin(alpha)])
            w = p1[:2] - U.DH_D[4]*z4 - U.DH_D[5]*z5
            c3 = (w @ w - U.DH_A[1]**2 - U.DH_A[2]**2) / (2*U.DH_A[1]*U.DH_A[2])
            if abs(c3) > 1 + 1e-12: continue
            for q3 in (np.arccos(np.clip(c3, -1, 1)), -np.arccos(np.clip(c3, -1, 1))):
                q2 = np.arctan2(w[1], w[0]) - np.arctan2(U.DH_A[2]*np.sin(q3), U.DH_A[1] + U.DH_A[2]*np.cos(q3))
                sols.append(U.wrap(np.array([q1, q2, q3, alpha - q2 - q3, q5, q6])))
    return sols

def m2_variant(Ts, q0, cap, enrich=False, n_fam=72):
    layers = []
    for T in Ts:
        L = U.ik_all(T)
        if enrich and any(abs(s[4]) < 1e-6 for s in L):
            L = L + ik_family(T, np.linspace(-np.pi, np.pi, n_fam, endpoint=False))
        layers.append(L)
    if any(len(L) == 0 for L in layers): return None
    d0 = [np.linalg.norm(U.wrap(s - q0)) for s in layers[0]]
    cost = [np.inf]*len(layers[0]); cost[int(np.argmin(d0))] = 0.0
    if min(d0) > 1e-6: return None
    back = [[None]*len(L) for L in layers]
    for k in range(1, len(layers)):
        new = [np.inf]*len(layers[k])
        for j, qj in enumerate(layers[k]):
            for i, qi in enumerate(layers[k-1]):
                if not np.isfinite(cost[i]): continue
                d = U.wrap(qj - qi)
                if np.max(np.abs(d)) <= cap:
                    c = cost[i] + d @ d
                    if c < new[j]: new[j] = c; back[k][j] = i
        cost = new
    if not np.any(np.isfinite(cost)): return None
    j = int(np.argmin(cost)); idx = [j]
    for k in range(len(layers)-1, 0, -1):
        j = back[k][j]; idx.append(j)
    idx = idx[::-1]
    Q = [q0.copy()]
    for k in range(1, len(layers)):
        Q.append(Q[-1] + U.wrap(layers[k][idx[k]] - layers[k-1][idx[k-1]]))
    return np.array(Q)

def run_B(out):
    P('== Test B: M2 at the wrist singularity ==')
    pth = U.build_paths()['wrist']; Qref = U.dense_reference(pth)
    refstep = float(np.max(np.abs(np.diff(Qref, axis=0))))
    P(f'dense reference lift (continuous, 2001 waypoints): max joint step {refstep:.4f} rad; min |q5| {np.min(np.abs(Qref[:,4])):.2e} -> a continuous path through the singular pose exists')
    out['B'] = dict(ref_max_step=refstep, cap_sweep=[], enrich=[], N_sweep=[])
    Ts, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], 5)
    for cap in (0.5, 0.7, 1.0, 1.5, 2.0):
        Q = m2_variant(Ts, pth['q_init'], cap)
        P(f'(i) N=5, edge limit {cap} rad, standard candidates: ' + ('no path' if Q is None else f'path found, max step {np.max(np.abs(np.diff(Q,axis=0))):.3f} rad'))
        out['B']['cap_sweep'].append(dict(cap=cap, found=Q is not None))
    for nfam in (8, 24, 72):
        Q = m2_variant(Ts, pth['q_init'], 0.5, enrich=True, n_fam=nfam)
        if Q is None: P(f'(ii) N=5, edge limit 0.5 rad, {nfam} self-motion candidates at the singular waypoint: no path'); out['B']['enrich'].append(dict(n=nfam, found=False)); continue
        ev = U.evaluate(Q, pth, np.array([10.0, 10.0, 10.0]))   # obstacle far away: only Level 1 is of interest here
        P(f'(ii) N=5, edge limit 0.5 rad, {nfam} self-motion candidates: path found, max step {ev["max_joint_step"]:.3f} rad, curve pos {ev["curve_pos_dev"]*1e3:.3f} mm, rot {ev["curve_rot_dev"]:.2e} rad, Level 1 {ev["level1_pass"]}')
        out['B']['enrich'].append(dict(n=nfam, found=True, step=ev['max_joint_step'], curve_pos=ev['curve_pos_dev'], curve_rot=ev['curve_rot_dev'], level1=ev['level1_pass']))
    far = np.array([10.0, 10.0, 10.0])
    for N in (5, 6, 7, 8, 9, 10, 11, 21, 51):
        Tn, _, _ = U.make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N)
        rec = dict(N=N)
        for lab, enr in (('standard', False), ('enriched', True)):
            Q = m2_variant(Tn, pth['q_init'], 0.5, enrich=enr, n_fam=72)
            if Q is None: rec[lab] = None; continue
            ev = U.evaluate(Q, pth, far)
            rec[lab] = dict(level1=ev['level1_pass'], curve_pos=ev['curve_pos_dev'], curve_rot=ev['curve_rot_dev'], step=ev['max_joint_step'])
        fmt = lambda r: 'no path' if r is None else f"path, Level 1 {r['level1']}, curve {r['curve_pos']*1e3:.2f} mm / {r['curve_rot']:.1e} rad, step {r['step']:.3f}"
        P(f"(iii) N={N:2d}, edge limit 0.5 rad | standard candidates: {fmt(rec['standard'])} | + 72 self-motion candidates: {fmt(rec['enriched'])}")
        out['B']['N_sweep'].append(rec)

if __name__ == '__main__':
    out = {}
    run_A(out); run_B(out)
    json.dump(out, open('results/extra_tests.json', 'w'), indent=1)
    open('extra_tests_log.txt', 'w').write('\n'.join(log) + '\n')
