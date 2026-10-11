<!-- Gate 7-R5: evidence-grounded revised manuscript; R4 baseline and the original 179/104/87 screening and reading ledgers are preserved. No new experiment or authenticated multi-database search is claimed. -->
# Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators: Branch Selection, Singularity Transitions, and Joint/Path Constraints

## Abstract

A Cartesian toolpath may admit multiple inverse-kinematics (IK) solutions without a readily identifiable constrained joint-space realization. This structured narrative synthesis examines pathwise IK for fixed-base serial manipulators through six purposively chosen mechanism anchors and complementary primary studies. Five axes distinguish solution-state representation, singularity or mode response, constraint scope, guarantee object and validation. An applicability-aware T1/T2/T3 lens separately examines coherent continuation, constraint enforcement and verification over the claimed execution domain. Our analysis distinguishes pointwise IK existence from a continuous selector, sampled-graph optimality from checked interpolated motion, nonsingular cuspidal mode changes from singular crossing, and hard model inequalities from physical execution guarantees. Graph-plus-collision posture optimization, task-constrained redundancy-based planning, bounded-corridor MPC, arm-angle retiming and cyclic IK provide positive examples of method integration; we do not claim that integrated methods are absent. A literature-grounded, hypothetical common-task analysis clarifies platform and task-transfer constraints without inventing common-robot experiments. The focused historical corpus comprises 179 DOI-unique records, but the search is non-exhaustive, and several 2026 near-neighbor studies remain assessed at abstract or publisher-preview depth. The principal contribution is a source- and applicability-aware account of how solution decisions, reconstructed trajectories and reported verification domains can be meaningfully connected, not a universal safety theorem or an exhaustive field census.

**Keywords:** pathwise inverse kinematics; solution branches; singularity transitions; cuspidal robots; redundancy resolution; collision constraints; dynamic programming; industrial manipulators

## 1. Introduction

For a fixed-base serial manipulator, a sequence of feasible end-effector poses does not uniquely specify how the joints should move between them. A robot may have different IK configurations for each pose, and a locally convenient choice can produce a discontinuity when carried along a process path. Obstacle geometry and actuator limits then impose additional conditions on the selected motion. These issues arise together in toolpath-following tasks, where the trajectory, not merely its endpoint, is part of the specification.

Let \(f:\mathcal Q\to\mathcal X\) be the forward-kinematics map and \(x:[0,1]\to\mathcal X\) a prescribed task-space path. An *exact geometric lift* is a continuous \(q:[0,1]\to\mathcal Q\) satisfying

\[
 f(q(s))=x(s),\qquad s\in[0,1].
\]

For a process with allowed task deviation, replace the equality by an explicit admissible set \(f(q(s))\in\mathcal X_{\mathrm{task}}(s)\). For time-dependent claims, a timing law \(s=s(t)\) and suitable differentiability or piecewise regularity are additionally required. When these derivatives exist,

\[
 \dot q(t)=q'(s)\dot s(t),\qquad
 \ddot q(t)=q''(s)\dot s(t)^2+q'(s)\ddot s(t),
\]

with velocities and accelerations interpreted on the smooth segments and with appropriate junction conditions. Torque and torque-rate calculations further require a dynamic model, payload, and operating assumptions. Continuity of \(q(s)\) alone supplies none of these higher-order guarantees.

Recent work makes different parts of this construction explicit. Analytical descriptions reveal IK solution structure (Hauser and Emmons, 2018; Gong et al., 2019). Pathwise graphs select compatible sampled configurations (Rakita et al., 2019; Wang et al., 2024; Elias and Wen, 2025). Geometry of cuspidal manipulators makes nonsingular solution-mode changes possible under particular architectures (Wenger and Chablat, 2023; Salunkhe et al., 2025), whereas Boschi et al. (2026) construct transitions through selected singularities of UR-like robots. Finite-grid dynamic programming and constrained differential IK address distinct joint and dynamic bounds (Ferrentino et al., 2024; Zhang and Kikuuwe, 2026). Industrial toolpath optimization adds task-space tolerance, collision, and controller realization (Weingartshofer et al., 2023).

Existing IK reviews principally organize solver families or kinematic architectures (Colomé and Torras, 2012; Trullo and Alban, 2025; Lakshmi Narayanan et al., 2026). The present review instead compares the *mathematical object* delivered by each approach: a candidate configuration, a continuation rule, a singularity event, a constrained finite path, or a checked executable trajectory. Its contribution is a mechanism-and-guarantee-domain comparison, strengthened here with non-anchor evidence and a transparent distinction among verified full text, publisher full text inspected in this revision, and abstract-only candidates. The synthesis framework is a reporting proposal, not a newly proven trajectory-safety theorem.

## 2. Scope and Analytical Method

### 2.1. Design, topic-aligned discovery, and source selection

This is a **structured, mechanism-oriented narrative synthesis**, not a systematic review. The research question concerns coherent inverse-kinematic realization of prescribed Cartesian paths for fixed-base serial manipulators, particularly branch or singularity events and geometric or time-dependent joint constraints. The archived focused protocol covers publications from 1 January 2016 to 29 September 2026, with separately identified foundational older work.

The topic-specific TCIK discovery used one exploratory Consensus Pro query for concept development and 16 logged Consensus Quick queries on 29 September 2026. Its RIS-derived exports contained **419 record instances**, not independent studies. DOI normalization produced **179 DOI-unique entries**. Historical screening decisions were **30 CORE_INCLUDE, 74 ADJACENT, 57 EXCLUDE and 18 UNCERTAIN_FULLTEXT**, yielding **104 retained** working-bibliography records. Among those 104, the dated reading log records **87 READ_COMPLETE and 17 PAYWALLED_OR_UNAVAILABLE**. The abstract metadata flags AVAILABLE (161) and MISSING (18) are not identical to the screening dispositions: five AVAILABLE records received uncertain decisions and five MISSING records were excluded. This post-hoc discrepancy is disclosed and not silently rewritten; see Supplementary S1.5–S1.6. READ_COMPLETE denotes documented reading, not complete independent verification of each published claim.

Six anchors were retrospectively selected for their contrasting mathematical and computational mechanisms, rather than representativeness, popularity or comparative performance: Rakita et al. (2019), Ferrentino et al. (2024), Elias and Wen (2025), Boschi et al. (2026), Weingartshofer et al. (2023), and Zhang and Kikuuwe (2026). Three are within the retained TCIK set; three are separately located in-window supplements. The analysis was triangulated with near neighbors and previously read studies when these challenged the proposed synthesis. A separate earlier uncertainty-aware trajectory-planning project (306 retrieval occurrences, 226 deduplicated titles) addressed a different question and is **not** an upstream screening denominator for the TCIK project.

A bounded public-web search on **11 October 2026** identified four relevant 2026 DOIs missing from the original 179: Y. Zhang et al. (*Machines*), Zeng et al. (*IEEE RA-L*), M. Zhang et al. (*ISA Transactions*), and Milenkovic et al. (*Mechanism and Machine Theory*). Their absence establishes known-item omissions, **not a measured recall rate**. The *Machines* publisher full HTML was inspected. The other three are cited only for their author-reported abstract or publisher-preview mechanisms, with exact theorem and experimental assumptions **NOT_ASSESSED**. An older SSRN version of Milenkovic et al. is known but is not assumed identical to the 2026 journal article. This update was not an authenticated Scopus, Web of Science or database-native IEEE Xplore search, and exhaustive citation chaining was **NOT_DONE**.

R5 adds four previously recorded READ_COMPLETE but uncited works that materially clarify cyclic repeatability, pathwise solution existence, redundancy-based task-constrained motion and bounded-corridor planning: Dulęba and Karcz-Dulęba (2018), Yoshizawa et al. (2023), Zhang and Wang (2025), and Oelerich et al. (2025; *BoundPlanner*). The formal bibliography now cites **25** of the 87 historically READ_COMPLETE records, with **62** not formally cited. A comprehensive R5 claim-impact audit of those 62 was **NOT_DONE**; they are not treated as negative field evidence.

Supplementary S1 provides provenance, frozen historical screening states and source-depth distinctions. PRISMA-S-style transparency principles inform documentation without a systematic-review designation. Neither literature saturation nor field-wide absence of an integrated verification framework is established.

### 2.2. Five comparison axes

The analytical unit is a method applied to a specified robot, task and path. Each primary-source claim is coded along the following axes:

| Axis | Question that distinguishes methods |
|---|---|
| **Solution-state representation** | Are alternatives indexed analytically, described by a redundancy coordinate, or represented as sampled nodes? |
| **Singularity/mode response** | Does the method avoid, regularize, permit, or construct a passage, and for which kinematic event? |
| **Constraint scope** | Which position, path-fidelity, collision, derivative, or torque constraints are encoded, and on what domain? |
| **Guarantee object** | Is the result an admissible solution, an optimal path in a finite graph, a conditional kinematic construction, discrete viability, or a continuously checked trajectory? |
| **Validation setting** | Is the result analytical, numerical, simulated, or executed on hardware, and with which task assumptions? |

This separation keeps a finite-graph optimum from being interpreted as a continuous-time optimum, and a successful hardware trial from being interpreted as an unconditional guarantee.

### 2.3. Applicability-aware integration questions

To discuss systems intended to execute a constrained manufacturing path, we distinguish three questions rather than assigning a universal pass/fail grade to every IK paper.

