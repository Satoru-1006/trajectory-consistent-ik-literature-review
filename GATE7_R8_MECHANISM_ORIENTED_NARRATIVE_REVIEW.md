# Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators: A Mechanism-Oriented Narrative Review

## Abstract

A sequence of valid inverse-kinematic (IK) solutions does not necessarily form a continuous, constraint-compliant joint trajectory for a prescribed Cartesian path. This mechanism-oriented narrative review examines how fixed-base serial manipulators select pathwise IK solutions, handle singularity and solution-mode events, and incorporate geometric and time-dependent constraints. It synthesizes analytical branch descriptions, sampled configuration graphs, continuation and optimization methods, architecture-dependent singular transitions, and integrated trajectory-planning systems. The comparison highlights three bounded findings: path continuation, singularity transitions, and cyclic repeatability are distinct properties; IK selection and constraint handling are already integrated in several architectures, but their results depend on the robot and task specification; and sampled feasibility, reconstructed-path verification, timed dynamic checks, and physical execution support different claims. A T1/T2/T3 comparison protocol is proposed as an analytical aid rather than a validated score; the guarantee or optimization object is recorded as a cross-cutting table column. A proposed G0/G1/G2E/G2T benchmark separates exact-path geometry, collision/event handling, exact-path timed execution, and toleranced timed processes. Because the literature sample is purposive, the search did not use authenticated database-native retrieval across Scopus or Web of Science, and the benchmark has not been executed, the findings are mechanism-level synthesis rather than estimates of field-wide prevalence or method superiority.

**Keywords:** trajectory-consistent inverse kinematics; branch continuation; singularity transitions; path constraints; time-optimal path parameterization; trajectory verification; fixed-base serial manipulators

## 1. Introduction

Inverse kinematics (IK) is often introduced as the problem of finding a joint configuration that realizes a desired end-effector pose. For a robot following a prescribed process path, however, solving each pose independently is not enough. Consecutive valid configurations can belong to incompatible solution branches, produce discontinuous joint motion, approach a singularity, or violate joint and obstacle constraints between sampled poses. The relevant engineering object is therefore not a collection of pose solutions but a joint-space realization of the path.

This distinction matters in industrial processes such as welding, spraying, grinding, deburring, and path machining, where tool motion must remain compatible with the workpiece and process tolerances. An abrupt change between inverse-kinematic branches can produce large joint-motion changes or interrupt execution; a path that is feasible only at sampled poses may still violate geometric or dynamic limits between them. These failures can degrade process quality, require replanning or operator intervention, and complicate safe deployment. Industrial robot programming and offline-programming research has long identified path generation and validation as practical bottlenecks (Pan et al., 2012; Weingartshofer et al., 2023).

Let \(f:\mathcal Q\rightarrow\mathcal X\) denote forward kinematics and let \(x(s)\), \(s\in[0,1]\), be a prescribed Cartesian path. An exact geometric lift is a continuous joint path \(q(s)\) satisfying \(f(q(s))=x(s)\). If the process permits deviation from the nominal path, the equality is replaced by an explicitly defined admissible task set \(\mathcal X_{\mathrm{task}}(s)\). Time-dependent claims additionally require a timing law \(s(t)\), a reconstruction/interpolation rule, and suitable regularity. Joint velocity and acceleration follow from
\[
\dot q=q'(s)\dot s,\qquad
\ddot q=q''(s)\dot s^2+q'(s)\ddot s.
\]
Consequently, geometric continuity alone does not establish velocity, acceleration, torque, torque-rate, collision, or controller-tracking feasibility.

Three mechanisms recur across the literature. **Pathwise solution selection** maintains a compatible sequence of configurations rather than solving poses independently. **Singularity and mode-event handling** determines whether a path should avoid a singular set, cross a permitted singular event, or move between modes without a singular crossing. **Constraint enforcement and verification** specify which geometric or dynamic conditions are imposed, on what mathematical object, and over which domain they are checked. These mechanisms interact, but they are not interchangeable: a branch-selection rule does not by itself prove collision clearance, and a time parameterizer cannot automatically repair an inadmissible geometric lift.

This review asks three questions:

1. What solution states and transition mechanisms are used to realize prescribed paths continuously?
2. How do robot architecture, task tolerance, and constraint domain change the interpretation of a method's result?
3. What evidence is needed to distinguish sampled feasibility, reconstructed-path validity, timed dynamic feasibility, and physical execution?

The contribution is a mechanism-level synthesis of selected studies, a task-conditioned interpretation of reported claims, and a proposed common-task evaluation design. It does not claim a statistically representative survey of all IK research. The focus is fixed-base serial manipulators and pathwise IK; general pose-level solvers are discussed only where they illuminate solution representation, while time-optimal path parameterization (TOPP) and sampling-based motion planning are treated as connected but distinct layers.

## 2. Research status and mechanism landscape

### 2.1. Relation to existing reviews and scope of this synthesis

Existing reviews address important but different questions. Lakshmi Narayanan et al. (2026) organize a broad serial-manipulator IK literature around model-driven and data-driven solvers, limitations, and reported performance. Xing et al. (2026) connect analytical, numerical, optimization, and AI methods with redundancy resolution and task-priority strategies. Trullo and Vivas Alban (2025) compare analytical, numerical, learning-based, and hybrid IK methods for fixed-base serial manipulators, emphasizing solver accuracy, response time, and method selection. Wenger and Chablat (2023) review the topology of cuspidal manipulators and nonsingular posture changes. Rudrasamudram and Malaichamee (2026), a non-peer-reviewed preprint, discuss formal versus empirical evidence for singularity robustness.

The present review narrows the unit of comparison from a solver family or isolated pose query to a **robot–task–path–solution–verification combination**. It asks how a method selects a compatible joint path, handles a relevant mode event, defines its constraints, and verifies the resulting motion. This emphasis complements existing solver taxonomies; it does not replace them or imply that prior reviews ignored constraints altogether.

The core evidence set concerns fixed-base serial manipulators and directly relevant claims about pathwise IK: solution selection or continuation; singularity or solution-mode events; joint, collision, derivative, or torque constraints; and reconstruction or verification of the resulting trajectory. Foundational work is retained when it establishes a mechanism needed to interpret newer methods. Adjacent studies are included only when they illuminate a relevant mechanism, and are labeled as such in Tables 1A–1B; they are not treated as evidence of prevalence or superiority for industrial serial manipulators. In particular, semi-constrained process paths, bounded-error corridors, pose-level solver evaluations, planar prototypes, and humanoid-arm studies do not automatically satisfy the core task definition. The search and selection approach is summarized in Supplementary Note S1.

| Related synthesis | Established contribution | Question emphasized here |
|---|---|---|
| Lakshmi Narayanan et al. (2026) | Broad serial-manipulator IK solver families and reported performance | How does a sequence of valid solutions become a continuous path realization? |
| Xing et al. (2026) | Redundancy resolution, objectives, task priorities, and optimization | Are constraint and execution claims made for compatible task and checking domains? |
| Trullo and Vivas Alban (2025) | Analytical, numerical, learning-based, and hybrid IK comparison | How do pose-level solver results relate to pathwise selection and event handling? |
| Wenger and Chablat (2023) | Cuspidal topology and nonsingular mode changes | When can a mode change occur without a Jacobian-singular crossing? |
| Rudrasamudram and Malaichamee (2026), preprint | Formal and empirical singularity-robustness terminology | What does each evidence type establish for the specified task? |

**Comparison framework.** T1–T3 are the only primary comparison dimensions. The guarantee or optimization object is retained as a cross-cutting annotation in Tables 1A–1B, rather than treated as a fourth dimension or a separate five-axis scheme. Evidence tags and their definitions are provided in Supplementary Note S4; they describe the scope of a reported claim and are not numerical scores.

| Dimension | Question asked of each study | What is recorded |
|---|---|---|
| **T1 — Pathwise selection and events** | What solution state is selected, and which branch, mode, or singularity events are allowed? | Branch/state representation, transition rules, path assumptions, and whether the claim is conditional or resolution-limited |
| **T2 — Constraints and domain** | Which conditions are hard constraints and which are objectives or penalties, and where are they imposed? | Joint, collision, derivative, torque, and task-tolerance conditions; nodes, edges, reconstructed segments, or timed commands |
| **T3 — Verification** | What realized object is checked, and what does that check establish? | Sampled configurations, reconstructed geometry (**T3g**), timed/dynamic execution (**T3d**), or physical tracking; T3g and T3d are subtypes of T3, not additional axes |

**How the proposed benchmark maps to T1–T3.** G0–G2T are task tiers for future evaluation, not scores assigned to the reviewed papers.

| Proposed tier | T1: path/event requirement | T2: constraint requirement | T3: verification requirement |
|---|---|---|---|
| **G0 — Geometric lift** | Exact Cartesian path and initial joint state; report any required event rule | Geometric path conditions and joint continuity; no external-obstacle claim by design | **T3g:** check the reconstructed joint path, forward-kinematics residual, continuity, and relevant events |
| **G1 — Collision/event-aware lift** | G0 requirements plus explicitly permitted event classes | Joint limits and modeled self/environment collision-clearance conditions | **T3g:** check full-link geometry along reconstructed segments at a declared resolution or with a sound bound |
| **G2E — Exact-path timed execution** | G1 path with a specified timing and controller/interpolation model | Velocity, acceleration, torque and other declared dynamic limits | **T3d:** check the actual timed command, dynamic extrema, tracking, and stated margins |
| **G2T — Toleranced timed process** | Selection within a separately specified task tube | Task-deviation bounds plus the declared dynamic and geometric constraints | **T3g + T3d:** verify the realized timed path remains within the tube and meets the declared constraints; do not rank as an exact-path G2E result |

