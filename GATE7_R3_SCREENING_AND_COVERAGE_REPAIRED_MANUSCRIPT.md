# Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators: Branch Selection, Singularity Transitions, and Joint/Path Constraints

## Abstract

A Cartesian toolpath may admit many inverse-kinematics (IK) solutions without admitting an equally obvious joint trajectory. Path-level planning must coordinate those solutions, interpret changes in posture or singularity, and connect geometric feasibility to constraints imposed on the commanded motion. This structured narrative synthesis compares six directly examined primary methods, supported by related work, along five axes: solution-state representation, singularity response, constraint domain, guarantee object, and validation. A three-part engineering lens distinguishes pathwise continuation (T1), modeled constraint enforcement (T2), and execution-domain verification when such verification is claimed (T3). The comparison reveals three consequential differences: graph-optimal selections depend on candidate and transition construction; a cuspidal nonsingular mode change is not the same kinematic event as a non-cuspidal singular crossing; and including constraints in a finite planner does not, by itself, establish their satisfaction on an interpolated, timed trajectory. Studies on UR5e singular transitions, Panda kineto-dynamic planning, and manufacturing-process paths illustrate complementary capabilities rather than a single hierarchy of methods. We outline interfaces and benchmark conditions needed to connect branch decisions to trajectory reconstruction, collision clearance, and timed execution. The review presents a mechanism-focused, bounded synthesis rather than a field-wide completeness claim.

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

Existing IK reviews principally organize solver families or kinematic architectures (Colomé and Torras, 2012; Trullo and Alban, 2025; Lakshmi Narayanan et al., 2026). The present review instead compares the *mathematical object* delivered by each approach: a candidate configuration, a continuation rule, a singularity event, a constrained finite path, or a checked executable trajectory. Its contribution is a cross-method explanation of how these objects fit together and where their guarantees cease to transfer.

## 2. Scope and Analytical Method

### 2.1. Design, topic-aligned discovery, and source selection

This article is a **structured narrative synthesis** addressing pathwise inverse kinematics (IK) of fixed-base serial manipulators. Its main evidence-discovery basis is a **separate, topic-specific trajectory-consistent-IK (TCIK) screening corpus**, rather than a retrospective restriction of the earlier uncertainty-aware trajectory-planning Gate 1 dataset. The TCIK review question, frozen in `SEARCH_PROTOCOL.md` on **29 September 2026**, asks which methods produce or track trajectory-consistent IK solutions along prescribed Cartesian/geometric paths, particularly through or near singularities and under joint constraints. The documented publication window was **1 January 2016–29 September 2026**, with older foundational publications permitted as explicitly distinguished context.

The TCIK search used a Consensus Pro research-mode query to identify search concepts and **16 recorded Consensus Quick queries** (C01–C16), including explicit terms for pathwise/continuous IK, solution branch tracking, singularity crossing or transitions, differential IK, and joint constraints. The Quick searches yielded **419 RIS export instances**, including repeated exports and cross-query duplicates; these are not 419 unique studies. DOI-based deduplication produced **179 unique records**. RIS files did not contain abstracts; the DOI-linked OpenAlex field was marked AVAILABLE for **161** records and MISSING for **18**. **Abstract status is not the screening disposition:** 13 of the MISSING records were UNCERTAIN_FULLTEXT and five were EXCLUDE, while five UNCERTAIN_FULLTEXT records were marked AVAILABLE (four with substantive abstracts and one containing only 'Graphical Abstract'). Thus, the historical screening dispositions remain **30 CORE_INCLUDE, 74 ADJACENT, 57 EXCLUDE, and 18 UNCERTAIN_FULLTEXT**, but the former explanation equating 18 missing abstracts with 18 uncertain decisions was inaccurate. This post-hoc discrepancy is disclosed and subject to record-specific re-screening in Supplementary S1.5. Thus **104 records** (30 core and 74 adjacent) entered the topic-specific working bibliography; the 18 unresolved items were *not* silently counted as included. Source-specific search strings, dates, export counts, and decisions are preserved in the TCIK repository's `SEARCH_LOG.csv`, `SCREENING.csv`, `SEARCH_PROTOCOL.md`, and original RIS exports. The 104-record `FULLTEXT_READING_LOG.csv` subsequently recorded **87 READ_COMPLETE** and **17 PAYWALLED_OR_UNAVAILABLE**; the latter status records an unsuccessful lawful-access attempt and does not necessarily establish a paywall.

