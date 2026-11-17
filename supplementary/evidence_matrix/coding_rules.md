# Coding rules for the evidence matrix (manuscript Section 4.2)

Unit: each reference cited in the manuscript, assigned to exactly one class, then coded (class M only) on six dimensions.
Files: `matrix_coding.csv` (one row per coded reference, 100 rows), `counts_with_lists.csv` and `heatmap_cells.csv` (every number in Figure 8 with its paper list), `matrix_summary.py` (regenerates both and the figure from `matrix_coding.csv`), `excluded_R155.csv` (four earlier candidates that were removed, with reasons).

## Classes
- **M (matrix, 73 studies):** the source proposes, evaluates or analyses a method whose output is a sequence or curve of joint configurations for a prescribed end-effector path or trajectory of a serial manipulator (pathwise IK, path or trajectory tracking, redundancy resolution along a path, or solver comparisons evaluated on such paths).
- **R (review, 7):** survey, systematic review or comparative review articles.
- **B (background, 20 coded here):** single-pose IK, point-to-point or free-space planning, kinematic or singularity theory without a pathwise procedure, learning-based single-pose IK, control or dynamics without a prescribed task path.
Six further background references (the five interval-certification studies of Section 3.1 and one branch-determination study) are cited in the manuscript but are not rows of `matrix_coding.csv`; with the 20 coded background rows they make the 26 background references of the bibliography.

## Fields for class M
1. `verification`: what the source's own evaluation examines: `samples` (waypoints, nodes, grid points, time steps) | `edges_grid` (graph edges, subdivided edges, grids) | `curve` (between-sample check of the reconstructed joint curve) | `timed` (executed or timed command) | `none`. Each study carries one primary label. Figure 8a counts it.
2. `constraint_finest`: the finest object at which the source itself enforces constraints: `none` | `samples` | `edges` | `curve` | `timed`.
3. `evidence`: `none` | `simulation` | `hardware_qualitative` | `hardware_quantitative`.
4. `reconstruction_stated`: `yes` | `no` | `unverified` (does the source state how joint motion between selected samples is generated).
5. `branch`: `yes` = the source explicitly treats the choice of, or switching between, distinct IK solution branches or components along the path (discrete IK solutions, cuspidal mode changes, self-motion-manifold components, arm-angle branches). Continuous local tracking without any discrete branch treatment = `no`.
6. `singularity`: `yes` = the source explicitly avoids, damps, crosses or analyses singular configurations along the path.
7. `constraints_integrated`: `yes` = at least one inequality constraint (joint limit, velocity/acceleration/jerk bound, collision, torque) is enforced in the same procedure that produces the joint path.
8. `dynamic`: `yes` = velocity, acceleration, jerk or torque limits are part of the procedure, not only joint-position limits.
9. `real_robot`: `none` | `qualitative` | `quantitative` (hardware only; simulation = `none`).
10. `version_class`: whether the text read was the published version or an author or preprint version.
Counting never infers: any code that could not be established is `unverified` and counted separately. In the released matrix no class-M code is `unverified`.

## Evidence and procedure
- Source of codes: reading notes written from the full text of each paper. The columns `loc_*` give the place in the source (section, page, table or figure) that supports each yes/no code; `class_basis` states why the paper has its class; `flags` records low-confidence or overridden codes; `note_files` names the reading note.
- Coding was done by a single coder from the reading notes. There was no second coder and no agreement statistic.
- Override recorded in `flags`: Dulęba et al. (2018), `verification` = `none` (the evaluation examines joint-loop length, not the task error of the reconstructed curve).

## Derived counts used in the manuscript (73 class-M studies)
Verification object: samples 40, edges/grid 7 (discrete total 47), reconstructed curve 1, timed or executed 21, none 4. Branch 27, singularity 42, constraints integrated 49, dynamic limits 24, hardware 24 (8 with quantitative tracking metrics). Branch, singularity and constraints jointly: 13; of these 3 also evaluate a timed or executed motion and 2 also use hardware.