**T1 — Continuation and event semantics.** **T1a** records whether and how the method selects a coherent joint-path relation. **T1b** records a branch or mode event rule only when the method claims to handle such an event. **T1c** specifies the domain of the result: samples, graph edges, a reconstructed curve, or an analytic interval. Absence of a singular crossing mechanism in a method devoted to obstacle-free ordinary continuation is not, by itself, failure of T1a.

**T2 — Constraint formulation and domain.** Record which constraints are hard, which are penalties, and whether they are evaluated at nodes, over edges, at discrete controller steps, or on reconstructed continuous intervals. “Hard inequality in an optimization program” describes a formulation; it is not equivalent to a separately established inequality for every intermediate physical configuration.

**T3 — Verification matched to the claim.** **T3g** concerns link/obstacle clearance on the reconstructed path **when collision avoidance is a task or method claim**. **T3d** concerns timed velocity/acceleration/torque behavior **when time or dynamics are part of the claim**. Each can be *not applicable*, *supported at finite resolution*, *supported over the asserted continuous domain*, or *unresolved*. A geometric-only singularity study should not be penalized for omitting torque certification it never sought to provide.

For an **integrated collision-constrained, timed manufacturing benchmark**, all relevant obligations become applicable to the *complete system*: it must specify the continuation and any required event, enforce the declared constraints, and demonstrate the safety and dynamic evidence required by that benchmark. These are requirements for the integrated task, not an assertion that every individual paper should solve it alone.

## 3. Research Status

### 3.1. What constitutes a persistent solution choice?

Analytical branch labels, redundancy coordinates, and sampled solution nodes describe different types of state. In an architecture-specific analytic model, a branch or posture index can explain why two joint solutions are distinct and when that description degenerates (Gong et al., 2019). Hauser and Emmons (2018) address global redundancy resolution through configuration-sheet and pseudoinverse constructions, shifting attention from a single IK query to an assignment over the task workspace. These descriptions can reveal connectivity that would be invisible to independently solved poses; they do not by themselves determine obstacle-aware timed execution. Faria et al. (2018) further illustrate architecture-aware global configuration control and joint-limit or singularity avoidance, while the pointwise global optimality investigated by Trutman et al. (2022) addresses a different object from a pathwise lift. This distinction matters even when both method classes are termed “global IK.”