The **six directly compared cases were chosen purposively for contrasting mechanisms**, not as a statistical subsample or as all methods meeting a common exhaustive eligibility standard. Three are included in the frozen 104-record TCIK bibliography: **Ferrentino et al. (2024)** (finite-grid kineto-dynamic planning), **Boschi et al. (2026)** (event-conditioned transitions for UR-like arms), and **Zhang and Kikuuwe (2026)** (modeled discrete viability). Three **in-window, source-located technical supplements were incorporated outside that 104-record screening corpus**: **Rakita et al. (2019; STAMPEDE)** (graph nodes and legal transitions), **Elias and Wen (2025)** (cuspidal solution connectivity and graph selection), and **Weingartshofer et al. (2023)** (process-tolerant manufacturing paths). They are not counted retroactively among the 104 screened-in records. Their article identities and claim-specific source locations are documented in Supplementary Note S2. This post-hoc account identifies why each belongs in the mechanism comparison; it does not reconstruct an unrecorded historical route by which each was originally discovered.

**Purposeful-selection rationale (retrospective, not preregistered).** Each of the six supplies an inspected example of a distinct path-state or transition representation, singularity/mode strategy, constraint/verification domain, and reported validation setting, with claim-specific source locations. Exactly six is an **illustrative design choice** rather than an empirically optimal number. These are not the six most cited, highest-performing or statistically representative methods. Important near neighbors that cover overlapping mechanisms, but were not given an equivalent source-level appraisal for this comparison, are disclosed in Table 2. A different objective—such as benchmarking only graph-based collision planning or arm-angle retiming—would yield a different case set.

A DOI-level check of this manuscript's **28 cited works** against the TCIK `SCREENING.csv` yielded **11 CORE_INCLUDE, seven ADJACENT, two UNCERTAIN_FULLTEXT, and eight citations absent from that screening table**. Of the eight supplementary citations, **four are pre-2016 foundational works** and **four are in-window additions** (the three technical cases just named and Trullo and Alban, 2025, used as review context). The two cited `UNCERTAIN_FULLTEXT` records are contextual citations, not proof that their original screening status was resolved. Accordingly, neither the 28-reference list nor the six-case set should be presented as identical to the 104-record screened-in bibliography. Supplementary Note S1 specifies these categories and their exact identifiers.

**Evidence-use reconciliation.** Cross-matching the 87 READ_COMPLETE DOIs against the 28 formally referenced DOIs finds **17 cited READ_COMPLETE records and 70 READ_COMPLETE records not formally cited**. One additional cited ADJACENT study is among the 17 PAYWALLED_OR_UNAVAILABLE records; the two cited UNCERTAIN_FULLTEXT records are outside the 104 retained group. Reading-log completion is a record of reading activity, **not automatically a source-verified vote for a field-wide conclusion**. The 70 uncited readings are documented reading-log entries, not silently aggregated negative evidence; their individual contribution to synthesis cannot be asserted without a source-to-claim map. The decisive mechanism comparisons and bounded synthesis statements in Sections 3–5 instead rely on identifiable cited works with source-version/claim locators in Supplementary S2. A full evidence-to-claim mapping for every read article has not been established.

An **earlier, separate** uncertainty-aware industrial trajectory-planning ledger recorded **226 de-duplicated titles and 306 reported source occurrences**, but its search question and eligibility logic differed. Its historical counts are retained as project provenance **only**; they are not the denominator or a reconstructable upstream stage of the TCIK 419→179→104 screening. The present review neither asserts a 226→104 transition nor treats the two corpora as one PRISMA study-selection flow. All claims are restricted to the directly source-checked studies and the explicitly stated contextual evidence; no field-wide completeness, absence claim, or prevalence estimate is inferred.

A **bounded public-web literature check was performed on 11 October 2026** across four concept groups (S01–S04) using a general web search index and verifiable publisher/academic landing pages; exact query strings and candidate DOI-level decisions are preserved in `TARGETED_SEARCH_UPDATE.csv`. This is a supplemental discovery exercise, **not a Scopus, Web of Science, IEEE Xplore database-query export, or an exhaustive forward/backward citation screen**. DOI comparison against the original 179 TCIK records surfaced newer or otherwise unrepresented potentially relevant work. For example, Milenkovic et al. (2026; DOI 10.1016/j.mechmachtheory.2025.106314) concerns singularity-related alternative IK paths, while Zeng et al. (2026; DOI 10.1109/LRA.2026.3732902) describes arm-angle interval continuity and velocity/acceleration-aware retiming. Only discoverable abstracts/landing-page evidence was inspected for these additions; they are **pending full-text mechanism appraisal**, are **not added to the 104 historical corpus**, and do not enter the six-case evidence-grade comparison. No cross-database search saturation or unqualified field-level gap is inferred.

