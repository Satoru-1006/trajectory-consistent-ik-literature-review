#!/usr/bin/env python3
"""Minimal kinematics-only UR5e run for the review's Section 5.1.

Everything that defines the experiment is fixed in the PARAMETERS block below
BEFORE the first run (written 2026-10-20, before any result was computed).
Nothing in this block was changed after seeing results.  See README.md.

Usage:  python3 ur5e_minimal.py            (writes results/ and run_log.txt)
"""
import json, csv, sys, platform, time
import numpy as np

# ----------------------------------------------------------------------------
# PARAMETERS (fixed before the first run)
# ----------------------------------------------------------------------------
# UR5e standard DH parameters, from the Universal Robots support article
# "Parameters for calculations of kinematics and dynamics" (UR5e column):
#   d = [0.1625, 0, 0, 0.1333, 0.0997, 0.0996] m,
#   a = [0, -0.425, -0.3922, 0, 0, 0] m,
#   alpha = [pi/2, 0, 0, pi/2, -pi/2, 0].
DH_D = np.array([0.1625, 0.0, 0.0, 0.1333, 0.0997, 0.0996])
DH_A = np.array([0.0, -0.425, -0.3922, 0.0, 0.0, 0.0])
DH_ALPHA = np.array([np.pi/2, 0.0, 0.0, np.pi/2, -np.pi/2, 0.0])

SEED = 20261020                      # random poses for the FK/IK check
N_RANDOM_POSES = 2000
N_LIST = [5, 10, 20, 50, 100, 200]   # waypoint counts
N_REF = 2001                         # dense reference lift (2000 segments)
SUBSAMPLES = 10                      # sub-samples per segment on the reconstructed curve

# Paths.  Regular line: 0.5 m, tool pointing down (flange z = -z_base).
REG_START_POS = np.array([0.35, -0.25, 0.35])   # m
REG_DIR = np.array([0.0, 1.0, 0.0])
REG_LEN = 0.5
REG_R = np.diag([1.0, -1.0, -1.0])
REG_SEED_Q = np.array([0.2, -1.2, 1.4, -1.8, -1.57, 0.0])  # picks the branch of the given start state
# Wrist-crossing line: 0.2 m, midpoint = FK(Q_SING) with q5 = 0 exactly (wrist-singular pose);
# fixed orientation = orientation of that pose; the line runs along the flange z axis of that pose
# (the tangential direction, so q5 changes sign along the line).
Q_SING = np.array([0.4, -1.5, 1.6, -1.2, 0.0, 0.5])
# REVISION (after run 1, see README): the given start state of this line is the analytic IK solution at the start
# pose nearest to Q_SING, and the dense reference lift is tracked from that start state (as for the regular line).
# Run 1 built the reference outward from Q_SING itself; at a wrist-singular pose the split of q4 and q6 is arbitrary,
# and that reference contained a 0.55 rad jump (visible as 'reference max joint step' in run1_discarded/run_log.txt).
# No threshold, tolerance, obstacle rule, c_min or N value was changed.
WR_LEN = 0.2

# Level 1 thresholds (on the reconstructed curve)
TOL_POS = 1e-3      # m
TOL_ROT = 1e-3      # rad
STEP_MAX = 0.5      # rad per waypoint step (also the edge limit of M2)
# Level 2: clearance threshold and geometry
C_MIN = 0.01        # m (half of the reference clearance below)
REF_CLEARANCE = 0.02  # m: obstacle is placed so that the dense reference lift has exactly this minimum clearance
OBST_RADIUS = 0.05  # m
# Link capsules between consecutive DH frame origins: (frame a, frame b, radius)
CAPSULES = [(2, 3, 0.05), (3, 4, 0.045), (4, 5, 0.04), (5, 6, 0.04)]  # upper arm, forearm, wrist 1, wrist 2
TOOL_TIP = 0.10     # m along flange z, capsule radius 0.03 from flange origin to tip
TOOL_R = 0.03

# DLS (M3)
DLS_LAMBDA = 0.01
DLS_MAXIT = 200
DLS_TOL_POS = 1e-9
DLS_TOL_ROT = 1e-9
SING_EPS = 1e-6     # |q5| below this is treated as exactly singular in the analytic IK (q6 := 0)

# ----------------------------------------------------------------------------
# Kinematics
# ----------------------------------------------------------------------------
def rz(t):
    c, s = np.cos(t), np.sin(t); return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
def rx(t):
    c, s = np.cos(t), np.sin(t); return np.array([[1.0, 0, 0], [0, c, -s], [0, s, c]])