The six mechanism anchors were selected purposively: Rakita et al. (STAMPEDE), Ferrentino et al., Elias and Wen, Boschi et al., Weingartshofer et al., and Zhang and Kikuuwe. Other rows in Table 1A are complementary cases, not additional members of the anchor set. The synthesis does not estimate field-wide method frequencies or cross-platform performance rankings.



### 2.2. Solution representation and pathwise selection

Analytical branch labels, redundancy coordinates, and sampled solution nodes describe different types of state. In an architecture-specific analytic model, a branch or posture index can explain why two joint solutions are distinct and when that description degenerates (Gong et al., 2019). Hauser and Emmons (2018) address global redundancy resolution through configuration-sheet and pseudoinverse constructions, shifting attention from a single IK query to an assignment over the task workspace. These descriptions can reveal connectivity that would be invisible to independently solved poses; they do not by themselves determine obstacle-aware timed execution. Faria et al. (2018) further illustrate architecture-aware global configuration control and joint-limit or singularity avoidance, while the pointwise global optimality investigated by Trutman et al. (2022) addresses a different object from a pathwise lift. This distinction matters even when both method classes are termed “global IK.”

STAMPEDE (Rakita et al., 2019) makes the decision pathwise by constructing layers of candidate IK configurations for successive Cartesian samples. Its graph nodes represent feasible configurations and its **edges represent legal inter-layer motion**, including joint-motion rules. Dynamic programming selects an optimum **among admissible paths in the constructed graph** (authors' §IV-A/B). Node feasibility and edge legality are both essential: reducing this method to independent pose checks would misstate its contribution. The sampling strategy is consequential because useful configurations absent from the graph cannot be selected.

Elias and Wen (2025) similarly use a sampled graph of IK solutions, with edge weights based on wrapped joint movement and the prescribed path increment (arXiv v2, §4.2, Eqs. 9–12). Their cuspidal analysis makes the nature of solution connectivity especially important: a pose may possess multiple solutions while the feasible continuous lift depends on which connected solutions are selected. The graph minimizes cost **within the represented candidates and edges**. The authors also optimize the workpiece-relative placement of a specified toolpath (§5), so their framework may change the robot-base location of the path as well as the selected joint route.

Further retained full-text evidence clarifies why "smooth" need not mean repeatable: Safeea et al. (2021) identify the cyclic-drift problem in conventional damped-least-squares IK and report a controlled cyclic scheme, including a KUKA iiwa experiment. Tringali and Cocuzza (2020) use multistart whole-trajectory optimization with constraints and cyclic-path examples; multiple numerical starts are not a general global-optimality certificate. Malhan et al. (2023) build layered configuration graphs for semi-constrained Cartesian paths and multiple tool-center-point options, so graph connectivity must be compared with the allowed task manifold rather than only with fixed-pose tracking. These sources broaden the path-state evidence beyond the six anchors. Dulęba and Karcz-Dulęba (2018) compare repeatable inverse-kinematics constructions and make a return to the initial joint configuration after a closed Cartesian circuit a separate requirement. Yoshizawa et al. (2023) use real quantifier elimination to check the existence of IK solutions for an entire parameterized path in a restricted 3-DOF model. An existence result for every path parameter does not, by itself, establish that a single continuous joint-space selection has been constructed; this distinction is mathematical, not an experimental criticism of that study.

IKLink (Wang et al., 2024), offline/online redundancy adjustment (Yin et al., 2025), and temporal multi-solution selection (Nguyen et al., 2026) add further computational perspectives. Their mechanisms are relevant to reducing reconfiguration, but an empirical preference for a nearby joint solution should not be equated with an analytic branch identifier. The useful distinction is **what state the algorithm preserves**, rather than whether all methods produce visually smooth joints.

#

### 2.3. Singularity and solution-mode transitions

A singular configuration is a rank-deficient point of a kinematic mapping; its meaning for a path depends on the robot architecture, the chosen task, and the direction of passage. Earlier continuation methods already treated such events along prescribed tool trajectories (Kieffer, 1992), while singularity-theoretic analyses distinguish the geometry of these configurations from merely numerical conditioning (Donelan, 2007; Dulęba and Karcz-Dulęba, 2023). Three responses should not be collapsed into one notion of “singularity handling.”

**Singularity-consistent tracking** may deliberately address paths for which rank loss cannot simply be avoided. Miyata, Miyahara and Nenchev (2017) propose a structure-specific right-pseudoinverse construction for a degenerate singular path, with numerical demonstrations on representative redundant limbs; the current review assessed the publisher bibliographic record and publicly indexed abstract, **not its complete mathematical proof**. Milenkovic (2022) studies path reversal and orientation deviation near an offset-wrist singularity, with a high-order predictor–corrector mechanism as described in the accessible Cambridge publisher abstract; this should not be treated as the same event or guarantee as Boschi's UR-like branch transition.

**Avoidance and regularization** restrict trajectories or numerical behavior near rank loss. They are useful when a nonsingular route exists or when modest task variation is allowed (Beck et al., 2023; Milenkovic et al., 2023). Colomé and Torras (2012) experimentally compare redundant-IK methods and introduce Jacobian singular-value filtering together with continuous task-priority and selective-damping enhancements, improving numerical behavior and motion smoothness in WAM experiments. Such regularization and task-execution mechanisms address a different question from the admissibility of a specified solution-branch transition. Avoidance can also exclude a necessary exact-path crossing, so success depends on whether the toolpath may move.

**Nonsingular mode change** can occur in suitable cuspidal manipulators. Wenger and Chablat (2023), Salunkhe et al. (2025), and Elias and Wen (2025) distinguish such topology from a passage through Jacobian rank loss. The route and its existence conditions are architecture-dependent. In Elias and Wen's graph construction, restricting edges to retain the sign of \(\det J\) can enforce a *sampled nonsingularity policy*; allowing graph connections across sign changes does not alone prove the regularity of every interpolated configuration (arXiv v2, §4.2).

**Singular crossing with a branch transition** is the target of Boschi et al. (2026) for UR-like non-cuspidal structures. The authors factor the Jacobian determinant into posture-related factors (published §II-B, Eqs. 13–14) and associate the signs with branch indices. When an admissible task path passes through a singular configuration, the appropriate post-event branch can differ from the pre-event branch. Their §III-A derives a threshold using the change in singularity factors between sampled commands (Eqs. 15–17); Algorithm 1 selects candidate branches and treats wrist singularity degeneracy. The threshold is a **switching/detection mechanism**, not a certification of joint-velocity bounds merely because maximum joint velocity appears in its derivation. In §IV, UR5e peg-in-hole and pick-and-place cases demonstrate the intended continuous joint evolution, while the paper conditions applicability on **kinematically admissible** paths (Conclusion). This is a specific solution to event-conditioned kinematic selection rather than a generic collision or dynamic-feasibility algorithm.

These distinctions lead to a task-conditioned decision: can the path remain within a nonsingular solution domain, can the architecture support a nonsingular mode change, or is an admissible singular crossing with a specified event law required? Boschi et al. (2026) demonstrate an architecture-conditioned mechanism for maintaining joint-path continuity through kinematically admissible singularity events. Its comparison with avoidance and cuspidal-mode transitions therefore depends on robot topology and the prescribed path.

#

### 2.4. Geometric, dynamic, and process constraints

The physical meaning of constraints depends on their variables and verification domain. Joint position can be bounded during geometric IK construction. Joint velocity, acceleration, jerk, torque and torque rate require a timing law and model approximations. Obstacle clearance depends on the occupied geometry of every relevant link along the path, not merely on end-effector pose. Collision-aware continuation was already an explicit IK consideration in Müller (2004); newer constrained formulations make different tradeoffs between geometry, dynamics and computational scope.

Ferrentino et al. (2024) integrate redundancy resolution and time-related limits in dynamic programming. Their **§II-B, Eqs. (17)–(22)** encode admissible states, joint velocity/acceleration/jerk and torque/torque-rate bounds; Algorithm 1 evaluates transitions on a finite discretization. The paper reports experiments on the Franka Emika Panda (§IV). This integrates choices often separated into geometric planning and retiming, but the optimized object remains discretized; the authors also note that checking some higher-order constraints without augmenting state can compromise an unrestricted global-optimality interpretation (§III). Physical execution supports the reported hardware case, not an all-interval certificate for arbitrary controller conditions.

Zhang and Kikuuwe (2026) address differential IK through an auxiliary discrete-time viability construction (§2.1–2.3). Their Lemma 1 and modeled joint and collision inequalities provide feasibility reasoning for the stated discrete model. This is stronger than merely placing soft penalties in a tracking cost, while remaining distinct from a continuous-time swept-volume or torque-bound verification. Their simulations examine the specified discrete scheme, without transferring the result to an unmodeled actuator or environment.

Weingartshofer et al. (2023) formulate manufacturing-process-toleranced joint-path optimization with distinct **hard joint-position bounds (Eq. 13b)**, a **collision inequality (Eq. 37)**, and **soft penalties** for clearance (Eq. 36), neighboring-joint motion (Eq. 40), and joint-limit proximity (Eqs. 42–44). The method permits specified position/orientation deviations and singular passage, reconstructs paths using cubic Hermite segments (§5.5), and evaluates KUKA LBR iiwa drawing on hardware and KUKA KR8 spraying in simulation (§6). Its application evidence illustrates how process tolerances, constraint formulations, and reconstruction define the relevant motion; checking continuous swept-link clearance and timed dynamics would require corresponding additional verification.

Patkó and Zelei (2021) compare velocity- and acceleration-level IK implementations and analyze numerical stability under their stated discretization assumptions; their publisher article is openly available and was inspected here. Their analytical convergence and step-size domains should not be read as collision, torque or branch-event certification. Li and Wang (2024) propose a combined obstacle–singularity–joint-limit avoidance controller based on projected gradients and weighted damped inverses, with simulation on a reduced-DOF redundant configuration. Their publisher full article explicitly notes that singularity and joint-limit avoidance introduce end-effector tracking error. This is positive *multi-constraint avoidance* evidence, not a singular crossing rule or whole-trajectory swept-volume certificate. Oelerich et al. (2025) take a different approach in BoundMPC, using Cartesian path-error windows in joint-space MPC; allowing bounded task deviation expands the feasible task specification rather than proving feasibility of the unrelaxed exact path.

Positive integrative studies extend this account. Zhang and Wang (2025) build redundancy-based, task-constrained, collision-aware motion connections for a 7-DOF robot and report simulations and tests, but an admissible task manifold is not automatically identical to an exact prescribed six-dimensional pose curve. Oelerich et al. (2025; *BoundPlanner*) combine bounded free-space convex corridors with a collision-aware joint-space model-predictive planner in a 7-DOF setting. Permissible path variation changes the task specification, and Cartesian corridor feasibility should not silently be called exact-path IK-lift certification. These cases are evidence of integration rather than evidence of a missing combination.

Additional constrained numerical approaches include higher-order IK and time-optimal multiple shooting (Reiter et al., 2018), dynamic joint bounds (Faroni et al., 2020), inequality-constrained real-time IK (Zhang et al., 2024), and model-predictive constrained differential kinematics (Reinhold et al., 2023). They broaden the architectural options for an integrated system, but their constraint objects should be compared against what they actually formulate and demonstrate, not credited with an unspecified branch-event theorem.

#

### 2.5. Scope boundaries: timing, constrained planning, learning, and offline programming

Time-optimal path parameterization (TOPP) and constrained sampling-based planning are connected but distinct layers. TOPP assumes a geometric path and computes a timing law under dynamic constraints; constrained sampling-based planning concerns how constraint-satisfying configurations and motions are generated (Kingston et al., 2018). Neither, by itself, establishes that a prescribed Cartesian path has a compatible continuous IK lift. TOPP methods are therefore discussed where they clarify the boundary between geometric path feasibility and timed execution, rather than surveyed as a separate field. Pham (2014) and Pham and Pham (2017, 2018) describe important TOPP formulations, including reachability analysis and third-order constraints; Huang et al. (2023) specifically study sampling-based time-optimal path parameterization for robotic manipulation with bounded jerk. This is a timing-layer contribution, not a substitute for pathwise IK selection.

Continuation and homotopy-related methods also have a substantial history in manipulator kinematics. Kieffer (1992), Müller (2004), Donelan (2007), and Hauser and Emmons (2018) provide representative foundations for untimed trajectory IK, collision-avoiding continuation, singularity-theoretic analysis, and continuous redundancy resolution. They are cited to position the mechanisms discussed here; this review does not attempt an exhaustive historical taxonomy of continuation or homotopy algorithms.

Learning-based IK is another adjacent family. Trullo and Vivas Alban (2025) review analytical, numerical, and machine-learning approaches, while Nguyen et al. (2026) examine permutation-invariant prediction of multiple IK solutions. Such work is relevant to branch representation and candidate generation, but pose-level or set-prediction performance is not treated as evidence of continuous path validity unless pathwise selection and the corresponding verification domain are assessed. The non-peer-reviewed review by Rudrasamudram and Malaichamee (2026) is used only as contextual discussion of evidence claims.

Finally, commercial offline-programming (OLP) systems are important in industrial deployment, especially for welding and machining, but this article does not benchmark individual vendor platforms. Product-level features are not consistently documented in a form that exposes comparable mathematical assumptions, constraint domains, and verification guarantees. Industrial programming methods are included as application context (Pan et al., 2012), while a comparative evaluation of commercial OLP software remains outside the present scope. These are deliberate scope boundaries, not claims that the excluded literatures are unimportant.

## 3. Key methodological controversies

The following are technical disputes about assumptions and evaluation, not claims that the field has reached a single formal controversy or consensus on every point. Published studies often solve different tasks; apparent disagreement can disappear once the task and evidence domain are made explicit.

### 3.1. Is sampled feasibility sufficient to claim a valid continuous trajectory?

Graph nodes, graph edges, controller steps, and reconstructed continuous segments are different mathematical objects. A path whose sampled configurations satisfy joint limits and collision checks may still have an interpolation that violates a limit between samples. Conversely, finite-resolution checking can be appropriate for a method whose claim is explicitly restricted to the discrete model. The disagreement is therefore not whether sampling is useful, but whether the evidence is being used to support a stronger claim than the method checked.

STAMPEDE's legal graph edges and Ferrentino et al.'s discretized dynamic-programming transitions support claims about the represented graph or discretization. Weingartshofer et al.'s reconstructed Hermite path creates a different object to validate. A system claiming continuous execution should specify the actual interpolant or controller command and check that object at a declared resolution or with a sound bound. This is a verification requirement, not evidence that a named study necessarily experienced an inter-sample failure.

### 3.2. Should singularities be avoided, crossed, or traversed through a nonsingular mode change?

These strategies optimize for different task conditions. Avoidance is appropriate when a feasible nonsingular route exists or task deviation is permitted. A cuspidal robot may admit a nonsingular mode change because of its configuration-space topology. A non-cuspidal robot following a fixed, admissible path may instead require an explicit singular-event transition rule. None is universally superior: the relevant choice depends on the robot's architecture, the prescribed path, the allowed task deviation, and the continuity/regularity property required.

A comparison that ranks these approaches without freezing those conditions risks comparing different feasible sets. The proper question is whether a method's preconditions match the intended application and whether its reported evidence supports the specific event claim.

### 3.3. Can exact-path and toleranced-path results be compared directly?

An exact Cartesian path fixes the required end-effector pose at each path parameter. A semi-constrained path may permit orientation freedom; a bounded-error corridor permits a specified deviation; workpiece-placement optimization may move the robot-relative location of a nominal process path. These are distinct problem formulations, not interchangeable implementation details.

Tolerances can make a process feasible where an exact path is not, but a toleranced-path success cannot be reported as an exact-path success. Likewise, a workpiece-placement variable must be declared rather than silently treated as fixed-frame IK. Meaningful comparisons therefore require the feasible task set, initial joint state, robot model, obstacle scene, and timing assumptions to be frozen in advance.

### 3.4. Does integration of IK and constraints imply end-to-end verified motion?

The reviewed literature includes genuine integration: graph-based selection with geometric filtering, kineto-dynamic planning, task-constrained redundancy resolution, collision-aware optimization, and predictive control with bounded path error. It would be inaccurate to claim that IK selection and constraint handling are generally absent from integrated systems.

However, the presence of modules does not automatically make their claims compositional. If one module selects a solution under model \(M_A\), another reconstructs or retimes a modified path, and a verifier checks a different object under model \(M_C\), system-level feasibility follows only if the relation between these objects and assumptions is established. This does not require literal byte identity: a justified approximation or robustness bound can connect them. What is required is a traceable link between the task, selected solution, reconstructed path, timed controller command, and claim-specific verification.

### 3.5. Where does IK end and time parameterization begin?

Geometric path selection and timing are conceptually separable, but their constraints interact. TOPP generally parameterizes a given path under dynamic limits; pathwise IK determines whether a compatible joint path exists in the first place. A discontinuous or inadmissible joint path cannot be made valid simply by assigning it a time law. In the other direction, geometric continuity alone does not establish that a timing law satisfies joint-velocity, acceleration, torque, jerk, or torque-rate bounds.

TOPP-RA uses reachability analysis to parameterize a specified path under modeled dynamic constraints (Pham and Pham, 2018), while TOPP3 addresses third-order constraints such as jerk and torque rate (Pham and Pham, 2017). Sampling-based TOPP has also been studied for jerk-bounded manipulation (Huang et al., 2023). These are relevant to timed execution but do not replace IK branch selection. An integrated pipeline may alternate path selection and timing or feed dynamic infeasibility back into path selection; it should state which stage owns each constraint and which final object is checked.

## 4. Research progress: cross-study synthesis

### 4.1. Cross-study evidence matrix

**Table 1A** compares studies for which the reviewed source provides detailed methodological or experimental material. The rows are a purposive mechanism sample, not a representative survey or performance ranking. **Table 1B** separately records three 2026 studies available here only through publisher abstracts or previews; these records are contextual leads and are excluded from the evidential basis of Findings F1–F3. Source depth indicates what was actually inspected, not an inferred level of scientific quality.
| Case: robot/task | T1: selected object, event, scope | T2: enforced/optimized constraint and domain | T3: checked realization and evidence | Claim/optimization object | Source depth / inference limit |
|---|---|---|---|---|
| **Rakita et al. (2019), STAMPEDE**, multiple manipulators | Layered sampled IK graph; admissible edges and finite-graph optimum; crossing theorem **N** | Legal nodes/edges and modeled collisions at graph resolution; **R** | Numerical multi-robot comparisons **D**; continuous swept extrema **U** | Optimum among represented graph paths only; not a continuous-path certificate | Author full PDF; finite graph is not continuous-path certification |
| **Ferrentino et al. (2024)**, redundant Panda | Finite redundancy/trajectory-state DP; conditional aspect restrictions; **C/R** | Joint positions, higher derivatives, torques and torque-rate in discretized transitions; hard modeled conditions **R** | Panda planning and hardware tracking **D**; all-interval extrema **U** | Discrete DP optimum under modeled kineto-dynamic constraints; no all-interval certificate | Institutional accepted full PDF; discretized global result only |
| **Elias and Wen (2025)**, cuspidal 6R path | Sampled all-IK graph; nonsingular cuspidal connections/optional singular edges; **C/R** | Graph movement/time edges; environmental collision not a checked central task (**N**) | Numerical path/workpiece offset examples **D**; hardware **U** | Lowest-cost path within the sampled IK graph and chosen edge policy; depends on graph resolution and robot topology | Author arXiv v2 technical sections, journal equation mapping **U** |
| **Boschi et al. (2026)**, UR-like robots/UR5e | Sign/posture-index switch at selected, kinematically admissible singular events; **C** | Kinematic event thresholds **D**; dynamic/collision certificate **N** to main claim | UR5e peg-in-hole/pick-and-place hardware **D**; generic interval safety **U** | Architecture- and path-conditioned event-switch rule; not a generic dynamic or collision guarantee | Published article technical sections and experiments |
| **Weingartshofer et al. (2023)**, iiwa drawing/KR8 spraying | Multi-start optimized joint paths; selected singular passages allowed **C** | Hard joint bounds/collision model inequalities; separate movement/clearance penalties; toleranced process path **D** | Cubic-Hermite reconstruction, iiwa hardware drawing, KR8 simulation **D**; swept extrema **U** | Multi-start joint-path objective with hard inequalities separated from soft penalties; global optimum not established | Published article sections/equations; do not conflate penalties with hard constraints |
| **Zhang and Kikuuwe (2026)**, discrete QP IK | Differential local update; special branch event **N** | Joint range/velocity/acceleration and approximate full-body collision in modeled discrete-time viability constraints **R** | Numerical simulations **D**; inter-step physical/continuous certificate **U** | Discrete-time viability claim under modeled inequalities; continuous-time physical certificate not established | Published-author copy, lemma and equations, not hardware |
| **Malhan et al. (2023) [Adjacent: semi-constrained path]**, semi-constrained process path | Layered/multilayer configuration-path selection with admissible tool-frame sets **C/R** | Tool-frame freedom and graph-level transition criteria; continuous swept safety **U** | Published numerical evaluations **D**; hardware on a common platform **U** | Graph/path selection within a semi-constrained tool-frame set; not equivalent to exact-pose IK | Historical full-text log and publisher metadata; not exact-pose task |
| **Oelerich et al. (2025) [Adjacent: bounded-error corridor]**, BoundPlanner, 7-DOF | Collision-free convex-set reference corridor + joint-space BoundMPC path following; branch-index event **N** | Convex corridor/path-error bounds and chain-collision constraints in predictive formulation **D** | Simulations and 7-DOF experiments **D**; exact-path and universal interval certificate **U** | Predictive bounded-error corridor and path-following objective; the tolerance corridor changes the task set | Peer-reviewed RA-L / university record / archived reading, not a UR5e head-to-head |
| **Peidro and Haug (2024)**, redundant 6/23-joint models | Differentiable configuration-manifold continuation in regular-domain examples; event crossing **N** | Obstacle avoidance in operational configuration domain **D**; positive clearance across arbitrary continuous intervals **U** | Numerical 4-/20-redundancy demonstrations **D**; hardware **U** | Manifold-based obstacle-aware continuation in the modeled operational configuration space; no arbitrary global-clearance proof | Open published full HTML + archived read log; model/step specific |
| **Malik et al. (2021)**, 7-DOF Sawyer | Sequential swarm-based joint-path generation; branch identity/event proof **U** | Weighted pose/effort/collision objective at path samples **R**; collision indicator is **not** an all-link swept certificate | Sawyer trajectory/hardware torque evaluation **D**; unsampled collision **U** | Weighted sampled trajectory objective; collision indicator is not a swept-link certificate | Open published full HTML + archived full-text notes |
| **Kelemen et al. (2018) [Extension: planar/prototype]**, planar 5R/20R and small prototype | Warm-start DLS sequential IK; singularity regularized/avoided, not a crossing rule (**N**) | Weighted joint-limit/obstacle objectives (**soft**) **D**; hard joint-bound path certificate **U** | Simulations and small 5R servo experiment **D**; cyclic repeatability **N** | Sequential DLS/local regularized solution; no global or cyclic guarantee | Open publisher page + archived read log; not evidence for industrial all-time bounds |
| **Caballero-Mora et al. (2026) [Adjacent: pose-level benchmark]**, UR3 full-pose IK benchmarks | Multiple metaheuristics/LM compared at poses; representative multi-pose tracking has empirical sequential stability, **not** a branch-continuity theorem | Smooth Jacobian-conditioning **penalty**, not a full swept-trajectory hard safety specification **U** | Statistical pose-level trials, RoboDK and selected real-UR3 multi-pose tests **D**; continuous-time safety **U** | Pose-level solver comparison plus empirical multi-pose tests; not a continuous path-lift theorem | Open published *Applied System Innovation* HTML + archived reading log; method-comparison validation, not certified path lift |
| **Y. Zhang et al. (2026) [Adjacent: sampled industrial graph planning]**, FANUC M-20iA grinding simulation | Sampled pose-graph/A* with configuration filtering; **R** | GJK-style clearance and joint/singularity tests in sampled modeled evaluation; continuous link sweep **U** | Author-reported simulation **D**; clearance/path-cost trade-off below | A* graph cost with sampled clearance filtering; clearance improvement does not establish swept safety or universal path-cost superiority | Published *Machines* HTML methods/results inspected |

**Table 1B. Abstract/preview-only candidates (contextual evidence; not used to support F1–F3)**

| Case: robot/task | T1: reported mechanism | T2: reported constraints | T3: validation stated | Claim/optimization object | Source depth / unassessed claims |
|---|---|---|---|---|
| **Zeng et al. (2026) [Extension: humanoid arm]**, SRS-like 7-DOF humanoid arm | Arm-angle interval continuity within a posture branch; near-singularity traversal reported; **C** | Velocity/acceleration limit enforcement via look-ahead bisection retiming/finite horizon **R** | Humanoid-platform experiments reported **D**; full theorem, exact interval guarantee and other-robot transfer **U** | Abstract-reported interval-continuity/retiming claims; full theorem and exact guarantee not assessed | **IEEE abstract/publisher metadata only**; reported T1/T2 claims not independently verified |
| **M. Zhang et al. (2026)**, offset-free 7-DOF | Arm-angle analytic selection, boundary/singularity handling reported **C** | EWMA smoothing and kinematic boundary selection; full hard-constraint equations **U** | Simulations in publisher description **D**; interval certificate **U** | Abstract-reported arm-angle selection and smoothing; hard-constraint object not assessed | **Publisher abstract/preview only** |
| **Milenkovic et al. (2026)**, serial robot near singularity | Alternative IK solutions from singularity encircling reported **D**; topology/event conditions **U** | Collision/dynamic claim **N** to inspected summary | Published theorem/evaluation detail **U** | Abstract-reported singularity-encircling IK alternatives; theorem and event assumptions not assessed | **Publisher abstract/metadata only**; older SSRN not presumed journal-identical |



**Tables 1A–1B interpretation.** Evidence tags are defined in Supplementary Note S4. **U** means unassessed in the source material inspected, not a failed study. A reported hardware experiment does not imply a theorem. Similarly, a graph or controller paper's failure to examine a singular crossing is not negative evidence unless it claims that event.

### 4.2. Three bounded findings from the evaluated cases

The following findings summarize the selected mechanisms; they are not estimates of prevalence across the full IK literature.

**Finding F1 — continuation/event/repeatability form distinct properties.** STAMPEDE's edge-connected finite candidate graph (Rakita et al., 2019), the conditional singular transition of Boschi et al. (2026), and cuspidal nonsingular graph transitions of Elias and Wen (2025) answer different path-lifting questions. Safeea et al. (2021) and Dulęba and Karcz-Dulęba (2018) additionally study cyclic return, which does not follow from open-path continuity. Thus a conventional solver-family label or a generic "smooth" score cannot order these results along one axis.

**Finding F2 — integrated methods exist, but their feasible sets are not interchangeable.** Ferrentino et al. combine redundancy planning with discretized kineto-dynamic constraints; Weingartshofer et al. combine process-toleranced manufacturing paths with joint and collision constraints; STAMPEDE and Y. Zhang et al. use graph transitions with geometric filtering; BoundPlanner combines bounded-error corridors with predictive collision handling; Malik et al. include collision and effort objectives in trajectory generation; and Peidro and Haug study manifold-based obstacle-aware continuation. These examples refute a blanket claim that IK selection and constraint handling are never integrated. They do not establish a common ranking: exact Cartesian poses, semi-constrained tool frames, bounded-error corridors, and workpiece-placement optimization define different feasible sets. The three abstract-only studies in Table 1B are not counted as decisive evidence for this finding.

**Finding F3 — T2 enforcement and T3 evidence establish different claims depending on domain.** A legal graph edge, hard optimizer inequality, approximate discrete-time viability condition, and experimental trajectory-tracking result establish different propositions (Rakita et al., 2019; Weingartshofer et al., 2023; Zhang and Kikuuwe, 2026; Ferrentino et al., 2024). The collision-distance/path-cost example in Y. Zhang et al. (2026) further shows that optimizing one geometric criterion can worsen another path-cost metric. These results motivate checking the **same reconstructed and timed motion**, but they do **not** establish that the cited papers actually experienced inter-sample failure.

**Author-reported quantitative trade-off, not a common benchmark:** Y. Zhang et al. (2026), *Machines* Table 3, report for one simulation scenario standard A* versus enhanced method search time **0.57 vs. 0.48 s**, minimum modeled distance **8.4 vs. 50.2 mm**, and joint-path cost **21.85 vs. 24.32**. Improved modeled clearance and increased path cost are both preserved; no independent replication, physical validation or swept-volume safety proof follows.

**Evidence-depth boundary.** Zeng et al. (2026), M. Zhang et al. (2026), and Milenkovic et al. (2026) are listed separately in Table 1B because only abstracts or publisher previews were assessed. Their complete mathematical assumptions and verification domains remain unassessed, and they are excluded from the evidence supporting Findings F1–F3. Rudrasamudram and Malaichamee (2026) is a non-peer-reviewed preprint and is cited only to clarify the originality boundary of guarantee terminology. No field-wide prevalence or cross-platform superiority is inferred.

## 5. Future outlook

The next step is not to add another universal solver taxonomy, but to test the interfaces that the evidence matrix leaves unresolved. Priorities are to formalize event semantics and cyclic conditions; verify the reconstructed and timed motion rather than only intermediate planning objects; and compare methods under explicitly frozen exact or toleranced task specifications. The benchmark below is a proposal for future work, not an experiment reported by this review.

### 5.1. A proposed common-task benchmark: G0/G1/G2E/G2T

The cross-study comparison motivates a common-task measurement design using a fixed-base **UR5e 6R** cell, for which UR-like branch/event behavior has been explicitly studied. This is a **proposed protocol**: model files, trajectories, controller assumptions, and validation settings must be fixed and published before comparative runs. No common-robot experiment has yet been performed.

**Shared task dossier (minimum required input).** Publish (a) the full robot/URDF and kinematic convention, joint limits, tool, workpiece frame and TCP calibration; (b) a parameterized Cartesian path with full pose and orientation, path direction, units and start/goal; (c) an initial joint state and accepted final-state/cyclic conditions; (d) a complete collision scene, self-collision pair policy, attached tool geometry, safety margin and swept-check precision; (e) process tolerances, if any, with a metric for position and orientation deviation; (f) payload, inertial/friction assumptions, controller update period, interpolation and timing freedom; (g) all solver seeds, stopping rules, computation budget and numerical tolerances. A **separate corpus** should specify regular, singular-event and potentially infeasible paths; feasibility labels cannot be presumed in advance.

**Task variants and proof/checking obligations:**

| Variant | Frozen task definition | Passing evidence for this particular benchmark | Invalid equivalence to avoid |
|---|---|---|---|
| **G0 — geometric lift** | Exact fixed-frame full-pose \(x(s)\), specified \(q(0)\); no external obstacles by design | Provide continuous or explicitly piecewise admissible reconstructed \(q(s)\); check FK error, joint continuity, and any required event across the **reconstruction**, not only pose nodes | Multiple valid IK samples do not prove an admissible lift |
| **G1 — collision- and event-aware lift** | Same exact \(x(s)\) and initial state, plus full modeled self/environment geometry, clearance margin and any permitted event class | G0 obligations, full-link clearance on reconstructed segments at a declared geometric resolution or sound bound, and evidence for every claimed event precondition and successor | Collision-free nodes alone do not imply collision-free interpolation |
| **G2E — exact-path timed execution** | The exact G1 path specification with payload, dynamic limits, timing/interpolation/controller model | G1 obligations plus appropriately checked \(\dot q,\ddot q,\tau\), tracking and runtime against declared error/margin limits on the final timed command | Geometric consistency does not imply timed or torque feasibility |
| **G2T — *toleranced* timed process** | A separately frozen admissible task tube \(\mathcal X_{\mathrm{task}}(s)\) and dynamic settings | Valid joint lift **inside the announced tube**, geometry/dynamic checks on the realized timed motion, deviation reports and abort logic | Relaxed G2T success must **not** be ranked as G2E exact-path success |

G2E is deliberately distinguished from G2T: the latter changes the admissible task and need not be a strict superset in every constrained design. A workpiece-frame optimization must also be reported as a **separate variable**, not smuggled into an exact fixed-frame variant.

**Comparable execution protocol.** Each method receives exactly the versioned task dossier and equal solver-resource reporting. Its output is recorded as \(q_{\mathrm{selected}}\), the **actual interpolated** \(q_{\mathrm{realized}}(s)\), timing \(s(t)\) when applicable, allowed/encountered event records, and any controller-resampled command. Validation must use these outputs **with consistent model version, joint/obstacle geometry and tool frame**. Report completion/feasibility, task residual (and maximum tube deviation), discontinuities or failed event transitions, minimum modeled link clearance, extrema of joint position/velocity/acceleration/torque, computation budget and hardware tracking if available. If a method cannot represent an imposed problem (e.g., a 7-DOF arm-angle method on UR5e), report it as **not applicable to that robot** rather than as zero success.

**Stop and outcome semantics.** Prespecify termination for solver budget/time-out, IK infeasibility at exact or toleranced poses, an inadmissible branch/singularity event, geometric collision/clearance failure, joint/time/dynamic-limit violation, controller-tracking abort, and numerical/model inconsistency. Report outcomes in plain language: success checked at the stated resolution; success with sound interval bounds (only when such bounds are produced); infeasibility with a valid proof; no solution found within budget; verifier rejection; execution abort; not applicable; or not assessed. A time-out is not proof of infeasibility, and an unassessed requirement is not a failure. Every claimed certificate must identify its mathematical domain and assumptions.

Existing UR5e, Panda, iiwa, KR8, FANUC, and 7-DOF platform studies use distinct robot and task conditions; their published outcomes cannot populate a common-dossier comparison. The proposed G0/G1/G2E/G2T benchmark provides a common-task design for evaluating path continuity, admissible transitions, constraint satisfaction, and verification of reconstructed joint trajectories under explicitly defined robot and task conditions; its pass/fail outcomes remain unfilled because the benchmark has not been run.

#

### 5.2. Event semantics and cycle-sensitive continuation

**Observed contrast:** sampled graph connectivity (Rakita et al., 2019), architecture-conditioned UR-like singular switches (Boschi et al., 2026), and cuspidal nonsingular mode changes (Elias and Wen, 2025) cannot be collapsed into one kind of branch continuity; Safeea et al. (2021) additionally study repeatable closed-loop IK. **Research requirement:** log incoming/outgoing solution state, admissibility of the event, regularity and whether a closed Cartesian circuit returns to the initial joint state. Unknown switching feasibility must produce an explicit rejection rather than an invented uninterrupted path.

### 5.3. Reconstructed-trajectory verification and checking domains

**Observed contrast:** discrete QP viability (Zhang and Kikuuwe, 2026), sampled graph collision tests (Rakita et al., 2019; Y. Zhang et al., 2026) and nonlinear hard constraints plus Hermite reconstruction (Weingartshofer et al., 2023) refer to different intermediate mathematical objects. **Research requirement:** report the real interpolant, controller step, link pairs, model, checking resolution/validated interval bounds, and time-domain extrema. Inter-sample checks should be evaluated as additional system-level evidence rather than demanded from a geometric paper whose goal is not continuous-time certification.

### 5.4. Fair comparisons of exact-path and task-toleranced systems

**Observed contrast:** Weingartshofer et al. accept specified process tolerances, Malhan et al. admit semi-constrained poses, BoundPlanner supplies bounded Cartesian corridors, and Elias and Wen optimize workpiece placement. **Research requirement:** benchmark these task freedoms as **distinct variants**, preserve the feasible-set definition, and explicitly flag 6R versus 7-DOF structural mismatch. The proposed G0/G1/G2E/G2T benchmark in Section 5.1 defines a candidate experiment but has not been executed.

### 5.5. An applicability-aware minimum reporting contract

| Capability actually claimed | Fields necessary to interpret or reproduce that claim |
|---|---|
| Continuous or sampled IK selection | Robot/DOF, exact versus toleranced task, start state, solution-state representation, sample and reconstruction map, path residual |
| Branch/singularity event | Event type, robot-specific topology/structural preconditions, pre/post state, admissibility rule, junction regularity, abort response |
| Collision-constrained motion | Hard inequality versus penalty, self/environment model and excluded pairs, sample/edge/interpolant domain, margins and resolution |
| Timed dynamic feasibility | Controller command and \(s(t)\), payload/model, derivative and torque limits, checked extrema and interval/discrete assumptions |
| Hardware evidence | Robot, calibration, task and controller settings, execution/abort record, measured versus planned motion, tracking error and transfer restrictions |
| Evidence provenance | Identify the source type and whether evidence is theoretical, simulated, or experimental; state plainly when a requirement is outside scope or has not been assessed |

These are **reporting recommendations illustrated by the reviewed cases**, not a validated standard or an experimentally verified T1/T2/T3 scoring rubric. A meaningful future test would preregister inter-rater coding rules and independently assess agreement on a larger, prospectively sampled literature set.

### 5.6. Targeted verification priorities

Further source checks should prioritize the complete mathematical assumptions and experiment settings of Zeng et al. (2026), M. Zhang et al. (2026), and Milenkovic et al. (2026), together with archived papers flagged by the 62-record triage for potential impact on cross-study interpretation. Broader database-native retrieval and citation chaining could expand the comparison, while shared-robot tests would evaluate whether the proposed T1/T2/T3 reporting criteria discriminate reliably among methods. These are specific evidence-development priorities arising from the current synthesis.

## 6. Method note and conclusion

### 6.1. Method note and limitations

This is a **mechanism-oriented narrative review using limited structured retrieval**, not a systematic review or meta-analysis. The search used 17 targeted queries on the Consensus platform, supplemented by focused public-web searches and inspection of relevant publisher pages. It did not include authenticated database-native retrieval from Scopus or Web of Science, exhaustive citation chaining, or independent full-text assessment of every potentially eligible study. Eligible core studies address pathwise IK for fixed-base serial manipulators, including solution selection/continuation, singularity or mode events, constraint enforcement, or trajectory-level verification. Adjacent studies are included only to clarify a mechanism or scope boundary. The six main mechanism anchors were selected purposively and are not a statistically representative sample.

Three studies available only through abstracts or publisher previews are separated in Table 1B and are not used as decisive support for Findings F1–F3. No independent second-coder pass or inter-rater agreement statistic has been completed; the proposed protocol is described in Supplementary Note S4 but remains to be performed. The common-task benchmark has not been executed. Accordingly, T1–T3 is a transparent analytical framework, not a validated scoring instrument, and the findings are limited to the mechanisms and sources examined.

### 6.2. Conclusion

For industrial path processes, a defensible IK result must connect the task specification to a selected joint path and then to the geometry and timed motion that will actually be executed. The reviewed studies show why branch continuity, event handling, constraint enforcement, and execution evidence must be reported separately rather than compressed into a single solver-performance label.

The immediate research priority is a staged, reproducible validation workflow: define the exact or toleranced task; state the permitted solution and singularity events; distinguish hard constraints from penalties; reconstruct the commanded joint path; check geometric and collision conditions on that reconstruction; and only then assess timing, dynamic limits, and physical tracking. The proposed G0/G1/G2E/G2T protocol organizes these obligations, but remains a design proposal until its tasks, models, and evaluation rules are frozen and tested. Future studies should prioritize independent coding of the selected literature, common-task comparisons on a shared robot, and explicit reporting of the resolution and assumptions behind every guarantee. No universal method ranking follows from the present purposive sample.

## Data availability statement

The search approach, eligibility rules, evidence-extraction fields, and source locators are documented in Supplementary Notes S1–S4. The review materials associated with this article are available at the project repository: https://github.com/Satoru-1006/trajectory-consistent-ik-literature-review. The repository materials document this narrative review and should not be interpreted as an exhaustive systematic-review dataset.

## References

Beck, F., Vu, M. N., Hartl-Nesic, C. and Kugi, A. (2023). Singularity avoidance with application to online trajectory optimization for serial manipulators. *IFAC-PapersOnLine*, 56(2), 284–291. https://doi.org/10.1016/j.ifacol.2023.10.1582

Boschi, I., De Toni, A., Di Leva, R., Ida, E. and Carricato, M. (2026). Handling transitions across singularities for UR-like serial robots. *IEEE Robotics and Automation Letters*, 11(3), 2714–2721. https://doi.org/10.1109/LRA.2026.3653295

Caballero-Mora, J. A., Sanin-Villa, D., Girón-Nieto, H., Botero-Gómez, V., Portillo-Vélez, R. J., López-Romero, J. C. and Tejada, J. C. (2026). UR3 collaborative robot inverse kinematics using metaheuristic optimization: A unified comparative and experimental evaluation. *Applied System Innovation*, 9(7), 140. https://doi.org/10.3390/asi9070140

Colomé, A. and Torras, C. (2012). Redundant inverse kinematics: Experimental comparative review and two enhancements. In *2012 IEEE/RSJ International Conference on Intelligent Robots and Systems*, 5333–5340. https://doi.org/10.1109/IROS.2012.6385672

Donelan, P. S. (2007). Singularity-theoretic methods in robot kinematics. *Robotica*, 25(6), 641–659. https://doi.org/10.1017/S0263574707003748

Dulęba, I. and Karcz-Dulęba, I. (2018). A comparison of methods solving repeatable inverse kinematics for robot manipulators. *Archives of Control Sciences*, 28(1), 5–18. https://doi.org/10.24425/119074

Dulęba, I. and Karcz-Dulęba, I. (2023). Many faces of singularities in robotics. *Pomiary Automatyka Robotyka*, 27(1), 19–26. https://doi.org/10.14313/par_247/19

Elias, A. J. and Wen, J. T. (2025). Path planning and optimization for cuspidal 6R manipulators. *Journal of Mechanisms and Robotics*, 17(12), 121008. https://doi.org/10.1115/1.4069599

Faria, C., Ferreira, F., Erlhagen, W., Monteiro, S. and Bicho, E. (2018). Position-based kinematics for 7-DoF serial manipulators with global configuration control, joint limit and singularity avoidance. *Mechanism and Machine Theory*, 121, 317–334. https://doi.org/10.1016/j.mechmachtheory.2017.10.025

Faroni, M., Beschi, M. and Pedrocchi, N. (2020). Inverse kinematics of redundant manipulators with dynamic bounds on joint movements. *IEEE Robotics and Automation Letters*, 5(4), 6435–6442. https://doi.org/10.1109/LRA.2020.3013879

Ferrentino, E., Savino, H. J., Franchi, A. and Chiacchio, P. (2024). A dynamic programming framework for optimal planning of redundant robots along prescribed paths with kineto-dynamic constraints. *IEEE Transactions on Automation Science and Engineering*, 21(4), 6744–6757. https://doi.org/10.1109/TASE.2023.3330371

Gong, M., Li, X. and Zhang, L. (2019). Analytical inverse kinematics and self-motion application for 7-DOF redundant manipulator. *IEEE Access*, 7, 18662–18674. https://doi.org/10.1109/ACCESS.2019.2895741

Hauser, K. and Emmons, S. (2018). Global redundancy resolution via continuous pseudoinversion of the forward kinematic map. *IEEE Transactions on Automation Science and Engineering*, 15(3), 932–944. https://doi.org/10.1109/TASE.2018.2805878

Huang, H., Liu, H., Xia, C., Mei, H., Gao, X. and Liang, B. (2023). Sampling-based time-optimal path parameterization with jerk constraints for robotic manipulation. *Robotics and Autonomous Systems*, 170, 104530. https://doi.org/10.1016/j.robot.2023.104530

Kelemen, M., Virgala, I., Lipták, T., Miková, Ľ., Filakovský, F. and Bulej, V. (2018). A novel approach for an inverse kinematics solution of a redundant manipulator. *Applied Sciences*, 8(11), 2229. https://doi.org/10.3390/app8112229

Kingston, Z., Moll, M. and Kavraki, L. E. (2018). Sampling-based methods for motion planning with constraints. *Annual Review of Control, Robotics, and Autonomous Systems*, 1, 159–185. https://doi.org/10.1146/annurev-control-060117-105226

Kieffer, J. (1992). Manipulator inverse kinematics for untimed end-effector trajectories with ordinary singularities. *The International Journal of Robotics Research*, 11(3), 225–237. https://doi.org/10.1177/027836499201100305

Lakshmi Narayanan, V., Narayan, J., Gritli, H. and Dwivedy, S. K. (2026). A decade of inverse kinematics methods for serial manipulators: A systematic review. *Journal of Field Robotics*, 43(1), 184–229. https://doi.org/10.1002/rob.70014

Li, Y. and Wang, L. (2024). Comprehensive research and analysis on obstacle–singularity–joint limit avoidance of redundant robot. *International Journal of Advanced Robotic Systems*, 21(1). https://doi.org/10.1177/17298806241233910

Malhan, R. K., Thakar, S., Kabir, A. M., Rajendran, P., Bhatt, P. M. and Gupta, S. K. (2023). Generation of configuration space trajectories over semi-constrained Cartesian paths for robotic manipulators. *IEEE Transactions on Automation Science and Engineering*, 20(1), 193–205. https://doi.org/10.1109/TASE.2022.3144673

Malik, A., Henderson, T. and Prazenica, R. (2021). Multi-objective swarm intelligence trajectory generation for a 7 degree of freedom robotic manipulator. *Robotics*, 10(4), 127. https://doi.org/10.3390/robotics10040127

Milenkovic, P. (2022). Optimal path crossing the orientation exclusion zone of a robot with offset wrist. *Robotica*, 40(1), 191–212. https://doi.org/10.1017/S0263574721000461

Milenkovic, P., Wang, Z. and Rodriguez, J. I. (2023). Encountering singularities of a serial robot along continuous paths at high precision. *Mechanism and Machine Theory*, 181, 105224. https://doi.org/10.1016/j.mechmachtheory.2022.105224

Milenkovic, P., Wang, Z. and Rodriguez, J. I. (2026). Encircling singularities of a serial robot to find alternative inverse-kinematic solutions. *Mechanism and Machine Theory*, 219, 106314. https://doi.org/10.1016/j.mechmachtheory.2025.106314

Miyata, S., Miyahara, S. and Nenchev, D. (2017). Analytical formula for the pseudoinverse and its application for singular path tracking with a class of redundant robotic limbs. *Advanced Robotics*, 31(10), 509–518. https://doi.org/10.1080/01691864.2017.1285721

Müller, A. (2004). Collision avoiding continuation method for the inverse kinematics of redundant manipulators. In *Proceedings of the 2004 IEEE International Conference on Robotics and Automation*, 1593–1598. https://doi.org/10.1109/ROBOT.2004.1308051

Nguyen, D. T., Nguyen, V. T. T., Do, T. and Nguyen, V. L. (2026). Multi-solution inverse kinematics for robotic manipulators via permutation-invariant set prediction. *IEEE Robotics and Automation Letters*, 11(8), 9803–9810. https://doi.org/10.1109/LRA.2026.3703280

Oelerich, T., Beck, F., Hartl-Nesic, C. and Kugi, A. (2025). BoundMPC: Cartesian path following with error bounds based on model predictive control in the joint space. *The International Journal of Robotics Research*, 44(8), 1287–1316. https://doi.org/10.1177/02783649241309354

Oelerich, T., Hartl-Nesic, C., Beck, F. and Kugi, A. (2025). BoundPlanner: A convex-set-based approach to bounded manipulator trajectory planning. *IEEE Robotics and Automation Letters*, 10(6), 5393–5400. https://doi.org/10.1109/LRA.2025.3558450

Pan, Z., Polden, J., Larkin, N., Van Duin, S. and Norrish, J. (2012). Recent progress on programming methods for industrial robots. *Robotics and Computer-Integrated Manufacturing*, 28(2), 87–94. https://doi.org/10.1016/j.rcim.2011.08.004

Patkó, D. and Zelei, A. (2021). Velocity and acceleration level inverse kinematic calculation alternatives for redundant manipulators. *Meccanica*, 56, 887–900. https://doi.org/10.1007/s11012-020-01305-z

Peidro, A. and Haug, E. J. (2024). Obstacle avoidance in operational configuration space kinematic control of redundant serial manipulators. *Machines*, 12(1), 10. https://doi.org/10.3390/machines12010010

Pham, Q.-C. (2014). A general, fast, and robust implementation of the time-optimal path parameterization algorithm. *IEEE Transactions on Robotics*, 30(6), 1533–1540. https://doi.org/10.1109/TRO.2014.2351113

Pham, H. and Pham, Q.-C. (2017). On the structure of the time-optimal path parameterization problem with third-order constraints. In *2017 IEEE International Conference on Robotics and Automation (ICRA)*, 679–686. https://doi.org/10.1109/ICRA.2017.7989084

Pham, H. and Pham, Q.-C. (2018). A new approach to time-optimal path parameterization based on reachability analysis. *IEEE Transactions on Robotics*, 34(3), 645–659. https://doi.org/10.1109/TRO.2018.2819195

Rakita, D., Mutlu, B. and Gleicher, M. (2019). STAMPEDE: A discrete-optimization method for solving pathwise-inverse kinematics. In *2019 International Conference on Robotics and Automation (ICRA)*, 3507–3513. https://doi.org/10.1109/ICRA.2019.8793617

Reinhold, J., Baumann, H. and Meurer, T. (2023). Constrained-differential-kinematics-decomposition-based NMPC for online manipulator control with low computational costs. *Robotics*, 12(1), 7. https://doi.org/10.3390/robotics12010007

Reiter, A., Mueller, A. and Gattringer, H. (2018). On higher order inverse kinematics methods in time-optimal trajectory planning for kinematically redundant manipulators. *IEEE Transactions on Industrial Informatics*, 14(4), 1681–1690. https://doi.org/10.1109/TII.2018.2792002

Rudrasamudram, V. and Malaichamee, H. (2026). Singularity avoidance in inverse kinematics: A unified treatment of classical and learning-based methods. *arXiv preprint* arXiv:2604.13405 [not peer-reviewed]. https://doi.org/10.48550/arXiv.2604.13405

Safeea, M., Bearee, R. and Neto, P. (2021). A modified DLS scheme with controlled cyclic solution for inverse kinematics in redundant robots. *IEEE Transactions on Industrial Informatics*, 17(12), 8014–8023. https://doi.org/10.1109/TII.2021.3060019

Salunkhe, D. H., Marauli, T., Müller, A., Chablat, D. and Wenger, P. (2025). Kinematic issues in 6R cuspidal robots, guidelines for path planning and deciding cuspidality. *The International Journal of Robotics Research*, 44(6), 1035–1054. https://doi.org/10.1177/02783649241293481

Tringali, A. and Cocuzza, S. (2020). Globally optimal inverse kinematics method for a redundant robot manipulator with linear and nonlinear constraints. *Robotics*, 9(3), 61. https://doi.org/10.3390/robotics9030061

Trullo, H. D. and Vivas Alban, O. A. (2025). A systematic review of inverse kinematics methods for fixed-base serial manipulators: Analytical, numerical, and machine learning methods. *International Journal of Robotics and Control Systems*, 5(3), 1808–1827. https://doi.org/10.31763/ijrcs.v5i3.1820

Trutman, P., Safey El Din, M., Henrion, D. and Pajdla, T. (2022). Globally optimal solution to inverse kinematics of 7DOF serial manipulator. *IEEE Robotics and Automation Letters*, 7(3), 6012–6019. https://doi.org/10.1109/LRA.2022.3163444

Wang, Y., Sifferman, C. and Gleicher, M. (2024). IKLink: End-effector trajectory tracking with minimal reconfigurations. In *2024 IEEE International Conference on Robotics and Automation (ICRA)*, 12165–12171. https://doi.org/10.1109/ICRA57147.2024.10611510

Weingartshofer, T., Bischof, B., Meiringer, M., Hartl-Nesic, C. and Kugi, A. (2023). Optimization-based path planning framework for industrial manufacturing processes with complex continuous paths. *Robotics and Computer-Integrated Manufacturing*, 82, 102516. https://doi.org/10.1016/j.rcim.2022.102516

Wenger, P. and Chablat, D. (2023). A review of cuspidal serial and parallel manipulators. *Journal of Mechanisms and Robotics*, 15(4), 040801. https://doi.org/10.1115/1.4055677

Xing, H., Huang, R., Yang, Y., Chen, J., Li, W., Yao, C., Shi, C. and Ding, L. (2026). Inverse kinematics and redundancy resolution in manipulators: Methods, optimization objectives, and future trends. *Biomimetic Intelligence and Robotics*, 6(2), 100339. https://doi.org/10.1016/j.birob.2026.100339

Yin, Z., Wu, F., Wang, Z., Yang, J., Tan, J. and Kong, D. (2025). Dynamic programming-based offline redundancy resolution of redundant manipulators along prescribed paths with real-time adjustment. *arXiv preprint* arXiv:2411.17052v2. https://doi.org/10.48550/arXiv.2411.17052

Yoshizawa, M., Terui, A. and Mikawa, M. (2023). Inverse kinematics and path planning of manipulator using real quantifier elimination based on Comprehensive Gröbner Systems. *arXiv preprint* arXiv:2305.12451. https://doi.org/10.48550/arXiv.2305.12451

Zeng, Z., Guo, J., Chen, J., Li, Y., Peng, S. and Pan, Y. (2026). Reliable 7-DOF manipulator execution via arm-angle selection and trajectory retiming. *IEEE Robotics and Automation Letters*, 11(11), 12919–12926. https://doi.org/10.1109/LRA.2026.3732902

Zhang, L., Du, H., Qin, Z., Zhao, Y.-J. and Yang, G. (2024). Real-time optimized inverse kinematics of redundant robots under inequality constraints. *Scientific Reports*, 14, 29754. https://doi.org/10.1038/s41598-024-81174-8

Zhang, M., Mei, S., He, H., Han, X. and Li, Z. (2026). Analytical inverse kinematics solution and global arm angle optimization method for 7-DOF redundant robotic arms without offset. *ISA Transactions*, 173, 425–436. https://doi.org/10.1016/j.isatra.2026.03.028

Zhang, Y. and Kikuuwe, R. (2026). Ensuring viability: A QP-based inverse kinematics for handling joint range, velocity and acceleration limits, as well as whole-body collision avoidance. *Journal of Intelligent & Robotic Systems*, 112(1), 16. https://doi.org/10.1007/s10846-025-02335-z

Zhang, Y. and Wang, H. (2025). Redundancy-based motion planning with task constraints for robot manipulators. *Sensors*, 25(6), 1900. https://doi.org/10.3390/s25061900

Zhang, Y., Xiao, Q., Wan, L. and Jiang, B. (2026). Collision-free robot pose optimization method based on improved algorithms. *Machines*, 14(1), 65. https://doi.org/10.3390/machines14010065


## Supplementary Note S1. Search and selection methods

### S1.1. Review type and retrieval approach

This article uses a mechanism-oriented narrative synthesis supported by limited structured retrieval. The search was designed to identify papers that explain a relevant mechanism, test a consequential contrast, or clarify the boundary between pathwise inverse kinematics (IK), constraint-aware planning, and timed execution. It was not designed to estimate the frequency of methods across the field.

The retrieval process used 17 targeted queries on the Consensus platform and a focused public-web update with inspection of publisher and academic landing pages where available. Search topics covered: (1) pathwise IK, solution-branch selection, and continuation; (2) singularity crossing, cuspidal manipulators, and mode transitions; (3) constrained differential IK, redundancy/arm-angle selection, and retiming; (4) graph-based IK and collision-aware path construction; (5) TOPP and higher-order dynamic constraints; (6) learning-based multi-solution IK; and (7) industrial robot programming and offline programming. These topic groups support focused retrieval but do not establish exhaustive coverage.

### S1.2. Eligibility and scope decisions

The core scope is fixed-base serial manipulators and studies that directly address at least one of the following: pathwise solution selection or continuation; singularity or solution-mode events; joint, collision, derivative, or torque constraints; or reconstruction and verification of the resulting trajectory. Foundational studies were retained when needed to explain a mechanism.

Adjacent studies were retained when they clarified an important boundary but did not match the core task in full. Examples include semi-constrained process paths, bounded-error Cartesian corridors, pose-level IK or solution-set prediction, constrained sampling-based planning, and time-optimal parameterization. A humanoid-arm study is marked as an extension rather than treated as representative evidence for industrial manipulators. Commercial offline-programming software is discussed as an application context, not compared feature by feature, because this review does not have a common, independently inspectable basis for comparing each product's internal algorithms and verification guarantees.

Studies of parallel, continuum, mobile-base, or dual-arm systems were not treated as core evidence unless a specific mechanism was directly relevant to the stated questions. The presence of an adjacent or extension study in the synthesis does not expand the population for which the findings are claimed.

### S1.3. Study selection and evidence extraction

Six mechanism anchors were selected purposively to expose contrasting solution-state representations, transition rules, constraint domains, and verification practices. Additional studies were retained when they supplied a useful comparator or challenged an overly broad interpretation. This selection strategy is analytical rather than statistically representative.

For each included study, the synthesis records the robot and task, the path/solution representation, relevant event or transition assumptions, hard constraints versus soft objectives, the domain on which constraints are imposed, the reconstructed or timed object actually checked, and the type of evidence reported. Tables 1A and 1B separate sources with detailed methodological or experimental material from candidates available only through abstracts or publisher previews. Abstract-only candidates are contextual leads and are not used as decisive support for Findings F1–F3.

### S1.4. Limitations of retrieval and appraisal

The search did not use authenticated database-native searches in Scopus or Web of Science, and citation chaining was not exhaustive. Not every candidate received an independent full-text assessment. The selected examples therefore support mechanism-level comparisons, not claims of exhaustive recall, field-wide prevalence, or universal method superiority.

The coding scheme is descriptive, not a numerical scale. A second independent coder has not completed the proposed six-anchor coding check, and no inter-rater agreement statistic is reported. The G0/G1/G2E/G2T benchmark is a proposal; no common-task experiment has been performed. These limits are reflected in the main-text conclusions.


## Supplementary Note S2. Claim-to-source locators and source-version distinctions

| Study | Source and technical locator | Bounded finding supported |
|---|---|---|
| Rakita et al. (2019) | Rakita et al. (2019), [author PDF](https://graphics.cs.wisc.edu/Papers/2019/RMG19/19_ICRA_Stampede.pdf), §IV-A/B | Layered graph with node-and-edge admissibility; finite-graph dynamic-programming optimum. |
| Ferrentino et al. (2024) | Ferrentino et al. (2024), [institutional accepted PDF](https://ris.utwente.nl/ws/portalfiles/portal/328327609/A_Dynamic_Programming_Framework_for_Optimal_Planning_of_Redundant_Robots_Along_Prescribed_Paths_With_Kineto-Dynamic_Constraints.pdf), §II-B Eqs. (17)–(22), §III Algorithm 1, §IV | Discrete state, derivative, torque and torque-rate feasibility; Panda experiments. |
| Elias and Wen (2025) | Elias and Wen (2025), [author arXiv v2](https://arxiv.org/abs/2501.18505), §4.2 Eqs. (9)–(12), §5 and §6 | Cuspidal path graph, optional sign-based nonsingularity policy and workpiece-offset optimization. Formal reference is the **journal** DOI 10.1115/1.4069599; paper-specific preprint page numbers are not assumed to match the journal layout. |
| Boschi et al. (2026) | Boschi et al. (2026), [published full paper](https://cris.unibo.it/handle/11585/1039115), §II-B Eqs. (13)–(14), §III-A Eqs. (15)–(17), §III-B Algorithm 1, §IV experiments and Conclusion | Architecture-specific factor/index transition at kinematically admissible crossings; UR5e evaluation. The Eq. (17) velocity parameter is part of threshold design, not a speed-limit certificate. |
| Weingartshofer et al. (2023) | Weingartshofer et al. (2023), [open article](https://doi.org/10.1016/j.rcim.2022.102516), Eq. (13b), §5.3.3 Eqs. (36)–(37), §5.3.4 Eqs. (40)–(44), §5.5, §6 | Hard joint bounds and collision inequality separated from collision, movement and joint-margin **penalties**; toleranced process paths; iiwa physical drawing and KR8 simulated spraying. |
| Zhang and Kikuuwe (2026) | Zhang and Kikuuwe (2026), [author-hosted published copy](https://home.hiroshima-u.ac.jp/kikuuwe/pub/26_jirs.pdf), §2.1 Eq. (2), §2.2 Lemma 1/Eq. (10), §2.3 Eqs. (13)–(16), (22)–(23), §5 | Discrete-time modeled viability and numerical evaluation with compound joint and approximate collision inequalities. |

Each locator identifies the source version and section or equation used to support the bounded statement shown. Graph feasibility, task-continuity evidence, physical demonstration, and independent interval certification are different evidence types. The listed locators do not imply independent replication of the original experiments. For Elias and Wen, the cited equation numbers refer to the author-hosted preprint version; exact correspondence with every equation number in the journal layout has not been independently verified.

Studies discussed in the main text but not represented by a row in this compact locator table are cited in the References. Their inclusion supports the specific proposition described in the relevant paragraph; it does not imply that every mathematical assumption or experiment has been independently re-evaluated.

## Supplementary Note S3. Three reporting examples

| Report item | Weingartshofer et al. (2023) | Elias and Wen (2025) | Zhang and Kikuuwe (2026) |
|---|---|---|---|
| Geometric task | Toleranced drawing / spraying toolpath | Cuspidal 6R path and workpiece placement | Differential end-effector tracking |
| IK and event | Multi-start nonlinear joint-path planning; passage permitted | Sampled all-solutions graph; optional sign-restricted edges | Discrete QP, no stated event-index mechanism |
| Declared constraints | Eq.13b hard joint limits, Eq.37 collision inequality; Eqs.36,40,42–44 penalties | Graph movement limits and optional time-conditioned edge rules; collision not integrated | State limits and approximated whole-body collision in discrete viability model |
| Reconstruction/validation | Piecewise cubic Hermite; iiwa hardware drawing and KR8 spraying simulation | Graph path with sampling and numerical examples | Discrete-time numerical simulation |
| What an integrated benchmark would additionally check | Same interpolated segment against swept-link geometry and timed limits | Link-obstacle clearance if environmental collision is introduced | Model-to-controller timing, geometry and continuous inter-sample bounds if claimed |

These cases illustrate the reporting fields' interpretability for different problem formulations; they do not estimate inter-rater agreement or certify a field-wide reporting standard.


## Supplementary Note S4. T1–T3 evidence tags and limited coding-reliability protocol

### S4.1. Five evidence tags

The tags apply to an individual claim or subclaim in Tables 1A–1B, not to a paper's overall quality or performance. More than one tag may appear in a cell only when it qualifies different claims.

| Tag | Definition | Interpretation rule |
|---|---|---|
| **D — Demonstrated/reported** | The inspected source reports the relevant method, result, simulation, or experiment | This does not mean independently replicated, formally proved, or transferable to another robot |
| **C — Conditional** | The claim depends on an explicit robot-architecture, path, task, or model precondition | Do not generalize beyond the stated preconditions |
| **R — Resolution-limited** | The check or optimization is defined over sampled, discrete, finite-graph, or finite-step objects | Do not silently upgrade it to an all-continuous-domain guarantee |
| **U — Unassessed** | The claim was not assessed, or the necessary detail was not present in the source material inspected | U is not evidence of failure |
| **N — Not applicable** | The issue does not apply to the paper's stated task or principal claim | N is not a negative result and must not be used when evidence is merely missing |

These five tags are the only evidence-status codes used in Tables 1A–1B; earlier variants have been normalized to this legend. They are descriptive labels, not ordinal levels, scores, or a ranking. The benchmark's outcome descriptions serve a different purpose: they describe possible results of a future run and must not be mixed with the T1–T3 evidence tags.

### S4.2. T1–T3 coding instructions

- **T1 — Pathwise selection and events:** record the selected state/branch representation, allowed transitions, and relevant preconditions. Use C when the transition is explicitly architecture- or path-dependent; use R when the reported selection is limited to a finite candidate graph or discrete sample set; use U when the transition assumptions are not available in the checked source; use N only when the event question is outside the stated task.
- **T2 — Constraints and domain:** distinguish hard inequalities from soft objectives or penalties. Record whether conditions are imposed on nodes, graph edges, reconstructed segments, or timed commands. Use R for discrete/sampled enforcement, U for a missing or unassessed constraint claim, and N when the constraint is outside the paper's stated scope.
- **T3 — Verification:** identify the object actually checked. **T3g** means verification of reconstructed geometry (including FK residual, continuity, and relevant full-link collision checks); **T3d** means verification of the realized timed trajectory/controller command (including dynamic extrema and tracking when claimed). T3g and T3d are subtypes of T3, not additional dimensions. A reported simulation or hardware test can receive D while a broader all-interval or cross-platform claim in the same cell receives U.

The guarantee or optimization object is not a separate axis. It is recorded in its own Table 1A/1B column to state precisely what is optimized or claimed (for example, a finite-graph optimum, a discrete-time viability result, or a bounded-error corridor objective).

### S4.3. Relationship to the proposed G benchmark

The benchmark tiers operationalize the evidence questions rather than validate the tags. G0 primarily tests T1 and T3g for an exact geometric lift. G1 adds T2 collision/clearance constraints and T3g checks of reconstructed full-link geometry. G2E adds time-dependent T2 constraints and T3d verification of the actual timed command. G2T uses the same T3g/T3d distinction but evaluates a separately defined task tube; its results must not be ranked as exact-path G2E results.

### S4.4. Limited reliability check: status and protocol

**Status: not performed.** The proposed protocol applies to the six purposively selected anchor cases: Rakita et al. (STAMPEDE), Ferrentino et al., Elias and Wen, Boschi et al., Weingartshofer et al., and Zhang and Kikuuwe. No independent second-coder assessment has been completed. It would be methodologically incorrect to report a two-coder agreement rate or Cohen's kappa from a self-check or from the same reviewer repeating the coding.

Before submission, two reviewers should independently code T1, T2, and T3 for those six anchor studies using S4.1–S4.2, without seeing each other's first-pass decisions. The manuscript should report the per-case disagreements, exact agreement separately for T1/T2/T3, and an overall raw agreement; Cohen's kappa may be added only with a clear warning that six cases provide a very small and potentially prevalence-sensitive estimate. Disagreements should be adjudicated only after the first-pass agreement is calculated. Until that step is completed, the framework should be described as transparent and auditable, but not as inter-rater validated.