**Search-risk statement.** Four new DOI candidates—Milenkovic et al., Zeng et al., M. Zhang et al. in ISA Transactions, and Y. Zhang et al. in Machines—were available before 29 September 2026, yet are absent from the original 179 DOI entries. Their omission is real at the DOI-set level but does not quantify recall or prove wholesale strategy failure. The separate ICRA 2026 viability-control record was indexed in IEEE Xplore on 30 September 2026, after the frozen date, so its absence has a different temporal interpretation. A fully documented multi-database search and complete candidate impact appraisal have **not** been conducted. **SEARCH_COVERAGE_SUFFICIENT = UNVERIFIED.**

Technical propositions are attributed to the inspected source version. The Boschi analysis uses its published article; Elias and Wen's journal bibliographic record is used while detailed technical section/equation locators refer to the openly available arXiv v2 analyzed here. Supplementary Note S2 records claim-specific source locations. A *missing verification item* means only that the stated guarantee was not established in the evidence evaluated at that domain.

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

IKLink (Wang et al., 2024), offline/online redundancy adjustment (Yin et al., 2025), and temporal multi-solution selection (Nguyen et al., 2026) add further computational perspectives. Their mechanisms are relevant to reducing reconfiguration, but an empirical preference for a nearby joint solution should not be equated with an analytic branch identifier. The useful distinction is **what state the algorithm preserves**, rather than whether all methods produce visually smooth joints.

### 3.2. Three different responses to singularity

A singular configuration is a rank-deficient point of a kinematic mapping; its meaning for a path depends on the robot architecture, the chosen task, and the direction of passage. Earlier continuation methods already treated such events along prescribed tool trajectories (Kieffer, 1992), while singularity-theoretic analyses distinguish the geometry of these configurations from merely numerical conditioning (Donelan, 2007; Dulęba and Karcz-Dulęba, 2023). Three responses should not be collapsed into one notion of “singularity handling.”

**Avoidance and regularization** restrict trajectories or numerical behavior near rank loss. They are useful when a nonsingular route exists or when modest task variation is allowed (Beck et al., 2023; Milenkovic et al., 2023). Avoidance can also exclude a necessary exact-path crossing, so success must be interpreted relative to whether the toolpath may move.

**Nonsingular mode change** can occur in suitable cuspidal manipulators. Wenger and Chablat (2023), Salunkhe et al. (2025), and Elias and Wen (2025) distinguish such topology from a passage through Jacobian rank loss. The route and its existence conditions are architecture-dependent. In Elias and Wen's graph construction, restricting edges to retain the sign of \(\det J\) can enforce a *sampled nonsingularity policy*; allowing graph connections across sign changes does not alone prove the regularity of every interpolated configuration (arXiv v2, §4.2).

**Singular crossing with a branch transition** is the target of Boschi et al. (2026) for UR-like non-cuspidal structures. The authors factor the Jacobian determinant into posture-related factors (published §II-B, Eqs. 13–14) and associate the signs with branch indices. When an admissible task path passes through a singular configuration, the appropriate post-event branch can differ from the pre-event branch. Their §III-A derives a threshold using the change in singularity factors between sampled commands (Eqs. 15–17); Algorithm 1 selects candidate branches and treats wrist singularity degeneracy. The threshold is a **switching/detection mechanism**, not a certification of joint-velocity bounds merely because maximum joint velocity appears in its derivation. In §IV, UR5e peg-in-hole and pick-and-place cases demonstrate the intended continuous joint evolution, while the paper conditions applicability on **kinematically admissible** paths (Conclusion). This is a specific solution to event-conditioned kinematic selection rather than a generic collision or dynamic-feasibility algorithm.

These distinctions suggest a practical question for a planner: *is the desired route feasible without a change of mode; does the chosen architecture permit nonsingular mode change; or does the fixed path require a singular passage with a valid event law?* A regularizer, a graph sign policy, and an indexed transition rule are not substitute answers.

### 3.3. Geometric, time-dependent, and process constraints

The physical meaning of constraints depends on their variables and verification domain. Joint position can be bounded during geometric IK construction. Joint velocity, acceleration, jerk, torque and torque rate require a timing law and model approximations. Obstacle clearance depends on the occupied geometry of every relevant link along the path, not merely on end-effector pose. Collision-aware continuation was already an explicit IK consideration in Müller (2004); newer constrained formulations make different tradeoffs between geometry, dynamics and computational scope.