def dh(theta, d, a, al):
    ct, st, ca, sa = np.cos(theta), np.sin(theta), np.cos(al), np.sin(al)
    return np.array([[ct, -st*ca, st*sa, a*ct], [st, ct*ca, -ct*sa, a*st], [0, sa, ca, d], [0, 0, 0, 1.0]])

def fk_frames(q):
    T = np.eye(4); out = [T.copy()]
    for i in range(6):
        T = T @ dh(q[i], DH_D[i], DH_A[i], DH_ALPHA[i]); out.append(T.copy())
    return out

def fk(q):
    return fk_frames(q)[-1]

def wrap(x):
    return (x + np.pi) % (2*np.pi) - np.pi

def ik_all(T):
    """Analytic IK of the UR5e (up to 8 solutions), joint angles wrapped to (-pi, pi]."""
    R = T[:3, :3]; p = T[:3, 3]
    p5 = p - DH_D[5]*R[:, 2]
    rho = np.hypot(p5[0], p5[1])
    if rho < abs(DH_D[3]): return []
    phi = np.arctan2(p5[1], p5[0]); asn = np.arcsin(DH_D[3]/rho)
    sols = []
    for q1 in (phi + asn, phi + np.pi - asn):
        R01 = rz(q1) @ rx(np.pi/2)
        M = R01.T @ R
        # M = Rz(q234) Ry(-q5) Rz(q6)  (ZYZ decomposition)
        b = np.arccos(np.clip(M[2, 2], -1, 1))
        branches = []
        if b < SING_EPS:                      # q5 = 0: only q234 + q6 is determined
            branches.append((0.0, np.arctan2(M[1, 0], M[0, 0]), 0.0))
        else:
            sb = np.sin(b)
            # beta = +b  -> q5 = -b ;  beta = -b -> q5 = +b
            branches.append((-b, np.arctan2(M[1, 2], M[0, 2]), np.arctan2(M[2, 1], -M[2, 0])))
            branches.append((+b, np.arctan2(-M[1, 2], -M[0, 2]), np.arctan2(-M[2, 1], M[2, 0])))
        p1 = R01.T @ (p - np.array([0, 0, DH_D[0]]))
        for q5, alpha, q6 in branches:
            z4 = np.array([np.sin(alpha), -np.cos(alpha)])
            z5 = np.array([-np.sin(q5)*np.cos(alpha), -np.sin(q5)*np.sin(alpha)])
            w = p1[:2] - DH_D[4]*z4 - DH_D[5]*z5
            c3 = (w @ w - DH_A[1]**2 - DH_A[2]**2) / (2*DH_A[1]*DH_A[2])
            if abs(c3) > 1 + 1e-12: continue
            for q3 in (np.arccos(np.clip(c3, -1, 1)), -np.arccos(np.clip(c3, -1, 1))):
                q2 = np.arctan2(w[1], w[0]) - np.arctan2(DH_A[2]*np.sin(q3), DH_A[1] + DH_A[2]*np.cos(q3))
                q4 = alpha - q2 - q3
                sols.append(wrap(np.array([q1, q2, q3, q4, q5, q6])))
    return sols

def pose_err(T, Tt):
    """Position error [m] and rotation error [rad] between two poses."""
    ep = np.linalg.norm(T[:3, 3] - Tt[:3, 3])
    Rr = Tt[:3, :3] @ T[:3, :3].T
    er = np.arccos(np.clip((np.trace(Rr) - 1)/2, -1, 1))
    return ep, er

def rotvec_err(R, Rt):
    Rr = Rt @ R.T
    ang = np.arccos(np.clip((np.trace(Rr) - 1)/2, -1, 1))
    if ang < 1e-12: return np.zeros(3)
    v = np.array([Rr[2, 1]-Rr[1, 2], Rr[0, 2]-Rr[2, 0], Rr[1, 0]-Rr[0, 1]])
    return ang * v / (2*np.sin(ang)) if ang < np.pi - 1e-6 else ang * v / np.linalg.norm(v)

def jacobian(q):
    fr = fk_frames(q); pe = fr[-1][:3, 3]
    J = np.zeros((6, 6))
    for i in range(6):
        z = fr[i][:3, 2]; o = fr[i][:3, 3]
        J[:3, i] = np.cross(z, pe - o); J[3:, i] = z
    return J

def unwrap_to(q, qref):
    return q + 2*np.pi*np.round((qref - q)/(2*np.pi))

