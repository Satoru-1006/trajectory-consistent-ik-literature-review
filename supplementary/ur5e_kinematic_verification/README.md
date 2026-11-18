# Minimal UR5e kinematics-only run (Section 5.2 of the review)

Code and results for the kinematic verification experiment (Levels 1 and 2) of the review. Figure scripts `make_figure*.py` write the experiment figures from `results/`; file names carry the draft round in which they were written.

## Reproduce
    python3 ur5e_minimal.py          # writes results/results.{json,csv}, results/wrist_curves.json, run_log.txt
    python3 reference_clearance_profile.py   # writes results/reference_clearance_profile.json
    python3 make_figure.py           # writes results/figure2.{pdf,svg,png}

Versions used: python 3.13.16, numpy 2.5.3, matplotlib 3.11.2 (figure font: Liberation Sans, Arial-metric).
Random poses of the FK/IK check use seed 20261020 (the paths and methods are deterministic).

## What is computed
* UR5e standard DH parameters (Universal Robots support article "Parameters for calculations of kinematics and dynamics"); own closed-form IK (up to 8 solutions).
* FK/IK check on 2000 random poses: no failures, max position error 1.7e-15 m, max rotation error 3.7e-8 rad.
* Two exact-pose lines (regular 0.5 m line, tool down; 0.2 m wrist-crossing line with a wrist-singular midpoint), N = 5, 10, 20, 50, 100, 200 waypoints.
* Methods: M1 nearest solution; M2 dynamic programming over all analytic IK solutions (edge limit 0.5 rad per step); M3 damped-least-squares differential IK (lambda = 0.01).
* Level 1: joint step <= 0.5 rad; position deviation of the joint-linearly reconstructed curve (10 sub-samples per segment) <= 1 mm; orientation deviation <= 1e-3 rad.
* Level 2: capsule-link clearance to one spherical obstacle (radius 0.05 m) >= c_min = 0.01 m. The obstacle is placed so that the dense reference lift (2001 waypoints) has minimum clearance exactly 0.02 m; c_min was set to half of that before the run.

## Process, stated as it happened
All parameters (thresholds, c_min, obstacle rule, N list, seed, methods) were written into the script before the first run.
Run 1 (kept in `run1_discarded/`) built the wrist-line dense reference outward from the singular pose Q_SING. At a wrist-singular pose the split of q4 and q6 is arbitrary, and that reference contained a 0.55 rad joint jump (see `run1_discarded/run_log.txt`), so it was not a valid reference. In run 2 the start state of that line is the IK solution at the start pose nearest to Q_SING and the reference is tracked from there, as for the regular line. This is the only change; no threshold, tolerance, obstacle rule, c_min or N value was changed after seeing results.

## Outcome (see results/results.csv)
* Regular line: Level 1 fails at N = 5 (5.84 mm) and N = 10 (1.19 mm) for all three methods; passes from N = 20.
* Wrist line N = 5: M1 fails (curve 5.64 mm, orientation 1.5e-2 rad, q4 0.676 rad away from the reference); M2 finds no admissible path; M3 passes (0.686 mm). Elsewhere identical.
* Level 2: every clearance is 20.0 mm (the closest approach of the reference is at an end waypoint, so interpolation cannot reduce it); Level 2 does not discriminate in this setup.

## Sufficient-condition check (`prop_check.py`)
`python3 prop_check.py` re-runs the three methods and, for every segment, compares the measured deviation of the joint-linear curve with
(i) eps_w + M h^2/8 for the position and orientation task error (h = 2-norm joint step, M from a finite-difference Hessian, per-point bound sqrt(sum_i ||H_i||_2^2)) and
(ii) min(node clearance) - L h/2 for the clearance (L = largest capsule end-point speed per rad).
The script was written before it was run; the thresholds, c_min and N list are those of `ur5e_minimal.py`, nothing was tuned. M and L are sampled numerical estimates (not interval-certified), so the check is a consistency check.
Result (results/prop_check.csv, prop_check_log.txt): the bound was not below the measured value in any of the 35 results. Position bound / measured = 4.0 to 4.5, except 21.5 for M1 at N = 5 on the wrist line. Rotation deviation is numerically zero except at the wrist line, N = 5 (ratios 11 and 58).
Step sizes the condition requires for the 1 mm and 1e-3 rad tolerances: N >= 29 (regular), N >= 14 (wrist); for the clearance margin c_min = 0.01 m: N >= 66 and N >= 26. The measured results pass the tolerances from N = 20 (regular) and N = 10 (wrist; M3 already at N = 5) and the clearance never fell below 20 mm, so the condition is conservative.

## Supplementary tests (extra_tests.py; added after internal review comments on the sufficient condition and on Level 2)
`python3 extra_tests.py` writes results/extra_tests.json and extra_tests_log.txt (about 2 minutes). Thresholds, tolerances and the N list of ur5e_minimal.py are unchanged.
* Test A, adversarial Level 2: regular line, M3, N = 5. A seeded random search (400 candidate placements of the same 0.05 m obstacle beside the four link capsules at the midpoint configuration of the middle segment, clearance there set to 5 mm) keeps the placement with the largest gap between waypoint clearance and curve clearance among those where every waypoint and the dense reference lift clear c_min. Result: waypoints 26.02 mm, dense reference 10.51 mm, interpolated curve 5.00 mm. Curve clearance by N: 5.00 (N=5), 9.36 (10), 10.26 (20), 10.49 (50), 10.50 (100), 10.51 (200) mm. The wrist-crossing line (joint steps < 0.16 rad) gave no placement with waypoint clearance and reference clearance >= c_min and a violating curve.
* Test B, M2 at the wrist singularity. (i) Edge limit 0.5/0.7/1.0/1.5/2.0 rad with the standard candidates at N = 5: no path at 0.5, a path with max step 0.689 rad from 0.7 (identical to the M1 path, Level 1 fails with 5.64 mm). (ii) Standard IK fixes q6 = 0 at an exactly singular waypoint; adding the exact self-motion family (q6 sampled uniformly, q234 = sum - q6, q2/q3 recomputed) with 8/24/72 members: Level 1 passes with 72 (curve 0.686 mm, rotation 2.7e-4 rad), as M3. (iii) Standard candidates fail at every odd N tested (5, 7, 9, 11, 21, 51; the midpoint waypoint is exactly singular) and pass at even N (6, 8, 10); with 72 family members every N passes Level 1. The dense reference lift has a maximum joint step of 2e-4 rad, so a continuous lift through the singular pose exists.

## Parameter-synchronous position error
`param_sync_check.py` (log: `param_sync_log.txt`, output: `results/param_sync.json`) re-runs the three methods on both paths and reports, next to the orthogonal deviation used by Level 1, the parameter-synchronous error |FK(q_I(σ)) − x(σ)| with σ = (k + j/10)/(N−1), together with the monotonicity of the progress t(σ) along the line. Over the 35 completed runs the synchronous error is at most 8.8% larger than the orthogonal deviation (regular line: 6.35 vs 5.84 mm at N = 5, 1.29 vs 1.19 mm at N = 10; wrist-crossing line, M1, N = 5: 5.65 vs 5.64 mm), progress is monotone in every run, and no Level 1 pass/fail outcome changes.