Ferrentino et al. (2024) integrate redundancy resolution and time-related limits in dynamic programming. Their **§II-B, Eqs. (17)–(22)** encode admissible states, joint velocity/acceleration/jerk and torque/torque-rate bounds; Algorithm 1 evaluates transitions on a finite discretization. The paper reports experiments on the Franka Emika Panda (§IV). This integrates choices often separated into geometric planning and retiming, but the optimized object remains discretized; the authors also note that checking some higher-order constraints without augmenting state can compromise an unrestricted global-optimality interpretation (§III). Physical execution supports the reported hardware case, not an all-interval certificate for arbitrary controller conditions.

Zhang and Kikuuwe (2026) address differential IK through an auxiliary discrete-time viability construction (§2.1–2.3). Their Lemma 1 and modeled joint and collision inequalities provide feasibility reasoning for the stated discrete model. This is stronger than merely placing soft penalties in a tracking cost, while remaining distinct from a continuous-time swept-volume or torque-bound verification. Their simulations examine the specified discrete scheme, without transferring the result to an unmodeled actuator or environment.

Weingartshofer et al. (2023) connect geometric feasibility to manufacturing-process freedom. The paper optimizes multiple candidate joint paths, permits specified position/orientation tolerances, and uses constraints adapted to drawing and spraying. Crucially, **joint-position limits are hard constraints in Eq. (13b)**. The collision term in **Eq. (36) is a soft penalty**, while **Eq. (37) is an inequality constraint**. The nearby-joint penalty **Eq. (40)** promotes continuity, and **Eqs. (42)–(44)** penalize approaches to joint-limit boundaries; these penalties must not be mislabelled as the hard joint limits (§5.3.3–5.3.4). The paper allows kinematic singular passage, reconstructs trajectories using cubic Hermite segments (§5.5), and reports real KUKA LBR iiwa drawing and simulated KUKA KR8 spraying (§6). Its process-specific flexibility is a substantive advantage: exact fidelity to an unrelaxed path is not the problem it sets out to solve. The formulation and demonstrations do not replace a separate continuous swept-link collision or timed-dynamic verification for every reconstructed segment.

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

**Table 2. Near-neighbor papers identified by the bounded 11 October public-web update.** These are deliberately shown outside the original 28-reference DOI count and do not acquire the evidence status of the six Table 1 papers by appearing here.