# ----------------------------------------------------------------------------
# Methods
# ----------------------------------------------------------------------------
def m1_nearest(Ts, q0):
    """M1: at each waypoint take the analytic IK solution closest (2-norm, angles unwrapped) to the previous one."""
    Q = [q0.copy()]
    for T in Ts[1:]:
        sols = ik_all(T)
        if not sols: return None
        cands = [unwrap_to(s, Q[-1]) for s in sols]
        Q.append(min(cands, key=lambda c: np.linalg.norm(c - Q[-1])))
    return np.array(Q)

def m2_graph(Ts, q0):
    """M2: dynamic programming over the graph of all analytic IK solutions; an edge exists if every joint
    changes by at most STEP_MAX (wrapped difference); cost = sum of squared joint steps.  The first node is the given state."""
    layers = [ik_all(T) for T in Ts]
    if any(len(L) == 0 for L in layers): return None
    d0 = [np.linalg.norm(wrap(s - q0)) for s in layers[0]]
    cost = [np.inf]*len(layers[0]); cost[int(np.argmin(d0))] = 0.0
    if min(d0) > 1e-6: return None
    back = [[None]*len(L) for L in layers]
    for k in range(1, len(layers)):
        new = [np.inf]*len(layers[k])
        for j, qj in enumerate(layers[k]):
            for i, qi in enumerate(layers[k-1]):
                if not np.isfinite(cost[i]): continue
                d = wrap(qj - qi)
                if np.max(np.abs(d)) <= STEP_MAX:
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
        Q.append(Q[-1] + wrap(layers[k][idx[k]] - layers[k-1][idx[k-1]]))
    return np.array(Q)

def dls_step(q, Tt):
    for _ in range(DLS_MAXIT):
        T = fk(q)
        e = np.concatenate([Tt[:3, 3] - T[:3, 3], rotvec_err(T[:3, :3], Tt[:3, :3])])
        if np.linalg.norm(e[:3]) < DLS_TOL_POS and np.linalg.norm(e[3:]) < DLS_TOL_ROT: break
        J = jacobian(q)
        q = q + J.T @ np.linalg.solve(J @ J.T + DLS_LAMBDA**2*np.eye(6), e)
    return q

def m3_dls(Ts, q0, order=1):
    Q = [q0.copy()]
    for T in Ts[1:]:
        Q.append(dls_step(Q[-1], T))
    return np.array(Q)

# ----------------------------------------------------------------------------
# Paths, checks
# ----------------------------------------------------------------------------
def make_line(P0, d, L, R, n):
    d = d/np.linalg.norm(d)
    Ts = []
    for s in np.linspace(0, 1, n):
        T = np.eye(4); T[:3, :3] = R; T[:3, 3] = P0 + s*L*d; Ts.append(T)
    return Ts, P0, d

def build_paths():
    paths = {}
    # regular line: start state = IK solution nearest to REG_SEED_Q at the start pose
    T0 = np.eye(4); T0[:3, :3] = REG_R; T0[:3, 3] = REG_START_POS
    sols = ik_all(T0)
    q_init = min((unwrap_to(s, REG_SEED_Q) for s in sols), key=lambda c: np.linalg.norm(c - REG_SEED_Q))
    paths['regular'] = dict(P0=REG_START_POS, d=REG_DIR, L=REG_LEN, R=REG_R, q_init=q_init, q_mid=None)
    # wrist line: midpoint pose FK(Q_SING); start state = IK solution at the start pose nearest to Q_SING
    Ts = fk(Q_SING); R = Ts[:3, :3]; Pm = Ts[:3, 3]; d = R[:, 2]
    P0w = Pm - 0.5*WR_LEN*d
    T0w = np.eye(4); T0w[:3, :3] = R; T0w[:3, 3] = P0w
    qw = min((unwrap_to(s, Q_SING) for s in ik_all(T0w)), key=lambda c: np.linalg.norm(c - Q_SING))
    paths['wrist'] = dict(P0=P0w, d=d, L=WR_LEN, R=R, q_init=qw, q_mid=None)
    return paths

def dense_reference(pth):
    Ts, _, _ = make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N_REF)
    if pth['q_mid'] is None:
        Q = m3_dls(Ts, pth['q_init'])
    else:
        mid = (N_REF-1)//2
        fwd = m3_dls(Ts[mid:], pth['q_mid'])
        bwd = m3_dls(Ts[:mid+1][::-1], pth['q_mid'])[::-1]
        Q = np.vstack([bwd[:-1], fwd])
        pth['q_init'] = Q[0].copy()
    return Q

def capsule_points(q):
    fr = fk_frames(q)
    org = [f[:3, 3] for f in fr]
    segs = [(org[a], org[b], r) for a, b, r in CAPSULES]
    segs.append((org[6], org[6] + TOOL_TIP*fr[6][:3, 2], TOOL_R))
    return segs