STAMPEDE (Rakita et al., 2019) makes the decision pathwise by constructing layers of candidate IK configurations for successive Cartesian samples. Its graph nodes represent feasible configurations and its **edges represent legal inter-layer motion**, including joint-motion rules. Dynamic programming selects an optimum **among admissible paths in the constructed graph** (authors' §IV-A/B). Node feasibility and edge legality are both essential: reducing this method to independent pose checks would misstate its contribution. The sampling strategy is consequential because useful configurations absent from the graph cannot be selected.

Elias and Wen (2025) similarly use a sampled graph of IK solutions, with edge weights based on wrapped joint movement and the prescribed path increment (arXiv v2, §4.2, Eqs. 9–12). Their cuspidal analysis makes the nature of solution connectivity especially important: a pose may possess multiple solutions while the feasible continuous lift depends on which connected solutions are selected. The graph minimizes cost **within the represented candidates and edges**. The authors also optimize the workpiece-relative placement of a specified toolpath (§5), so their framework may change the robot-base location of the path as well as the selected joint route.

Further retained full-text evidence clarifies why "smooth" need not mean repeatable: Safeea et al. (2021) identify the cyclic-drift problem in conventional damped-least-squares IK and report a controlled cyclic scheme, including a KUKA iiwa experiment. Tringali and Cocuzza (2020) use multistart whole-trajectory optimization with constraints and cyclic-path examples; multiple numerical starts are not a general global-optimality certificate. Malhan et al. (2023) build layered configuration graphs for semi-constrained Cartesian paths and multiple tool-center-point options, so graph connectivity must be compared with the allowed task manifold rather than only with fixed-pose tracking. These three records were already READ_COMPLETE but were absent from the R3 bibliography; they broaden the path-state evidence beyond the six anchors.

IKLink (Wang et al., 2024), offline/online redundancy adjustment (Yin et al., 2025), and temporal multi-solution selection (Nguyen et al., 2026) add further computational perspectives. Their mechanisms are relevant to reducing reconfiguration, but an empirical preference for a nearby joint solution should not be equated with an analytic branch identifier. The useful distinction is **what state the algorithm preserves**, rather than whether all methods produce visually smooth joints.

### 3.2. Distinct mechanisms for singularity handling and transitions

A singular configuration is a rank-deficient point of a kinematic mapping; its meaning for a path depends on the robot architecture, the chosen task, and the direction of passage. Earlier continuation methods already treated such events along prescribed tool trajectories (Kieffer, 1992), while singularity-theoretic analyses distinguish the geometry of these configurations from merely numerical conditioning (Donelan, 2007; Dulęba and Karcz-Dulęba, 2023). Three responses should not be collapsed into one notion of “singularity handling.”

**Singularity-consistent tracking** may deliberately address paths for which rank loss cannot simply be avoided. Miyata, Miyahara and Nenchev (2017) propose a structure-specific right-pseudoinverse construction for a degenerate singular path, with numerical demonstrations on representative redundant limbs; the current review assessed the publisher bibliographic record and publicly indexed abstract, **not its complete mathematical proof**. Milenkovic (2022) studies path reversal and orientation deviation near an offset-wrist singularity, with a high-order predictor–corrector mechanism as described in the accessible Cambridge publisher abstract; this should not be treated as the same event or guarantee as Boschi's UR-like branch transition.

**Avoidance and regularization** restrict trajectories or numerical behavior near rank loss. They are useful when a nonsingular route exists or when modest task variation is allowed (Beck et al., 2023; Milenkovic et al., 2023). Avoidance can also exclude a necessary exact-path crossing, so success must be interpreted relative to whether the toolpath may move.

**Nonsingular mode change** can occur in suitable cuspidal manipulators. Wenger and Chablat (2023), Salunkhe et al. (2025), and Elias and Wen (2025) distinguish such topology from a passage through Jacobian rank loss. The route and its existence conditions are architecture-dependent. In Elias and Wen's graph construction, restricting edges to retain the sign of \(\det J\) can enforce a *sampled nonsingularity policy*; allowing graph connections across sign changes does not alone prove the regularity of every interpolated configuration (arXiv v2, §4.2).

**Singular crossing with a branch transition** is the target of Boschi et al. (2026) for UR-like non-cuspidal structures. The authors factor the Jacobian determinant into posture-related factors (published §II-B, Eqs. 13–14) and associate the signs with branch indices. When an admissible task path passes through a singular configuration, the appropriate post-event branch can differ from the pre-event branch. Their §III-A derives a threshold using the change in singularity factors between sampled commands (Eqs. 15–17); Algorithm 1 selects candidate branches and treats wrist singularity degeneracy. The threshold is a **switching/detection mechanism**, not a certification of joint-velocity bounds merely because maximum joint velocity appears in its derivation. In §IV, UR5e peg-in-hole and pick-and-place cases demonstrate the intended continuous joint evolution, while the paper conditions applicability on **kinematically admissible** paths (Conclusion). This is a specific solution to event-conditioned kinematic selection rather than a generic collision or dynamic-feasibility algorithm.

These distinctions suggest a practical question for a planner: *is the desired route feasible without a change of mode; does the chosen architecture permit nonsingular mode change; or does the fixed path require a singular passage with a valid event law?* A regularizer, a graph sign policy, and an indexed transition rule are not substitute answers.

### 3.3. Geometric, time-dependent, and process constraints

The physical meaning of constraints depends on their variables and verification domain. Joint position can be bounded during geometric IK construction. Joint velocity, acceleration, jerk, torque and torque rate require a timing law and model approximations. Obstacle clearance depends on the occupied geometry of every relevant link along the path, not merely on end-effector pose. Collision-aware continuation was already an explicit IK consideration in Müller (2004); newer constrained formulations make different tradeoffs between geometry, dynamics and computational scope.

Ferrentino et al. (2024) integrate redundancy resolution and time-related limits in dynamic programming. Their **§II-B, Eqs. (17)–(22)** encode admissible states, joint velocity/acceleration/jerk and torque/torque-rate bounds; Algorithm 1 evaluates transitions on a finite discretization. The paper reports experiments on the Franka Emika Panda (§IV). This integrates choices often separated into geometric planning and retiming, but the optimized object remains discretized; the authors also note that checking some higher-order constraints without augmenting state can compromise an unrestricted global-optimality interpretation (§III). Physical execution supports the reported hardware case, not an all-interval certificate for arbitrary controller conditions.

Zhang and Kikuuwe (2026) address differential IK through an auxiliary discrete-time viability construction (§2.1–2.3). Their Lemma 1 and modeled joint and collision inequalities provide feasibility reasoning for the stated discrete model. This is stronger than merely placing soft penalties in a tracking cost, while remaining distinct from a continuous-time swept-volume or torque-bound verification. Their simulations examine the specified discrete scheme, without transferring the result to an unmodeled actuator or environment.

Weingartshofer et al. (2023) connect geometric feasibility to manufacturing-process freedom. The paper optimizes multiple candidate joint paths, permits specified position/orientation tolerances, and uses constraints adapted to drawing and spraying. Crucially, **joint-position limits are hard constraints in Eq. (13b)**. The collision term in **Eq. (36) is a soft penalty**, while **Eq. (37) is an inequality constraint**. The nearby-joint penalty **Eq. (40)** promotes continuity, and **Eqs. (42)–(44)** penalize approaches to joint-limit boundaries; these penalties must not be mislabelled as the hard joint limits (§5.3.3–5.3.4). The paper allows kinematic singular passage, reconstructs trajectories using cubic Hermite segments (§5.5), and reports real KUKA LBR iiwa drawing and simulated KUKA KR8 spraying (§6). Its process-specific flexibility is a substantive advantage: exact fidelity to an unrelaxed path is not the problem it sets out to solve. The formulation and demonstrations do not replace a separate continuous swept-link collision or timed-dynamic verification for every reconstructed segment.

Patkó and Zelei (2021) compare velocity- and acceleration-level IK implementations and analyze numerical stability under their stated discretization assumptions; their publisher article is openly available and was inspected here. Their analytical convergence and step-size domains should not be read as collision, torque or branch-event certification. Li and Wang (2024) propose a combined obstacle–singularity–joint-limit avoidance controller based on projected gradients and weighted damped inverses, with simulation on a reduced-DOF redundant configuration. Their publisher full article explicitly notes that singularity and joint-limit avoidance introduce end-effector tracking error. This is positive *multi-constraint avoidance* evidence, not a singular crossing rule or whole-trajectory swept-volume certificate. Oelerich et al. (2025) take a different approach in BoundMPC, using Cartesian path-error windows in joint-space MPC; allowing bounded task deviation expands the feasible task specification rather than proving feasibility of the unrelaxed exact path.

Additional constrained numerical approaches include higher-order IK and time-optimal multiple shooting (Reiter et al., 2018), dynamic joint bounds (Faroni et al., 2020), inequality-constrained real-time IK (Zhang et al., 2024), and model-predictive constrained differential kinematics (Reinhold et al., 2023). They broaden the architectural options for an integrated system, but their constraint objects should be compared against what they actually formulate and demonstrate, not credited with an unspecified branch-event theorem.

### 3.4. Cross-method five-axis comparison

**Table 1** distills directly examined studies. Entries state a method's positive mechanism and its mathematical/experimental domain. Detailed source locations are in Supplementary Note S2.

| Method | Solution state | Singularity/mode response | Constraints and enforcement domain | Guarantee or optimization object | Validation |
|---|---|---|---|---|---|
| **STAMPEDE** (Rakita et al., 2019) | Sampled, layered IK-candidate graph | Singularity-related sampling/filtering; no claimed indexed crossing law | Legal nodes **and** inter-layer edges; modeled collisions and joint-motion criteria | Admissible minimum-cost route in constructed graph | Numerical comparisons on multiple manipulators |
| **Ferrentino et al. (2024)** | Finite redundancy/trajectory-state grid | Aspect-based restrictions are conditional on available decomposition | Discretized state/transition constraints for positions, derivatives, torques and torque rates | Finite-resolution dynamic-programming solution; higher-order check qualification | Panda numerical planning and hardware tracking |
| **Elias and Wen (2025)** | All IK solutions at task-path samples; graph edges | Nonsingular cuspidal mode changes; optional sampled singular connections | Graph-edge movement/optional time-dependent bounds; collision modeling not integrated in analyzed construction | Graph-optimal path, sensitive to sampling and edge rules | Cuspidal-model numerical/toolpath optimization |
| **Boschi et al. (2026)** | Posture indices from Jacobian-factor signs | Event-conditioned switch through selected UR-like singularities | Kinematic admissibility and thresholded branch selection; no separate collision/dynamic certificate reported in reviewed sections | Conditional kinematic transition algorithm, not universal continuous-time proof | UR5e peg-in-hole and pick-and-place experiments |
| **Weingartshofer et al. (2023)** | Multiple optimization-start joint paths | Singular passage permitted during numerical planning | Hard joint bounds Eq.13b and collision inequality Eq.37; soft smoothness and clearance costs | Process-tolerant nonlinear planning plus Hermite reconstruction | iiwa drawing hardware; KR8 spraying simulation |
| **Zhang and Kikuuwe (2026)** | Differential QP solution at discrete steps | No branch-event mechanism assessed as part of its stated problem | Discrete-time joint-state and modeled whole-body collision constraints | Viability/feasibility conditions for modeled discrete dynamics | Numerical simulations |

**Table 1A. Why these six anchor methods were selected, and what alternatives prevent a single-case conclusion.** Selection is mechanism-based and retrospective; these are not performance rankings.

| Anchor method | Distinct contrast supplied to Table 1 | Closest complementary or challenging study |
|---|---|---|
| STAMPEDE | Legal inter-layer transitions in sampled IK graph | Malhan et al. (2023) semi-constrained multilayer graph; Y. Zhang et al. (2026) graph plus GJK collision filtering |
| Ferrentino et al. | Finite-state kineto-dynamic path planning | Tringali and Cocuzza (2020) multistart whole-path NLP; Zeng et al. (2026) arm-angle retiming, abstract-level |
| Elias and Wen | Cuspidal nonsingular mode connectivity and graph cost | Salunkhe et al. (2025) robot-specific cuspidality analysis; Milenkovic et al. (2026), abstract-level |
| Boschi et al. | UR-like conditional *singular* transition event | Miyata et al. (2017) singular tracking; Milenkovic (2022) offset-wrist turning-point event |
| Weingartshofer et al. | Hard vs soft process constraints and path tolerances | Malhan et al. (2023) semi-constrained toolpath; Oelerich et al. (2025) bounded-error MPC |
| Zhang and Kikuuwe | Modeled discrete-time viability and inequalities | Li and Wang (2024) simulated multi-constraint avoidance; Y. Zhang et al. (2026) sampled geometric filtering |

**Table 2. Near-neighbor papers identified by the bounded 11 October public-web update.** These are deliberately shown outside the original 28-reference DOI count and do not acquire the evidence status of the six Table 1 papers by appearing here.

| Candidate (DOI link) | Demonstrated or reported mechanism overlap | Why not another fully compared Table 1 case | Consequence for conclusions |
|---|---|---|---|
| Milenkovic et al. (2026), [10.1016/j.mechmachtheory.2025.106314](https://doi.org/10.1016/j.mechmachtheory.2025.106314) | Alternative IK paths around singularities; near the Elias–Wen/Boschi T1 event discussion | Publisher abstract inspected; full constraint and event-domain audit not done | The six cannot be claimed to exhaust branch-transition methods |
| Zeng et al. (2026), [10.1109/LRA.2026.3732902](https://doi.org/10.1109/LRA.2026.3732902) | Joint-limited arm-angle interval continuity with velocity/acceleration retiming | IEEE abstract and task-specific humanoid evaluation; full guarantee and platform transfer unresolved | **Positive T1/T2 integration exists**; withdraw an absence claim |
| M. Zhang et al. (2026), [10.1016/j.isatra.2026.03.028](https://doi.org/10.1016/j.isatra.2026.03.028) | Feasible arm-angle intervals, joint/singularity bounds and motion-derivative smoothing | Publisher summary and simulation evidence; full mechanism guarantee not independently audited | Additional T1/T2 near neighbor, not a blanket execution certificate |
| Y. Zhang et al. (2026), [10.3390/machines14010065](https://doi.org/10.3390/machines14010065) | Layered pose graph, A* selection, joint-limit/singularity filtering, GJK collision checks for industrial grinding | **Full accessible publisher HTML article inspected**: Sections 3–4 specify sampled path-point nodes and FANUC M-20iA simulation; continuous swept-path proof not identified | **Strong graph + constraint overlap**; reported sampled checks do not establish all-interval safety |
| Z. Zhang et al. (2026), [10.1109/ICRA57385.2026.11696479](https://doi.org/10.1109/ICRA57385.2026.11696479) | Viability-constrained torque control, adjacent to T3 | Control-domain paper without identified IK branch-selection claim; IEEE record indexed after frozen search | Relevant verification comparator, not a seventh branch-selection case |

A comparison aimed specifically at graph-plus-collision planners should evaluate Y. Zhang et al. against STAMPEDE; one aimed at redundancy-interval selection plus retiming should evaluate Zeng et al. against its closest peers. Because Table 1 was organized to contrast *different mathematical objects*, not to rank every algorithm in each family, these alternatives are disclosed instead of being silently omitted. Full-text, common-benchmark assessment remains necessary for a ranking or substitution.

The new references are **not** quietly promoted into the 2026-09-29 search set. The 2026 *Machines* article receives article-level publisher inspection, while Zeng et al. (2026), M. Zhang et al. (2026) and Milenkovic et al. (2026) receive **metadata/abstract-only impact assessments**. Thus the coexistence of arm-angle continuity and bounded retiming is established as an *author-reported method*, but its precise theorem assumptions, cross-platform generality and continuous inter-sample verification remain NOT_ASSESSED here.

The **path-state object** is the key source of apparent disagreement. A graph method can be optimal without having a topology-preserving branch index; an analytic branch method can preserve joint continuity without optimizing an obstacle-aware path; and a constrained discretized solution can satisfy strong modeled inequalities without certifying their extrema between samples. Their positive achievements remain intact once the object and domain are stated correctly.

## 4. Methodological Tensions and Design Implications

### 4.1. Continuation is not a single property

The weakest useful pathwise statement is that a solver chooses a sequence of IK states with legal sampled transitions. A stronger statement identifies a reconstruction \(q(s)\) whose task error and regularity are controlled between samples. A branch-event claim adds conditions connecting the solution state across singularity or mode boundaries. All three are meaningful; the strongest is not a prerequisite for reporting the first.

The historical READ_COMPLETE corpus adds two useful counterpoints. Safeea et al. (2021) treat *closed-path repeatability*—the joint trajectory returns to its start after a closed Cartesian circuit—as an additional property beyond continuity. Malhan et al. (2023) operate with *semi-constrained* Cartesian poses; an admissible lift there is relative to a set of permissible frames, not a single prescribed pose curve.

This hierarchy clarifies the complementary roles of STAMPEDE, Elias and Wen, and Boschi. STAMPEDE searches feasible inter-layer transitions; Elias and Wen bring cuspidal path connectivity into a finite graph and workpiece-pose optimization; Boschi supplies an explicit event-conditioned switch for UR-like singular configurations. None should be evaluated as if it were designed to implement the other two's central mechanism. For integrated planning, the open interface is the mapping **candidate identity → reconstructed joint segment → admissible event**, including how the algorithm detects failure when the expected segment cannot exist.

### 4.2. The specification determines which singularity strategy is legitimate

In a fixed toolpath, changing the Cartesian motion to avoid singularity changes the task. In manufacturing, specified position or orientation windows may make that change acceptable. Weingartshofer et al.'s toleranced drawing/spraying formulation, Malhan et al.'s semi-constrained tool frames, Oelerich et al.'s bounded-error MPC, and Elias and Wen's workpiece-offset optimization illustrate different kinds of task freedom absent from a strictly fixed-base-frame path claim. These freedoms should not be pooled as a single tolerance model: orientation windows, path-error corridors and rigid placement changes have distinct feasible sets. Conversely, Boschi's singular crossing is valuable precisely where the assigned path must remain kinematically admissible through a singular event and the chosen robot architecture dictates a branch change.

There is no conflict in reporting all three approaches as effective within their intended tasks. The engineering conflict arises only when a system specification silently alternates between **exact toolpath**, **toleranced toolpath**, and **free placement of a fixed workpiece-relative path**. A benchmark must freeze that choice before comparing success, cost or robustness.

### 4.3. Finite feasibility and continuous execution use different domains

Node, edge and controller-step constraints can be powerful. STAMPEDE tests legal graph transitions; Ferrentino et al. compute state and time-dependent bounds on discretized decisions; Zhang and Kikuuwe provide discrete viability reasoning; Weingartshofer et al. use hard inequalities in nonlinear process planning. Their discretizations are not defects in themselves: they enable combinatorial search and practical optimization. The additional requirement for a continuous physical execution claim is to specify the interpolation/controller command and check the claimed extrema over the resulting time/geometry domain.

A minimal illustrative counterexample captures the distinction: two collision-free sampled configurations may be joined by an interpolated link motion that intersects an obstacle. Similarly, derivative and torque extrema can occur between time samples. This observation is a **geometric and numerical domain distinction**, not a claimed experimental failure of any named method. The expanded literature makes the distinction more specific: Tringali and Cocuzza (2020) optimize whole-trajectory constraints with multistart numerical search, whereas Li and Wang (2024) report a combined avoidance control in simulation with tracking-error trade-offs. Neither the use of whole-path decision variables nor positive simulation clearance alone establishes a universal interpolated-path certificate. The natural engineering response is an explicit inter-sample check or bound, rather than declaring the sampled method ineffective.

### 4.4. A mechanism-aware stress comparison

To test whether a proposed integrated solution genuinely joins the capabilities highlighted above, three task settings are more revealing than counting papers that contain words such as *continuous* or *constraint*:

| Benchmark setting | Applicable evidence | What is learned from comparing methods |
|---|---|---|
| Ordinary, obstacle-free prescribed path | T1a; T1b only if a mode event is claimed | Whether a graph/analytic method can select a coherent lift without forcing an irrelevant collision or torque test |
| Tight-clearance path with admissible mode or singular transition | T1a–c, event T1b, T2 geometry, T3g | Whether event feasibility survives a common collision model and a validated reconstructed path |
| Timed manufacturing path with process tolerances | T1a–c, task-specific T2, applicable T3g and T3d | Whether tolerance, geometry, retiming, payload and controller tracking can be checked on the *same* realized motion |

This is a **proposed benchmark design**, not an experiment conducted for this review. Changing from finite-node checks to interval-validated collision/dynamics changes the strength of the scientific claim; changing the application from obstacle-free IK to collision-constrained manufacturing changes which tests are applicable. A fixed denominator of “methods passing all tests” would therefore conflate different tasks. The meaningful comparison is among methods evaluated against **the same declared task**.

### 4.5. What an integrated planning interface must expose

The literature suggests a compositional software architecture with four inspectable outputs:

1. **Task specification:** exact or toleranced Cartesian path, workpiece frame, timing freedom, collision environment, robot and tool geometry.
2. **IK state and transition record:** chosen solution family/graph node, continuation segments, admissible singular/mode events and explicit rejection of inadmissible events.
3. **Realized trajectory:** interpolation or continuation \(q(s)\), timing \(s(t)\), controller resampling and configuration of any path deviation.
4. **Verification result:** checked pairs, clearance minima or certified bounds, joint/dynamic extrema on the asserted domain, and measured deviations where hardware is used.

A planner can supply only the first three and rely on a separate verifier for the fourth. The salient research problem is then **whether the composition preserves the same trajectory and assumptions**, not whether a single algorithm can simultaneously be called analytic, optimal, collision-free and experimentally proven.

The expanded corpus supplies further *positive* combinations: Safeea et al. (2021) address cyclic path repeatability, Tringali and Cocuzza (2020) optimize constrained complete tracking trajectories, Malhan et al. (2023) connect layered IK to semi-constrained process paths, and Li and Wang (2024) combine multiple avoidance objectives while acknowledging tracking error. These examples narrow any claim that the field only contains isolated branch, singularity and constraint solvers.

The bounded 11 October update establishes that several relevant integrations are **already reported**: Zeng et al. (2026) connect arm-angle interval continuity with joint-limited velocity/acceleration retiming (T1/T2), while Y. Zhang et al. (2026) combine a sampled industrial posture graph with singularity, joint-limit and collision filtering (T1 with reported finite-resolution geometric constraints). Consequently, neither graph-plus-collision selection nor arm-angle-plus-retiming should be described as a missing method combination. The narrower, conditional research question is whether a *specific integrated system*, when it claims such coverage, validates the **same reconstructed and timed joint trajectory** under its actual collision geometry, limits, singular/mode-event requirements and model assumptions. Absence of a universal continuous-time safety theorem has **not** been established from the available sources; candidate-level evidence neither proves nor disproves its presence elsewhere.

## 5. Research Directions and Reporting

### 5.1. Event-aware continuity with explicit failure states

New planning systems should expose solution identities and transitions in a form meaningful to their robot family. Repeatability of a cyclic lift (Safeea et al., 2021), stability of velocity/acceleration-level implementations (Patkó and Zelei, 2021), and admissible event semantics (Boschi et al., 2026; Miyata et al., 2017) should be reported as separate properties, because none logically implies all the others. An analytical index (Boschi et al., 2026), a redundancy coordinate (Gong et al., 2019), or a graph path (Rakita et al., 2019; Elias and Wen, 2025) need not share the same internal representation. But all can report the pre-event state, the admissibility test, the chosen successor state, and an explicit failure when no admissible successor can be realized. This would connect kinematic theory to usable, fail-closed planning interfaces.

### 5.2. Verification after reconstruction

Pathwise feasibility should be reported with the **actual reconstruction and timing** used by the controller. Inter-sample collision bounds and dynamic-envelope checks can be layered over sampled planners without discarding their graph or optimization strengths. Ferrentino et al. (2024) show how powerful a finite integrated optimization can be; Zhang and Kikuuwe (2026) show the value of disciplined discrete viability reasoning. For a system **claiming continuous-domain safety**, the report should state its verified domain, reconstruction, collision/dynamic model and margins rather than equating finite-node inequalities with inter-sample certification. This reporting proposal does not deny the T1/T2 integrations already reported in 2026 near-neighbor work or the earlier whole-path and multiple-constraint approaches (Tringali and Cocuzza, 2020; Li and Wang, 2024).

### 5.3. Comparable experiments with meaningful task fidelity

An informative comparison would report the same industrial task under three explicit variants: fixed exact path, fixed tolerance window, and adjustable workpiece placement. For each, measure feasible completion rate, branch/mode-event quality, maximum task deviation, minimum modeled clearance, joint and torque extrema, timing deviation, runtime, and hardware tracking when available. Cyclic-versus-open paths, admissible workpiece pose, exact-versus-semi-constrained orientation, and whether a constraint is a hard inequality or a weighted avoidance objective must also be fixed. Robot configuration, payload, obstacle geometry and controller rates belong in the benchmark definition because otherwise one successful UR5e transition cannot be meaningfully ranked against a Panda kineto-dynamic planner or a KUKA iiwa drawing experiment.

### 5.4. A compact reporting contract

Instead of imposing the same certificate on every paper, each claimed capability should be accompanied by the information required to interpret it:

| Claimed result | Essential reportable details |
|---|---|
| Pathwise IK selection | Robot model, task/path identity, starting state, state representation, sample/reconstruction rule, joint/task residuals |
| Singularity or mode transition | Event type and location, kinematic assumptions, successor rule, joint regularity, allowed task deviation |
| Geometric collision feasibility | Full collision geometry/pairs, margins, checking domain, interpolation and worst clearance |
| Timed/dynamic feasibility | \(s(t)\), payload/dynamics, velocity/acceleration/torque limits and extrema, resampling/interval treatment |
| Hardware execution | Command mode/rate, tool calibration, planned versus measured trajectories, tracking error and abort conditions |

This contract is a synthesis-derived **reporting proposal**. Supplementary Note S3 illustrates how it distinguishes the iiwa manufacturing example, the cuspidal graph planner, and discrete viability-based IK; those illustrations are not a formal inter-rater validation study.

## 6. Conclusion

Trajectory-consistent IK is best understood as a chain of objects: **IK solution identity, admissible pathwise continuation, event-conditioned transition, constrained trajectory reconstruction, and verification on the claimed physical domain**. The six mechanism-focused studies examined here reveal complementary strengths. Sampled graphs make long-horizon IK selection tractable; cuspidal analysis and UR-like crossing laws clarify different modes of solution connectivity; finite dynamic programming and discrete viability integrate constraints at specified resolutions; and manufacturing planners exploit tolerances while connecting geometric decisions to actual robot tasks.

The main technical implication is **interface consistency**. A branch or graph decision must refer to the same reconstructed joint motion on which collision and dynamic claims are checked. Keeping representation, domain, task fidelity, and validation distinct both improves comparison of existing work and defines concrete requirements for future integrated planners.

Publisher-level 2026 candidates already report partial and substantial integrations. Therefore our proposals concern the *scope and comparability of reported guarantees*, not a claim of globally absent integrated planning algorithms.

## 7. Scope and Data Availability

The evidence base is **topic-aligned, mechanism-selected and non-exhaustive**. Historical source accounting has not been changed: 419 Consensus Quick RIS export instances, 179 DOI-unique records, 104 CORE/ADJACENT records, 18 UNCERTAIN_FULLTEXT outside that 104, and 87 READ_COMPLETE versus 17 unavailable among the 104. The separate older uncertainty-planning 306/226 ledger is historical context, not an upstream screening denominator.

The **R4 references contain 40 unique DOIs**: 28 represented in the historical TCIK screening table and 12 documented supplements. The 28 historically screened references consist of **15 CORE_INCLUDE, 7 ADJACENT, 0 EXCLUDE, and 6 UNCERTAIN_FULLTEXT** under the unchanged original screening codes. Some of the previously unresolved titles have acquired provisional scientific relevance decisions through targeted publisher-source checks, but original recorded status has not been silently rewritten. The 12 outside-table supplements comprise eight already disclosed in R3 and four 2026 discoveries. Source, appraisal and status distinctions are itemized in S1.2, S1.4 and S1.6.

Of the 87 historical READ_COMPLETE records, **21** now appear in the formal R4 references and **66** do not. The 2026 *Machines* article has publisher full HTML inspected, while the three other newly referenced 2026 papers are cited with **abstract/metadata-only verification**, so their conditional mechanism claims must not be elevated to full-text-verified guarantees. The title-only 3R geometry candidate remains a targeted screening exception, not a formally endorsed mechanism paper.

The review does not claim search saturation, an exhaustive 2016–2026 field census, quantitative publication prevalence, or a fully validated T1/T2/T3 benchmark. It is a **bounded structured narrative synthesis**, not a systematic review. Figures, the proposed reporting contract and the benchmark design express cross-method reasoning and proposed validation criteria, not experiments or theorems newly established by this article.

## References
Beck, F., Vu, M. N., Hartl-Nesic, C. and Kugi, A. (2023). Singularity avoidance with application to online trajectory optimization for serial manipulators. *IFAC-PapersOnLine*, 56(2), 284–291. https://doi.org/10.1016/j.ifacol.2023.10.1582

Boschi, I., De Toni, A., Di Leva, R., Ida, E. and Carricato, M. (2026). Handling transitions across singularities for UR-like serial robots. *IEEE Robotics and Automation Letters*, 11(3), 2714–2721. https://doi.org/10.1109/LRA.2026.3653295

Colomé, A. and Torras, C. (2012). Redundant inverse kinematics: Experimental comparative review and two enhancements. In *2012 IEEE/RSJ International Conference on Intelligent Robots and Systems*, 5333–5340. https://doi.org/10.1109/IROS.2012.6385672

Donelan, P. S. (2007). Singularity-theoretic methods in robot kinematics. *Robotica*, 25(6), 641–659. https://doi.org/10.1017/S0263574707003748

Dulęba, I. and Karcz-Dulęba, I. (2023). Many faces of singularities in robotics. *Pomiary Automatyka Robotyka*, 27(1), 19–26. https://doi.org/10.14313/par_247/19

Elias, A. J. and Wen, J. T. (2025). Path planning and optimization for cuspidal 6R manipulators. *Journal of Mechanisms and Robotics*, 17(12), 121008. https://doi.org/10.1115/1.4069599

Faria, C., Ferreira, F., Erlhagen, W., Monteiro, S. and Bicho, E. (2018). Position-based kinematics for 7-DoF serial manipulators with global configuration control, joint limit and singularity avoidance. *Mechanism and Machine Theory*, 121, 317–334. https://doi.org/10.1016/j.mechmachtheory.2017.10.025

Faroni, M., Beschi, M. and Pedrocchi, N. (2020). Inverse kinematics of redundant manipulators with dynamic bounds on joint movements. *IEEE Robotics and Automation Letters*, 5(4), 6435–6442. https://doi.org/10.1109/LRA.2020.3013879

Ferrentino, E., Savino, H. J., Franchi, A. and Chiacchio, P. (2024). A dynamic programming framework for optimal planning of redundant robots along prescribed paths with kineto-dynamic constraints. *IEEE Transactions on Automation Science and Engineering*, 21(4), 6744–6757. https://doi.org/10.1109/TASE.2023.3330371

Gong, M., Li, X. and Zhang, L. (2019). Analytical inverse kinematics and self-motion application for 7-DOF redundant manipulator. *IEEE Access*, 7, 18662–18674. https://doi.org/10.1109/ACCESS.2019.2895741

Hauser, K. and Emmons, S. (2018). Global redundancy resolution via continuous pseudoinversion of the forward kinematic map. *IEEE Transactions on Automation Science and Engineering*, 15(3), 932–944. https://doi.org/10.1109/TASE.2018.2805878

Kieffer, J. (1992). Manipulator inverse kinematics for untimed end-effector trajectories with ordinary singularities. *The International Journal of Robotics Research*, 11(3), 225–237. https://doi.org/10.1177/027836499201100305

Lakshmi Narayanan, V., Narayan, J., Gritli, H. and Dwivedy, S. K. (2026). A decade of inverse kinematics methods for serial manipulators: A systematic review. *Journal of Field Robotics*, 43(1), 184–229. https://doi.org/10.1002/rob.70014

Li, Y. and Wang, L. (2024). Comprehensive research and analysis on obstacle–singularity–joint limit avoidance of redundant robot. *International Journal of Advanced Robotic Systems*, 21(1). https://doi.org/10.1177/17298806241233910

Malhan, R. K., Thakar, S., Kabir, A. M., Rajendran, P., Bhatt, P. M. and Gupta, S. K. (2023). Generation of configuration space trajectories over semi-constrained Cartesian paths for robotic manipulators. *IEEE Transactions on Automation Science and Engineering*, 20(1), 193–205. https://doi.org/10.1109/TASE.2022.3144673

Milenkovic, P. (2022). Optimal path crossing the orientation exclusion zone of a robot with offset wrist. *Robotica*, 40(1), 191–212. https://doi.org/10.1017/S0263574721000461

Milenkovic, P., Wang, Z. and Rodriguez, J. I. (2023). Encountering singularities of a serial robot along continuous paths at high precision. *Mechanism and Machine Theory*, 181, 105224. https://doi.org/10.1016/j.mechmachtheory.2022.105224

Milenkovic, P., Wang, Z. and Rodriguez, J. I. (2026). Encircling singularities of a serial robot to find alternative inverse-kinematic solutions. *Mechanism and Machine Theory*, 219, 106314. https://doi.org/10.1016/j.mechmachtheory.2025.106314

Miyata, S., Miyahara, S. and Nenchev, D. (2017). Analytical formula for the pseudoinverse and its application for singular path tracking with a class of redundant robotic limbs. *Advanced Robotics*, 31(10), 509–518. https://doi.org/10.1080/01691864.2017.1285721

Müller, A. (2004). Collision avoiding continuation method for the inverse kinematics of redundant manipulators. In *Proceedings of the 2004 IEEE International Conference on Robotics and Automation*, 1593–1598. https://doi.org/10.1109/ROBOT.2004.1308051

Nguyen, D. T., Nguyen, V. T. T., Do, T. and Nguyen, V. L. (2026). Multi-solution inverse kinematics for robotic manipulators via permutation-invariant set prediction. *IEEE Robotics and Automation Letters*, 11(8), 9803–9810. https://doi.org/10.1109/LRA.2026.3703280

Oelerich, T., Beck, F., Hartl-Nesic, C. and Kugi, A. (2025). BoundMPC: Cartesian path following with error bounds based on model predictive control in the joint space. *The International Journal of Robotics Research*, 44(8), 1287–1316. https://doi.org/10.1177/02783649241309354

Patkó, D. and Zelei, A. (2021). Velocity and acceleration level inverse kinematic calculation alternatives for redundant manipulators. *Meccanica*, 56, 887–900. https://doi.org/10.1007/s11012-020-01305-z

Rakita, D., Mutlu, B. and Gleicher, M. (2019). STAMPEDE: A discrete-optimization method for solving pathwise-inverse kinematics. In *2019 International Conference on Robotics and Automation (ICRA)*, 3507–3513. https://doi.org/10.1109/ICRA.2019.8793617

Reinhold, J., Baumann, H. and Meurer, T. (2023). Constrained-differential-kinematics-decomposition-based NMPC for online manipulator control with low computational costs. *Robotics*, 12(1), 7. https://doi.org/10.3390/robotics12010007

Reiter, A., Mueller, A. and Gattringer, H. (2018). On higher order inverse kinematics methods in time-optimal trajectory planning for kinematically redundant manipulators. *IEEE Transactions on Industrial Informatics*, 14(4), 1681–1690. https://doi.org/10.1109/TII.2018.2792002

Safeea, M., Bearee, R. and Neto, P. (2021). A modified DLS scheme with controlled cyclic solution for inverse kinematics in redundant robots. *IEEE Transactions on Industrial Informatics*, 17(12), 8014–8023. https://doi.org/10.1109/TII.2021.3060019

Salunkhe, D. H., Marauli, T., Müller, A., Chablat, D. and Wenger, P. (2025). Kinematic issues in 6R cuspidal robots, guidelines for path planning and deciding cuspidality. *The International Journal of Robotics Research*, 44(6), 1035–1054. https://doi.org/10.1177/02783649241293481

Tringali, A. and Cocuzza, S. (2020). Globally optimal inverse kinematics method for a redundant robot manipulator with linear and nonlinear constraints. *Robotics*, 9(3), 61. https://doi.org/10.3390/robotics9030061

Trullo, H. D. and Alban, O. A. (2025). A systematic review of inverse kinematics methods for fixed-base serial manipulators: Analytical, numerical, and machine learning methods. *International Journal of Robotics and Control Systems*, 5(3), 1808–1827. https://doi.org/10.31763/ijrcs.v5i3.1820

Trutman, P., Safey El Din, M., Henrion, D. and Pajdla, T. (2022). Globally optimal solution to inverse kinematics of 7DOF serial manipulator. *IEEE Robotics and Automation Letters*, 7(3), 6012–6019. https://doi.org/10.1109/LRA.2022.3163444

Wang, Y., Sifferman, C. and Gleicher, M. (2024). IKLink: End-effector trajectory tracking with minimal reconfigurations. In *2024 IEEE International Conference on Robotics and Automation (ICRA)*, 12165–12171. https://doi.org/10.1109/ICRA57147.2024.10611510

Weingartshofer, T., Bischof, B., Meiringer, M., Hartl-Nesic, C. and Kugi, A. (2023). Optimization-based path planning framework for industrial manufacturing processes with complex continuous paths. *Robotics and Computer-Integrated Manufacturing*, 82, 102516. https://doi.org/10.1016/j.rcim.2022.102516

Wenger, P. and Chablat, D. (2023). A review of cuspidal serial and parallel manipulators. *Journal of Mechanisms and Robotics*, 15(4). https://doi.org/10.1115/1.4055677

Yin, Z., Wu, F., Wang, Z., Yang, J., Tan, J. and Kong, D. (2025). Dynamic programming-based offline redundancy resolution of redundant manipulators along prescribed paths with real-time adjustment. *arXiv preprint* arXiv:2411.17052v2. https://doi.org/10.48550/arXiv.2411.17052

Zeng, Z., Guo, J., Chen, J., Li, Y., Peng, S. and Pan, Y. (2026). Reliable 7-DOF manipulator execution via arm-angle selection and trajectory retiming. *IEEE Robotics and Automation Letters*, 11(11), 12919–12926. https://doi.org/10.1109/LRA.2026.3732902

Zhang, L., Du, H., Qin, Z., Zhao, Y.-J. and Yang, G. (2024). Real-time optimized inverse kinematics of redundant robots under inequality constraints. *Scientific Reports*, 14, 29754. https://doi.org/10.1038/s41598-024-81174-8

Zhang, M., Mei, S., He, H., Han, X. and Li, Z. (2026). Analytical inverse kinematics solution and global arm angle optimization method for 7-DOF redundant robotic arms without offset. *ISA Transactions*, 173, 425–436. https://doi.org/10.1016/j.isatra.2026.03.028

Zhang, Y. and Kikuuwe, R. (2026). Ensuring viability: A QP-based inverse kinematics for handling joint range, velocity and acceleration limits, as well as whole-body collision avoidance. *Journal of Intelligent & Robotic Systems*, 112(1). https://doi.org/10.1007/s10846-025-02335-z

Zhang, Y., Xiao, Q., Wan, L. and Jiang, B. (2026). Collision-free robot pose optimization method based on improved algorithms. *Machines*, 14(1), 65. https://doi.org/10.3390/machines14010065

## Supplementary Note S1. Search provenance, screening units, and citation-to-corpus reconciliation

### S1.1. Two historically distinct projects

The old **uncertainty-aware industrial trajectory-planning** Gate 1 ledger (`Satoru-1006/sci-review-gate1-uncertainty-aware-planning/SCREENING_LEDGER.csv`) has **226 records** (historically reported 306 source occurrences), with 36 `INCLUDE_FOR_FULLTEXT`, 46 `UNCERTAIN_FULLTEXT_REQUIRED`, 136 `EXCLUDE`, and eight `ABSTRACT_PENDING`. These decisions addressed an earlier, broader uncertainty-aware planning topic. They are **not** the source-count flow of the final IK-focused review and must not be mathematically subtracted from, combined with, or used to represent the later TCIK corpus.

The later **TCIK-specific** source is the separate frozen repository `Satoru-1006/trajectory-consistent-ik-literature-review`, anchored to `SEARCH_PROTOCOL.md` and 16 Quick searches in `SEARCH_LOG.csv` dated **2026-09-29**. The protocol's substantive focus is fixed-base serial manipulators, prescribed pathwise IK, branch/solution continuity, singularity events, and joint constraints.

| TCIK stage | Count | Unit and qualification |
|---|---:|---|
| Consensus Pro research-mode seeding | 1 exploratory query | Its visible estimated eligible count is not an exported record count |
| Consensus Quick C01–C16 RIS exports | **419** | Export **instances**, including within-query repeat exports and duplicates |
| DOI-normalized deduplicated records | **179** | Unique DOI-bearing records; title/abstract screen denominator |
| Abstract metadata AVAILABLE / MISSING | **161 / 18** | OpenAlex field flags; not identical to uncertain screening decisions |
| CORE_INCLUDE / ADJACENT | **30 / 74** | **104** screened-in, topic-specific working bibliography records |
| EXCLUDE / UNCERTAIN_FULLTEXT | **57 / 18** | The latter 18 are outside the 104; five have AVAILABLE abstract flags |
| Full-text READ_COMPLETE / PAYWALLED_OR_UNAVAILABLE | **87 / 17** | Statuses **within** the 104; no `NOT_STARTED` remain in the latest reading log |

The `exports/corpus_summary.json` in the frozen screening package reflects an **earlier interim full-text count**; final 87/17 full-text statuses should be taken from the later dated `FULLTEXT_READING_LOG.csv` and its 2026-10-03 README reconciliation rather than interpreted as an inconsistency in title/abstract selection. Search terms, export counts, provenance strings, DOI normalization, abstract status, and decision rationale are traceable in the named TCIK artifacts. There is no claim of exhaustive multi-database search saturation or full formal systematic-review screening.

### S1.2. R4 manuscript DOI-reference audit (2026-10-11)

R3's **28-reference** crosswalk is retained as an historical baseline: 11 CORE_INCLUDE, seven ADJACENT, two UNCERTAIN_FULLTEXT, eight outside the 179 DOI table. R4 adds twelve bibliographically identified works. A direct exact-DOI reconciliation against the frozen 179-row TCIK `SCREENING.csv` gives the following **unchanged historical statuses**, without claiming that a newly discussed paper was screened-in back in September:

| Original 179-row screening category of formally cited R4 references | Count |
|---|---:|
| CORE_INCLUDE | **15** |
| ADJACENT | **7** |
| UNCERTAIN_FULLTEXT | **6** |
| EXCLUDE | **0** |
| Cited but outside historical TCIK screening table | **12** |
| **Unique R4 reference DOIs** | **40** |

Four R4-referenced methods newly drawn from the 87 earlier completed reading records are Tringali and Cocuzza (2020), Safeea et al. (2021), Malhan et al. (2023) and Oelerich et al. (2025). Four previously undecided TCIK records newly examined for source relevance are Miyata et al. (2017), Milenkovic (2022), Patkó and Zelei (2021), and Li and Wang (2024); original decision flags remain UNCERTAIN_FULLTEXT, despite the separate R4 provisional classification in S1.6. Four completely new 2026 citations (Milenkovic, Zeng, M. Zhang, Y. Zhang) lie outside the frozen 179-row DOI table and are not retroactively included in 104.

Of the 87 READ_COMPLETE records, 21 are formally cited and 66 are uncited. The three selected outside-corpus anchor cases (STAMPEDE, Elias–Wen, Weingartshofer) remain six-case supplements rather than a representative 6/104 sample; the six-case selection was retrospective. The bibliographic inclusion of an abstract-only source does not certify its full text or all guarantee claims.

The five DOI/abstract evidence exceptions originally identified in S1.5 and newly examined 2026 candidates are followed by the R4 decision-and-impact ledger in S1.6. The full original search route for every supplement is not reconstructed; no invented source counts or PRISMA funnel are asserted.

### S1.3. Bounded reproducibility and unresolved history

The **final research question now has its own documented search protocol, dated search log, exported source set, DOI-specific screening decisions, and reading statuses**. It no longer depends on the earlier uncertainty-planning ledger for identification of its IK literature base. However, the six-case purposeful selection and the additional in-window citations do not amount to a retrospectively reproducible, fully exhaustive search of every eligible study. The original paths by which the four in-window supplements were initially discovered are not available as complete query-level logs. The 18 abstract-status MISSING entries and the 18 UNCERTAIN_FULLTEXT decisions are overlapping but **nonidentical** groups; neither is the same as the 17 included records lacking article bodies. None is recast as a verified exclusion or a negative result about the field.

### S1.4. Bounded public-web search update (11 October 2026)

**Execution and scope.** On **2026-10-11**, four focused, human-readable literature queries were executed through a **public web search index**, with publisher, IEEE Xplore and other academic landing pages inspected where indexed content was available. These were not authenticated database-native exports. The searchable topic groups were: **S01** solution-branch/pathwise tracking; **S02** singularity crossing and bifurcation; **S03** constrained differential IK, arm angle and retiming; and **S04** graph/constraint-aware path construction. The executed query texts, source links, classification and claim-impact notes are preserved in `TARGETED_SEARCH_UPDATE.csv`. Results are a purposively recorded set of impact-relevant candidates, **not a complete retrieval count or statistically representative source pool**. Publisher pages were sometimes accessible only through indexed excerpts. No new paper was counted as FULLTEXT_VERIFIED.

**DOI comparison.** The new candidate DOIs `10.1016/j.mechmachtheory.2025.106314` (Milenkovic, Wang and Rodriguez, 2026), `10.1109/LRA.2026.3732902` (Zeng et al., 2026), `10.1016/j.isatra.2026.03.028` (Zhang et al., 2026), `10.3390/machines14010065` (2026 collision-free posture-graph optimization), and `10.1109/ICRA57385.2026.11696479` (2026 viability-preserving torque control) are **absent from the original 179 DOI-unique TCIK rows**. That absence records non-membership in the 2026-09-29 set, not proof of a defective original decision; some works were indexed/published later. In contrast `10.1109/LRA.2026.3653295` (Boschi et al.) and `10.1007/s10846-025-02335-z` (Zhang and Kikuuwe) are already present. No earlier decisions were silently rewritten.

**Preliminary impact appraisal (publisher metadata/abstracts, and selected open Machines article sections; NOT a complete five-paper full-text audit or final eligibility).**
- **S02:** Milenkovic et al. (2026) explicitly discuss alternative IK solutions reached by singularity-related continuous paths, potentially sharpening the branch-transition and topology discussion (T1). No demonstration of collision/dynamic feasibility or whole-path certification is inferred from the accessed record.
- **S03:** Zeng et al. (2026) combine interval-based arm-angle continuity under joint limits with finite-horizon velocity/acceleration retiming (T1/T2). Because the abstract reports experiments on a humanoid platform, transfer and eligibility for a fixed-base industrial-serial scope require full-text inspection. Its reported success rate is not transplanted as a field-wide guarantee.
- **S03:** Zhang et al. (2026, *ISA Transactions*, DOI `10.1016/j.isatra.2026.03.028`) report arm-angle selection and trajectory kinematic limits (T1/T2); validation domain and formal guarantee strength remain uncertain without full text.
- **S04:** *Collision-Free Robot Pose Optimization Method Based on Improved Algorithms* (2026, DOI 10.3390/machines14010065) is a close **graph-plus-constraints** comparator. Publisher Section 3.1 describes discretized path-point graph nodes filtered for joint bounds, manipulability and GJK collisions, and Section 4 reports FANUC M-20iA simulations. This is positive evidence of that combination at the reported sampled/planned domain, **not a separately established continuous swept-path guarantee**.
- **S03 contextual:** *Viability-Preserving Passive Torque Control* (ICRA 2026, DOI `10.1109/ICRA57385.2026.11696479`) concerns constrained torque control and modeled viable sets, not itself evidence for a branch-tracking IK method. It is adjacent benchmark/verification context, not a new IK core paper.

**Consequence.** The revised synthesis avoids any claim that no integrated T1/T2 methodology exists. Its six-case comparison is a **bounded mechanism sample**; T1/T2 integration is positively reported by near neighbors, while a claimed **field-wide absence** of any system satisfying the applicable T1/T2/T3 obligations on a common verified continuous domain remains **UNVERIFIED** without full-text appraisal of these candidates and a reproducible multi-database search. This public-web update is recorded as executed, whereas Scopus/Web of Science systematic coverage, database-native IEEE export, complete citation chasing, and independent full-text screening of additions remain **NOT_DONE**.

**Historical-source reconciliation.** Direct recount of the earlier project's `SCREENING_LEDGER.csv` found 226 unique record IDs whose `raw_hit_count` sum is 306. Direct recount of the separate TCIK `exports/records_raw.csv`, `exports/records_deduplicated.csv`, `SCREENING.csv`, and `FULLTEXT_READING_LOG.csv` found 419 instances, 179 DOI-unique records, 30/74/57/18 dispositions, and 87/17 full-text statuses. The 104 retained DOIs **and normalized titles** match the full-text log one-to-one. These two flows are separate, not a 306→226→104→87 funnel. Source and counting limitations are documented in `SEARCH_PROVENANCE_RECONCILIATION.md`.

### S1.5. Post-hoc screening cross-tab and targeted correction queue (11 October 2026)

The frozen SCREENING.csv has 179 rows. Screening dispositions and abstract metadata are separate columns, with the following independently recounted cross-tabulation:

| Abstract flag / Screening decision | CORE_INCLUDE | ADJACENT | EXCLUDE | UNCERTAIN_FULLTEXT | Total |
|---|---:|---:|---:|---:|---:|
| AVAILABLE | 30 | 74 | 52 | 5 | **161** |
| MISSING | 0 | 0 | 5 | 13 | **18** |
| **Total** | **30** | **74** | **57** | **18** | **179** |

The five **AVAILABLE + UNCERTAIN_FULLTEXT** records retain stale decision rationales that say no abstract was available. Four carry meaningful text and one is only a graphical-abstract label:

| DOI | Available evidence and status correction | Action, not a final eligibility decision |
|---|---|---|
| [10.1080/01691864.2017.1285721](https://doi.org/10.1080/01691864.2017.1285721) | The field says only “Graphical Abstract”; **no usable prose abstract verified** | Keep uncertain; obtain readable abstract or full text |
| [10.1017/S0263574721000461](https://doi.org/10.1017/S0263574721000461) | Substantive offset-wrist singular-path-crossing abstract; publisher record found | Re-screen under T1; prior no-abstract rationale incorrect |
| [10.1007/s11012-020-01305-z](https://doi.org/10.1007/s11012-020-01305-z) | Substantive velocity/acceleration-level serial-manipulator IK abstract | Re-screen for constrained differential-IK relevance |
| [10.1177/17298806241233910](https://doi.org/10.1177/17298806241233910) | Substantive obstacle/singularity/joint-limit-avoidance abstract | Re-screen; avoid equating avoidance with crossing |
| [10.3390/robotics13060091](https://doi.org/10.3390/robotics13060091) | Substantive FANUC CRX 6R IK/solution-set abstract | Re-screen to distinguish pose-level IK from pathwise selection |

Of five **MISSING + EXCLUDE** records, four have an apparently reasonable **title-level platform mismatch**: a five-axis hybrid robot (DOI 10.1016/j.rcim.2018.06.003), a pneumatic continuum manipulator (10.1007/978-981-16-1769-0_1), a dual-arm space robot (10.1016/j.actaastro.2022.03.024), and a parallel robot (10.1016/j.mechmachtheory.2024.105865). Their recorded rationales should reference title-based **architecture/scope exclusions** rather than falsely imply abstract-based evidence about method absence. The fifth, *Geometry Based Analysis of 3R Serial Robots* ([10.1007/978-3-031-08140-8_8](https://doi.org/10.1007/978-3-031-08140-8_8)), is a serial-robot title; absence of path-level relevance cannot be established from its title alone and **RE_SCREEN_REQUIRED** is the defensible action.

These ten exception annotations repair the **manuscript's evidence-state interpretation**; they do **not** silently rewrite the frozen 179 historical decisions. Formal re-screening outcome counts remain **NOT_ASSESSED**, pending saved DOI-specific decisions. This distinction prevents mixing an auditable correction queue with an unperformed screening round.

**Reading-to-claim audit.** Among 104 retained DOIs there are 87 READ_COMPLETE and 17 PAYWALLED_OR_UNAVAILABLE. Under R3's original 28-reference bibliography 17 READ_COMPLETE were cited; the R4 bibliography now cites 21 READ_COMPLETE and leaves **66** READ_COMPLETE not formally referenced. Historical flags and current post-hoc scientific relevance assessments are distinct. Their logging does not prove that all their mechanisms entered the synthesis. The evidence-promoting rule is source-specific: record the method, assumptions, mathematical/verification domain, validation type and exact support for each major claim before using a source to support, contradict, or generalize a conclusion.



### S1.6. R4 targeted screening correction and 2026 full-text impact boundary

**Separate evidence/decision layers.** Original `SCREENING.csv` decisions remain a dated historical ledger; this R4 correction **does not** overwrite them. The following judgments are **post-hoc provisional topic-aligned dispositions**, not an independent 179-record prospective screen, and were applied to the frozen fixed-base serial pathwise-IK review question. Full-text inspected indicates accessible publisher HTML with substantial article content, not independently reproduced experiments or full equation-by-equation mathematical proof.

| Historical DOI | Historical state | R4 provisional disposition | Evidence actually inspected | Claim consequence |
|---|---|---|---|---|
| 10.1080/01691864.2017.1285721, Miyata et al. (2017) | UNCERTAIN_FULLTEXT | CORE_CANDIDATE | Journal listing / indexed abstract, **not entire article** | Direct singular-path pseudoinverse tracking; full proof assumptions remain UNVERIFIED |
| 10.1017/S0263574721000461, Milenkovic (2022) | UNCERTAIN_FULLTEXT | CORE_CANDIDATE | Cambridge published abstract/metadata, **full PDF not independently read here** | Offset-wrist turning-point mechanism, not interchangeable with UR-like event index |
| 10.1007/s11012-020-01305-z, Patkó and Zelei (2021) | UNCERTAIN_FULLTEXT | ADJACENT_METHOD | Springer full published HTML, including stability and conclusion | Velocity/acceleration IK stability does not establish branch/swept-path safety |
| 10.1177/17298806241233910, Li and Wang (2024) | UNCERTAIN_FULLTEXT | CORE_CANDIDATE | SAGE full published HTML, including methodology, figures and limitations | Positive multi-constraint avoidance, finite simulation with tracking-error trade-off |
| 10.1007/978-3-031-08140-8_8, Salunkhe et al. (2022) | EXCLUDE | ADJACENT_CANDIDATE_NOT_CITED | Chapter title/metadata only | 3R cuspidal geometry may be theoretical context; no demonstrated pathwise planning verified |

Four `MISSING + EXCLUDE` entries about hybrid, continuum, space dual-arm and parallel platforms retain title-based architecture mismatch and their original EXCLUDE dispositions. Their historical rationales overstated abstract-based absence in some cases; R4 does not relabel the original ledger. The fifth title-only 3R serial-robot exclusion is the adjacent candidate above, not a newly affirmed full-text core paper. A separate label-only "Graphical Abstract" cannot stand in for a scientific prose abstract.

**2026 candidate impact checks, not an exhaustive full-text-completed search:**

| New DOI | Evidence level this revision | Impact appraisal |
|---|---|---|
| 10.3390/machines14010065, Y. Zhang et al. | Publisher **full open HTML** inspected, Sections 3–4 | Industrial FANUC graph + joint/singularity/GJK collision filtering is a substantive positive T1/T2 sampled-domain comparator to STAMPEDE/Weingartshofer; no separately demonstrated swept-continuous certificate |
| 10.1109/LRA.2026.3732902, Zeng et al. | IEEE article metadata and abstract **only** | IAS continuity plus finite-horizon velocity/acceleration retiming is positive reported T1/T2; humanoid validation limits platform transfer; full assumptions NOT_ASSESSED |
| 10.1016/j.isatra.2026.03.028, M. Zhang et al. | Elsevier/PubMed article metadata and abstract **only** | Arm-angle interval optimization is a close constrained redundancy comparator; exact theorem/experimental-domain appraisal PENDING |
| 10.1016/j.mechmachtheory.2025.106314, Milenkovic et al. | Elsevier publisher abstract and highlights **only** | Encircling singularities suggests alternative IK path connectivity; precise event proof/collision domain PENDING |
| 10.1109/ICRA57385.2026.11696479, viability-control work | Indexed conference metadata **only**, not cited as IK-core | Control/viability comparator; indexed after the 29 September frozen date; not a core branch-selection claim |

**Consequence for manuscript claims.** The R4 main text gives positive credit to reported cyclic, multi-constraint, semi-constrained-path and arm-angle/retiming integrations. It narrows the proposed open problem to compatibility of task specifications, reconstructed trajectory and verification domain, rather than asserting that graph-plus-collision or T1/T2 integration is absent. **FULLTEXT_VERIFIED is NOT claimed for the three abstract-only 2026 references or the two publisher-abstract-only 2017/2022 works.** The present revision materially strengthens evidence triangulation but does not certify recall, inter-sample feasibility or cross-platform method dominance. Independent full-text study of these pending candidates remains required before any stronger comparative ranking.

## Supplementary Note S2. Claim-to-source locators and source-version distinctions

| Evidence key | Version and locator directly consulted | Bounded positive finding |
|---|---|---|
| **R19-01** | Rakita et al. (2019), [author PDF](https://graphics.cs.wisc.edu/Papers/2019/RMG19/19_ICRA_Stampede.pdf), §IV-A/B | Layered graph with node-and-edge admissibility; finite-graph dynamic-programming optimum. |
| **F24-01** | Ferrentino et al. (2024), [institutional accepted PDF](https://ris.utwente.nl/ws/portalfiles/portal/328327609/A_Dynamic_Programming_Framework_for_Optimal_Planning_of_Redundant_Robots_Along_Prescribed_Paths_With_Kineto-Dynamic_Constraints.pdf), §II-B Eqs. (17)–(22), §III Algorithm 1, §IV | Discrete state, derivative, torque and torque-rate feasibility; Panda experiments. |
| **EW25-01** | Elias and Wen (2025), [author arXiv v2](https://arxiv.org/abs/2501.18505), §4.2 Eqs. (9)–(12), §5 and §6 | Cuspidal path graph, optional sign-based nonsingularity policy and workpiece-offset optimization. Formal reference is the **journal** DOI 10.1115/1.4069599; paper-specific preprint page numbers are not assumed to match the journal layout. |
| **B26-FT-01** | Boschi et al. (2026), [published full paper](https://cris.unibo.it/handle/11585/1039115), §II-B Eqs. (13)–(14), §III-A Eqs. (15)–(17), §III-B Algorithm 1, §IV experiments and Conclusion | Architecture-specific factor/index transition at kinematically admissible crossings; UR5e evaluation. The Eq. (17) velocity parameter is part of threshold design, not a speed-limit certificate. |
| **W23-01** | Weingartshofer et al. (2023), [open article](https://doi.org/10.1016/j.rcim.2022.102516), Eq. (13b), §5.3.3 Eqs. (36)–(37), §5.3.4 Eqs. (40)–(44), §5.5, §6 | Hard joint bounds and collision inequality separated from collision, movement and joint-margin **penalties**; toleranced process paths; iiwa physical drawing and KR8 simulated spraying. |
| **ZK26-01** | Zhang and Kikuuwe (2026), [author-hosted published copy](https://home.hiroshima-u.ac.jp/kikuuwe/pub/26_jirs.pdf), §2.1 Eq. (2), §2.2 Lemma 1/Eq. (10), §2.3 Eqs. (13)–(16), (22)–(23), §5 | Discrete-time modeled viability and numerical evaluation with compound joint and approximate collision inequalities. |

An evidence key denotes **one source proposition** irrespective of how many tables repeat it. Graph feasibility, task-continuity evidence, physical demonstration, and independent interval certification are separate observation types. Publisher-format inspection was performed for Boschi and Weingartshofer; the other specific technical locators refer to the identified author or institutional versions. For Elias and Wen, correspondence of every equation number with the 2025 journal layout has not been independently verified.



**R4 complementary-source locator ledger (distinct from six anchor case source keys).** This section records what was actually consulted rather than assigning invented equation locators to a secondary abstract. Tringali and Cocuzza (2020): historical READ_COMPLETE log, article Sections 3–5, DOI 10.3390/robotics9030061; Safeea et al. (2021): historical READ_COMPLETE log, Sec. III and simulation/hardware discussion, DOI 10.1109/TII.2021.3060019; Malhan et al. (2023): historical READ_COMPLETE log, graph/formulation and evaluation sections, DOI 10.1109/TASE.2022.3144673; Oelerich et al. (2025): historical READ_COMPLETE log, online bounded-path formulation and evaluation, DOI 10.1177/02783649241309354. Patkó and Zelei (2021): Springer published article Secs. 2–4; Li and Wang (2024): SAGE published article method/simulation/conclusion; Y. Zhang et al. (2026): *Machines* publisher full text Sections 3–4. Miyata et al. (2017), Milenkovic (2022), Zeng et al. (2026), M. Zhang et al. (2026), Milenkovic et al. (2026): **publisher/indexed abstracts and metadata only**, with detailed source-level theorem and numerical checks NOT_ASSESSED.

## Supplementary Note S3. Three reporting examples

| Report item | Weingartshofer et al. (2023) | Elias and Wen (2025) | Zhang and Kikuuwe (2026) |
|---|---|---|---|
| Geometric task | Toleranced drawing / spraying toolpath | Cuspidal 6R path and workpiece placement | Differential end-effector tracking |
| IK and event | Multi-start nonlinear joint-path planning; passage permitted | Sampled all-solutions graph; optional sign-restricted edges | Discrete QP, no stated event-index mechanism |
| Declared constraints | Eq.13b hard joint limits, Eq.37 collision inequality; Eqs.36,40,42–44 penalties | Graph movement limits and optional time-conditioned edge rules; collision not integrated | State limits and approximated whole-body collision in discrete viability model |
| Reconstruction/validation | Piecewise cubic Hermite; iiwa hardware drawing and KR8 spraying simulation | Graph path with sampling and numerical examples | Discrete-time numerical simulation |
| What an integrated benchmark would additionally check | Same interpolated segment against swept-link geometry and timed limits | Link-obstacle clearance if environmental collision is introduced | Model-to-controller timing, geometry and continuous inter-sample bounds if claimed |

These cases illustrate the reporting fields' interpretability for different problem formulations; they do not estimate inter-rater agreement or certify a field-wide reporting standard.