| Candidate (DOI link) | Demonstrated or reported mechanism overlap | Why not another fully compared Table 1 case | Consequence for conclusions |
|---|---|---|---|
| Milenkovic et al. (2026), [10.1016/j.mechmachtheory.2025.106314](https://doi.org/10.1016/j.mechmachtheory.2025.106314) | Alternative IK paths around singularities; near the Elias–Wen/Boschi T1 event discussion | Publisher abstract inspected; full constraint and event-domain audit not done | The six cannot be claimed to exhaust branch-transition methods |
| Zeng et al. (2026), [10.1109/LRA.2026.3732902](https://doi.org/10.1109/LRA.2026.3732902) | Joint-limited arm-angle interval continuity with velocity/acceleration retiming | IEEE abstract and task-specific humanoid evaluation; full guarantee and platform transfer unresolved | **Positive T1/T2 integration exists**; withdraw an absence claim |
| M. Zhang et al. (2026), [10.1016/j.isatra.2026.03.028](https://doi.org/10.1016/j.isatra.2026.03.028) | Feasible arm-angle intervals, joint/singularity bounds and motion-derivative smoothing | Publisher summary and simulation evidence; full mechanism guarantee not independently audited | Additional T1/T2 near neighbor, not a blanket execution certificate |
| Y. Zhang et al. (2026), [10.3390/machines14010065](https://doi.org/10.3390/machines14010065) | Layered pose graph, A* selection, joint-limit/singularity filtering, GJK collision checks for industrial grinding | Publisher Sections 3.1 and 4 describe discretized path-point nodes and simulation; continuous swept-path verification not established | **Strong graph + constraint overlap**; reported geometric checks do not automatically yield a continuous-time bound |
| Z. Zhang et al. (2026), [10.1109/ICRA57385.2026.11696479](https://doi.org/10.1109/ICRA57385.2026.11696479) | Viability-constrained torque control, adjacent to T3 | Control-domain paper without identified IK branch-selection claim; IEEE record indexed after frozen search | Relevant verification comparator, not a seventh branch-selection case |

A comparison aimed specifically at graph-plus-collision planners should evaluate Y. Zhang et al. against STAMPEDE; one aimed at redundancy-interval selection plus retiming should evaluate Zeng et al. against its closest peers. Because Table 1 was organized to contrast *different mathematical objects*, not to rank every algorithm in each family, these alternatives are disclosed instead of being silently omitted. Full-text, common-benchmark assessment remains necessary for a ranking or substitution.

The **path-state object** is the key source of apparent disagreement. A graph method can be optimal without having a topology-preserving branch index; an analytic branch method can preserve joint continuity without optimizing an obstacle-aware path; and a constrained discretized solution can satisfy strong modeled inequalities without certifying their extrema between samples. Their positive achievements remain intact once the object and domain are stated correctly.

## 4. Methodological Tensions and Design Implications

### 4.1. Continuation is not a single property

The weakest useful pathwise statement is that a solver chooses a sequence of IK states with legal sampled transitions. A stronger statement identifies a reconstruction \(q(s)\) whose task error and regularity are controlled between samples. A branch-event claim adds conditions connecting the solution state across singularity or mode boundaries. All three are meaningful; the strongest is not a prerequisite for reporting the first.

This hierarchy clarifies the complementary roles of STAMPEDE, Elias and Wen, and Boschi. STAMPEDE searches feasible inter-layer transitions; Elias and Wen bring cuspidal path connectivity into a finite graph and workpiece-pose optimization; Boschi supplies an explicit event-conditioned switch for UR-like singular configurations. None should be evaluated as if it were designed to implement the other two's central mechanism. For integrated planning, the open interface is the mapping **candidate identity → reconstructed joint segment → admissible event**, including how the algorithm detects failure when the expected segment cannot exist.

### 4.2. The specification determines which singularity strategy is legitimate

In a fixed toolpath, changing the Cartesian motion to avoid singularity changes the task. In manufacturing, specified position or orientation windows may make that change acceptable. Weingartshofer et al.'s toleranced drawing/spraying formulation and Elias and Wen's workpiece-offset optimization therefore embody a design freedom absent from a strictly fixed-base-frame path claim. Conversely, Boschi's singular crossing is valuable precisely where the assigned path must remain kinematically admissible through a singular event and the chosen robot architecture dictates a branch change.

There is no conflict in reporting all three approaches as effective within their intended tasks. The engineering conflict arises only when a system specification silently alternates between **exact toolpath**, **toleranced toolpath**, and **free placement of a fixed workpiece-relative path**. A benchmark must freeze that choice before comparing success, cost or robustness.

### 4.3. Finite feasibility and continuous execution use different domains

Node, edge and controller-step constraints can be powerful. STAMPEDE tests legal graph transitions; Ferrentino et al. compute state and time-dependent bounds on discretized decisions; Zhang and Kikuuwe provide discrete viability reasoning; Weingartshofer et al. use hard inequalities in nonlinear process planning. Their discretizations are not defects in themselves: they enable combinatorial search and practical optimization. The additional requirement for a continuous physical execution claim is to specify the interpolation/controller command and check the claimed extrema over the resulting time/geometry domain.

A minimal illustrative counterexample captures the distinction: two collision-free sampled configurations may be joined by an interpolated link motion that intersects an obstacle. Similarly, derivative and torque extrema can occur between time samples. This observation is a **geometric and numerical domain distinction**, not a claimed experimental failure of any named method. The natural engineering response is an explicit inter-sample check or bound, rather than declaring the sampled method ineffective.

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

The bounded 11 October update establishes that several relevant integrations are **already reported**: Zeng et al. (2026) connect arm-angle interval continuity with joint-limited velocity/acceleration retiming (T1/T2), while Y. Zhang et al. (2026) combine a sampled industrial posture graph with singularity, joint-limit and collision filtering (T1 with reported finite-resolution geometric constraints). Consequently, neither graph-plus-collision selection nor arm-angle-plus-retiming should be described as a missing method combination. The narrower, conditional research question is whether a *specific integrated system*, when it claims such coverage, validates the **same reconstructed and timed joint trajectory** under its actual collision geometry, limits, singular/mode-event requirements and model assumptions. Absence of a universal continuous-time safety theorem has **not** been established from the available sources; candidate-level evidence neither proves nor disproves its presence elsewhere.

## 5. Research Directions and Reporting

### 5.1. Event-aware continuity with explicit failure states

New planning systems should expose solution identities and transitions in a form meaningful to their robot family. An analytical index (Boschi et al., 2026), a redundancy coordinate (Gong et al., 2019), or a graph path (Rakita et al., 2019; Elias and Wen, 2025) need not share the same internal representation. But all can report the pre-event state, the admissibility test, the chosen successor state, and an explicit failure when no admissible successor can be realized. This would connect kinematic theory to usable, fail-closed planning interfaces.

### 5.2. Verification after reconstruction

Pathwise feasibility should be reported with the **actual reconstruction and timing** used by the controller. Inter-sample collision bounds and dynamic-envelope checks can be layered over sampled planners without discarding their graph or optimization strengths. Ferrentino et al. (2024) show how powerful a finite integrated optimization can be; Zhang and Kikuuwe (2026) show the value of disciplined discrete viability reasoning. For a system **claiming continuous-domain safety**, the report should state its verified domain, reconstruction, collision/dynamic model and margins rather than equating finite-node inequalities with inter-sample certification. This reporting proposal does not deny the T1/T2 integrations already reported in 2026 near-neighbor work.

### 5.3. Comparable experiments with meaningful task fidelity

An informative comparison would report the same industrial task under three explicit variants: fixed exact path, fixed tolerance window, and adjustable workpiece placement. For each, measure feasible completion rate, branch/mode-event quality, maximum task deviation, minimum modeled clearance, joint and torque extrema, timing deviation, runtime, and hardware tracking when available. Robot configuration, payload, obstacle geometry and controller rates belong in the benchmark definition because otherwise one successful UR5e transition cannot be meaningfully ranked against a Panda kineto-dynamic planner or a KUKA iiwa drawing experiment.

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

The literature base is explicitly **topic-aligned but non-exhaustive**. The independently documented, 29 September 2026 TCIK search (`SEARCH_PROTOCOL.md`, `SEARCH_LOG.csv`, `SCREENING.csv`, raw Consensus RIS exports, and `FULLTEXT_READING_LOG.csv`) supplies the relevant 2016–2026 discovery and screening provenance: 419 export instances, 179 DOI-unique records, 104 screened-in core/adjacent papers, 18 unresolved abstracts outside that inclusion count, and 87 completed versus 17 unavailable full-text reading statuses among the 104. These are different counting units and should not be collapsed into one notion of articles reviewed.

The 18 abstract-status MISSING records and the 18 UNCERTAIN_FULLTEXT dispositions overlap in only 13 records, as audited in S1.5. The 104/57/18 historical dispositions remain frozen pending targeted re-screening. Of the 87 records with a READ_COMPLETE log status, only 17 appear in the formal 28-DOI reference list; the remaining 70 are not automatically treated as evidence for a synthesized claim.

The manuscript's 28 references are **not coterminous with** those 104 records. A retrospective DOI audit of the cited bibliography found 20 present in the TCIK screening table (including two still marked `UNCERTAIN_FULLTEXT`) and eight explicit supplements: four pre-window foundations and four in-window topic-relevant works. Three of the six directly discussed mechanisms were screened-in TCIK records; three were targeted supplements. These supplements are source-located but are not retroactively presented as having followed the 29 September screening pipeline.

The 11 October 2026 public-web search update is recorded separately and is **not incorporated into the historical 104, the 28 original formally cited sources, or the six full-text-checked cases**. Its provisional records can change the scope of future claims after full-text examination; this update alone cannot establish database search saturation (see S1.4 and `TARGETED_SEARCH_UPDATE.csv`).

The earlier uncertainty-aware planning ledger (306 source occurrences and 226 titles) is historical project background, not an upstream selection stage for this manuscript. No verified record-level transformation from that ledger to the TCIK corpus is claimed or required for the latter's independent traceability. Details, identifiers, original-source distinctions, and unresolved provenance boundaries appear in Supplementary Notes S1–S2.

This is a **bounded structured narrative synthesis**, not a systematic review or PRISMA-compliant evidence census. The manuscript does not estimate the prevalence of branch tracking, singularity transition, or continuous-time feasibility guarantees across the field. Claims about individual methods are limited to the specific reported mathematical and validation domains; broader conclusions are framed as cross-method interpretations and proposals.

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

Milenkovic, P., Wang, Z. and Rodriguez, J. I. (2023). Encountering singularities of a serial robot along continuous paths at high precision. *Mechanism and Machine Theory*, 181, 105224. https://doi.org/10.1016/j.mechmachtheory.2022.105224

Müller, A. (2004). Collision avoiding continuation method for the inverse kinematics of redundant manipulators. In *Proceedings of the 2004 IEEE International Conference on Robotics and Automation*, 1593–1598. https://doi.org/10.1109/ROBOT.2004.1308051

Lakshmi Narayanan, V., Narayan, J., Gritli, H. and Dwivedy, S. K. (2026). A decade of inverse kinematics methods for serial manipulators: A systematic review. *Journal of Field Robotics*, 43(1), 184–229. https://doi.org/10.1002/rob.70014

Nguyen, D. T., Nguyen, V. T. T., Do, T. and Nguyen, V. L. (2026). Multi-solution inverse kinematics for robotic manipulators via permutation-invariant set prediction. *IEEE Robotics and Automation Letters*, 11(8), 9803–9810. https://doi.org/10.1109/LRA.2026.3703280

Rakita, D., Mutlu, B. and Gleicher, M. (2019). STAMPEDE: A discrete-optimization method for solving pathwise-inverse kinematics. In *2019 International Conference on Robotics and Automation (ICRA)*, 3507–3513. https://doi.org/10.1109/ICRA.2019.8793617

Reinhold, J., Baumann, H. and Meurer, T. (2023). Constrained-differential-kinematics-decomposition-based NMPC for online manipulator control with low computational costs. *Robotics*, 12(1), 7. https://doi.org/10.3390/robotics12010007

Reiter, A., Mueller, A. and Gattringer, H. (2018). On higher order inverse kinematics methods in time-optimal trajectory planning for kinematically redundant manipulators. *IEEE Transactions on Industrial Informatics*, 14(4), 1681–1690. https://doi.org/10.1109/TII.2018.2792002

Salunkhe, D. H., Marauli, T., Müller, A., Chablat, D. and Wenger, P. (2025). Kinematic issues in 6R cuspidal robots, guidelines for path planning and deciding cuspidality. *The International Journal of Robotics Research*, 44(6), 1035–1054. https://doi.org/10.1177/02783649241293481

Trullo, H. D. and Alban, O. A. (2025). A systematic review of inverse kinematics methods for fixed-base serial manipulators: Analytical, numerical, and machine learning methods. *International Journal of Robotics and Control Systems*, 5(3), 1808–1827. https://doi.org/10.31763/ijrcs.v5i3.1820

Trutman, P., Safey El Din, M., Henrion, D. and Pajdla, T. (2022). Globally optimal solution to inverse kinematics of 7DOF serial manipulator. *IEEE Robotics and Automation Letters*, 7(3), 6012–6019. https://doi.org/10.1109/LRA.2022.3163444

Wang, Y., Sifferman, C. and Gleicher, M. (2024). IKLink: End-effector trajectory tracking with minimal reconfigurations. In *2024 IEEE International Conference on Robotics and Automation (ICRA)*, 12165–12171. https://doi.org/10.1109/ICRA57147.2024.10611510

Wenger, P. and Chablat, D. (2023). A review of cuspidal serial and parallel manipulators. *Journal of Mechanisms and Robotics*, 15(4). https://doi.org/10.1115/1.4055677

Weingartshofer, T., Bischof, B., Meiringer, M., Hartl-Nesic, C. and Kugi, A. (2023). Optimization-based path planning framework for industrial manufacturing processes with complex continuous paths. *Robotics and Computer-Integrated Manufacturing*, 82, 102516. https://doi.org/10.1016/j.rcim.2022.102516

Yin, Z., Wu, F., Wang, Z., Yang, J., Tan, J. and Kong, D. (2025). Dynamic programming-based offline redundancy resolution of redundant manipulators along prescribed paths with real-time adjustment. *arXiv preprint* arXiv:2411.17052v2. https://doi.org/10.48550/arXiv.2411.17052

Zhang, L., Du, H., Qin, Z., Zhao, Y.-J. and Yang, G. (2024). Real-time optimized inverse kinematics of redundant robots under inequality constraints. *Scientific Reports*, 14, 29754. https://doi.org/10.1038/s41598-024-81174-8

Zhang, Y. and Kikuuwe, R. (2026). Ensuring viability: A QP-based inverse kinematics for handling joint range, velocity and acceleration limits, as well as whole-body collision avoidance. *Journal of Intelligent & Robotic Systems*, 112(1). https://doi.org/10.1007/s10846-025-02335-z

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

### S1.2. Current manuscript reference audit (2026-10-11)

The 28 unique reference DOIs printed in **this manuscript** were normalized and compared with the 179 DOI entries in TCIK `SCREENING.csv`. This is a **retrospective citation-to-corpus audit**, not an unrecorded change to 2026-09-29 eligibility decisions.

| Manuscript reference category | Number | Treatment |
|---|---:|---|
| TCIK CORE_INCLUDE | **11** | Core-labeled at title/abstract screening; manuscript claims still depend on the inspected source |
| TCIK ADJACENT | **7** | Contextual/adjacent; original screening status retained |
| TCIK UNCERTAIN_FULLTEXT | **2** | Contextual citation only; screening uncertainty is **not** retroactively cleared |
| Cited but **outside** TCIK screening table | **8** | Explicit supplementary sources, itemized below |
| **All manuscript references** | **28** | Citation count ≠ 104-record corpus size ≠ six compared technical cases |

Four **pre-2016 foundational** supplements: Colomé and Torras (2012), DOI `10.1109/IROS.2012.6385672`; Donelan (2007), DOI `10.1017/S0263574707003748`; Kieffer (1992), DOI `10.1177/027836499201100305`; and Müller (2004), DOI `10.1109/ROBOT.2004.1308051`.

Four **2016–2026 in-window targeted** supplements: Rakita et al. (2019, STAMPEDE), DOI `10.1109/ICRA.2019.8793617`; Weingartshofer et al. (2023), DOI `10.1016/j.rcim.2022.102516`; Elias and Wen (2025), DOI `10.1115/1.4069599`; and Trullo and Alban (2025), DOI `10.31763/ijrcs.v5i3.1820`. Rakita, Elias–Wen, and Weingartshofer are three of the six **direct mechanism-comparison cases**. Trullo and Alban supply broader survey context. The available manuscript provenance supports their content-specific inclusion and bibliographic identity but does not establish which original search or backward-citation operation led to each citation; no such history is invented here.

The two TCIK `UNCERTAIN_FULLTEXT` references retained in manuscript context are Faria et al. (2018), DOI `10.1016/j.mechmachtheory.2017.10.025`, and Milenkovic et al. (2023), DOI `10.1016/j.mechmachtheory.2022.105224`. Their title/abstract screening status remains unresolved in the historical TCIK table, irrespective of later source-level discussion. No claim of formal rescreening is made.

Of the **six** closely examined methods in Table 1, **three are TCIK core** (Ferrentino 2024; Boschi 2026; Zhang and Kikuuwe 2026) and **three are targeted additions** (Rakita 2019; Elias and Wen 2025; Weingartshofer 2023). They are selected for distinct mechanisms, **not** because all six arise from a six-of-104 representative or randomized sampling design.

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

**Reading-to-claim audit.** Among 104 retained DOIs there are 87 READ_COMPLETE and 17 PAYWALLED_OR_UNAVAILABLE. Intersection with the original 28 formally cited DOIs: 17 cited READ_COMPLETE; one cited ADJACENT with unavailable full text; two cited UNCERTAIN records outside the 104; eight sources absent from the screening table. The remaining **70** READ_COMPLETE records are not formally referenced. Their logging does not prove that all their mechanisms entered the synthesis. The evidence-promoting rule is source-specific: record the method, assumptions, mathematical/verification domain, validation type and exact support for each major claim before using a source to support, contradict, or generalize a conclusion.

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

## Supplementary Note S3. Three reporting examples

| Report item | Weingartshofer et al. (2023) | Elias and Wen (2025) | Zhang and Kikuuwe (2026) |
|---|---|---|---|
| Geometric task | Toleranced drawing / spraying toolpath | Cuspidal 6R path and workpiece placement | Differential end-effector tracking |
| IK and event | Multi-start nonlinear joint-path planning; passage permitted | Sampled all-solutions graph; optional sign-restricted edges | Discrete QP, no stated event-index mechanism |
| Declared constraints | Eq.13b hard joint limits, Eq.37 collision inequality; Eqs.36,40,42–44 penalties | Graph movement limits and optional time-conditioned edge rules; collision not integrated | State limits and approximated whole-body collision in discrete viability model |
| Reconstruction/validation | Piecewise cubic Hermite; iiwa hardware drawing and KR8 spraying simulation | Graph path with sampling and numerical examples | Discrete-time numerical simulation |
| What an integrated benchmark would additionally check | Same interpolated segment against swept-link geometry and timed limits | Link-obstacle clearance if environmental collision is introduced | Model-to-controller timing, geometry and continuous inter-sample bounds if claimed |

These cases illustrate the reporting fields' interpretability for different problem formulations; they do not estimate inter-rater agreement or certify a field-wide reporting standard.