def seg_point_dist(a, b, c):
    ab = b - a; t = np.clip(((c - a) @ ab) / max(ab @ ab, 1e-18), 0, 1)
    return np.linalg.norm(a + t*ab - c)

def clearance(q, center):
    return min(seg_point_dist(a, b, center) - r - OBST_RADIUS for a, b, r in capsule_points(q))

def place_obstacle(Qref):
    """Obstacle beside the forearm of the reference lift: centre = forearm-axis midpoint at s=0.5 plus t*n,
    n = horizontal arm-plane normal (-sin q1, cos q1, 0) of the reference at s=0.5; t is found by bisection so that
    the minimum clearance of the dense reference lift equals REF_CLEARANCE."""
    qm = Qref[(len(Qref)-1)//2]; fr = fk_frames(qm)
    mid = 0.5*(fr[3][:3, 3] + fr[4][:3, 3])
    n = np.array([-np.sin(qm[0]), np.cos(qm[0]), 0.0])
    f = lambda t: min(clearance(q, mid + t*n) for q in Qref[::10]) - REF_CLEARANCE
    lo, hi = 0.0, 1.0
    assert f(lo) < 0 < f(hi), (f(lo), f(hi))
    for _ in range(60):
        m = 0.5*(lo+hi)
        if f(m) > 0: hi = m
        else: lo = m
    t = 0.5*(lo+hi)
    center = mid + t*n
    return center, t, min(clearance(q, center) for q in Qref)

def evaluate(Q, pth, center):
    """Level 1 and Level 2 metrics of a joint sequence Q (N x 6) for the given path."""
    N = len(Q); Pm = pth['P0']; d = pth['d']; L = pth['L']; Rt = pth['R']
    wp_pos = wp_rot = 0.0
    step = float(np.max(np.abs(np.diff(Q, axis=0))))
    curve_pos = curve_rot = 0.0; clr_wp = np.inf; clr_curve = np.inf
    for k in range(N):
        T = fk(Q[k]); s = k/(N-1)
        ep = np.linalg.norm(T[:3, 3] - (Pm + s*L*d)); er = np.arccos(np.clip((np.trace(Rt @ T[:3, :3].T)-1)/2, -1, 1))
        wp_pos = max(wp_pos, ep); wp_rot = max(wp_rot, er)
        clr_wp = min(clr_wp, clearance(Q[k], center))
    for k in range(N-1):
        for j in range(SUBSAMPLES+1):
            q = Q[k] + (j/SUBSAMPLES)*(Q[k+1]-Q[k]); T = fk(q)
            v = T[:3, 3] - Pm; t = np.clip(v @ d, 0, L); ep = np.linalg.norm(v - t*d)
            er = np.arccos(np.clip((np.trace(Rt @ T[:3, :3].T)-1)/2, -1, 1))
            curve_pos = max(curve_pos, ep); curve_rot = max(curve_rot, er)
            clr_curve = min(clr_curve, clearance(q, center))
    l1 = (step <= STEP_MAX) and (curve_pos <= TOL_POS) and (curve_rot <= TOL_ROT)
    l2 = l1 and (clr_curve >= C_MIN)
    return dict(max_joint_step=step, wp_pos_err=wp_pos, wp_rot_err=wp_rot, curve_pos_dev=curve_pos, curve_rot_dev=curve_rot,
                clr_waypoints=clr_wp, clr_curve=clr_curve, level1_pass=bool(l1), level2_pass=bool(l2))

# ----------------------------------------------------------------------------
def main():
    t0 = time.time(); log = []
    def P(*a):
        s = ' '.join(str(x) for x in a); print(s); log.append(s)
    P('python', platform.python_version(), 'numpy', np.__version__, 'seed', SEED)
    # --- FK/IK check on random poses (position and rotation errors reported separately)
    rng = np.random.default_rng(SEED)
    worst_p = worst_r = 0.0; nfail = 0; nsol = []
    for _ in range(N_RANDOM_POSES):
        q = rng.uniform(-np.pi, np.pi, 6); T = fk(q); sols = ik_all(T); nsol.append(len(sols))
        if not sols: nfail += 1; continue
        errs = [pose_err(fk(s), T) for s in sols]
        worst_p = max(worst_p, max(e[0] for e in errs)); worst_r = max(worst_r, max(e[1] for e in errs))
        # the generating configuration must be among the solutions (wrapped)
        if min(np.linalg.norm(wrap(s - q)) for s in sols) > 1e-6: nfail += 1
    P(f'FK/IK check on {N_RANDOM_POSES} random poses: failures {nfail}, solutions per pose min/max {min(nsol)}/{max(nsol)}, '
      f'max position error {worst_p:.2e} m, max rotation error {worst_r:.2e} rad')
    paths = build_paths(); results = []; curves = {}; setup = {}
    for name, pth in paths.items():
        Qref = dense_reference(pth)
        refstep = float(np.max(np.abs(np.diff(Qref, axis=0))))
        center, t, minclr = place_obstacle(Qref)
        qs = np.min(np.abs(Qref[:, 4]))
        setup[name] = dict(q_init=pth['q_init'].tolist(), obstacle_center=center.tolist(), obstacle_offset_t=float(t),
                           ref_min_clearance=float(minclr), ref_max_joint_step=refstep, ref_min_abs_q5=float(qs),
                           P0=pth['P0'].tolist(), direction=pth['d'].tolist(), length=pth['L'])
        P(f'[{name}] q_init={np.round(pth["q_init"],4).tolist()}  reference max joint step {refstep:.4f} rad  min|q5| on ref {qs:.2e}')
        P(f'[{name}] obstacle centre {np.round(center,4).tolist()} (offset {t:.4f} m), reference min clearance {minclr:.5f} m')
        for N in N_LIST:
            Ts, _, _ = make_line(pth['P0'], pth['d'], pth['L'], pth['R'], N)
            for mname, fn in (('M1', m1_nearest), ('M2', m2_graph), ('M3', m3_dls)):
                Q = fn(Ts, pth['q_init'])
                rec = dict(path=name, N=N, method=mname)
                if Q is None:
                    rec.update(found=False)
                else:
                    ev = evaluate(Q, pth, center)
                    # joint deviation from the dense reference lift at the waypoints (interpolated on the dense grid)
                    sref = np.linspace(0, 1, N_REF); sk = np.linspace(0, 1, N)
                    qr = np.array([np.interp(sk, sref, Qref[:, i]) for i in range(6)]).T
                    ev['max_joint_dev_from_ref'] = float(np.max(np.abs(Q - qr)))
                    ev['max_dq4_from_ref'] = float(np.max(np.abs(Q[:, 3] - qr[:, 3])))
                    rec.update(found=True, **ev)
                    if name == 'wrist' and N == 5: curves[mname] = Q.tolist()
                results.append(rec)
                if Q is None: P(f'  {name:8s} N={N:3d} {mname}: no admissible path')
                else: P(f"  {name:8s} N={N:3d} {mname}: step {rec['max_joint_step']:.3f} wp pos {rec['wp_pos_err']:.1e} m rot {rec['wp_rot_err']:.1e} rad | curve pos {rec['curve_pos_dev']*1e3:.3f} mm rot {rec['curve_rot_dev']:.2e} rad | clr wp {rec['clr_waypoints']*1e3:.2f} curve {rec['clr_curve']*1e3:.2f} mm | dev ref {rec['max_joint_dev_from_ref']:.4f} rad | L1 {rec['level1_pass']} L2 {rec['level2_pass']}")
        if name == 'wrist':
            curves['reference'] = Qref[::50].tolist(); curves['s_reference'] = np.linspace(0, 1, N_REF)[::50].tolist()
            curves['ref_q'] = Qref.tolist()
    import os; os.makedirs('results', exist_ok=True)
    json.dump(dict(results=results, setup=setup, params=dict(N_LIST=N_LIST, N_REF=N_REF, SUBSAMPLES=SUBSAMPLES, TOL_POS=TOL_POS, TOL_ROT=TOL_ROT,
              STEP_MAX=STEP_MAX, C_MIN=C_MIN, REF_CLEARANCE=REF_CLEARANCE, OBST_RADIUS=OBST_RADIUS, DLS_LAMBDA=DLS_LAMBDA, SEED=SEED,
              fkik_random=dict(n=N_RANDOM_POSES, failures=nfail, max_pos_err_m=worst_p, max_rot_err_rad=worst_r))),
              open('results/results.json', 'w'), indent=1)
    json.dump(curves, open('results/wrist_curves.json', 'w'))
    keys = ['path', 'N', 'method', 'found', 'max_joint_step', 'wp_pos_err', 'wp_rot_err', 'curve_pos_dev', 'curve_rot_dev', 'clr_waypoints',
            'clr_curve', 'max_joint_dev_from_ref', 'max_dq4_from_ref', 'level1_pass', 'level2_pass']
    with open('results/results.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore'); w.writeheader(); w.writerows(results)
    P(f'done in {time.time()-t0:.1f} s')
    open('run_log.txt', 'w').write('\n'.join(log) + '\n')

if __name__ == '__main__':
    main()
