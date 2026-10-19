from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "exports" / "records_with_abstracts.csv"
OUT = ROOT / "SCREENING.csv"

# The lists encode the frozen title/abstract rubric in SCREENING_PROTOCOL.md.
# CORE is limited to path-/trajectory-level behavior or a direct solution to
# branch, singularity-transition, or along-path joint-constraint handling.
CORE = [
    "A Fast Evaluation of Initial Configurations in Repeatable Inverse Kinematics",
    "A Novel Approach for a Inverse Kinematics Solution of a Redundant Manipulator",
    "Global Redundancy Resolution via Continuous Pseudoinversion",
    "On Higher Order Inverse Kinematics Methods in Time-Optimal Trajectory Planning",
    "Analytical Inverse Kinematics and Self-Motion Application for 7-DOF",
    "Inverse Kinematics with Forward Dynamics Solvers for Sampled Motion Tracking",
    "Globally Optimal Inverse Kinematics Method for a Redundant Robot Manipulator with Linear and Nonlinear Constraints",
    "Inverse Kinematics of Redundant Manipulators With Dynamic Bounds on Joint Movements",
    "A Modified DLS Scheme With Controlled Cyclic Solution",
    "Modified Configuration Control With Potential Field for Inverse Kinematic Solution",
    "Multi-Objective Swarm Intelligence Trajectory Generation",
    "Singularity Configuration Pass Algorithm of Manipulator Based on PVT Trajectory Planning",
    "A Dynamic Programming Framework for Optimal Planning of Redundant Robots Along Prescribed Paths",
    "A novel QP-based kinematic redundancy resolution method with joint constraints satisfaction",
    "An Inverse Kinematic Optimization Method for the S-R-S Redundant Manipulator",
    "Evolutionary multi-objective trajectory optimization for a redundant robot in Cartesian space",
    "Singularity Avoidance with Application to Online Trajectory Optimization for Serial Manipulators",
    "A comparison of methods solving repeatable inverse kinematics",
    "A Research on Manipulator-Path Tracking Based on Deep Reinforcement Learning",
    "Constrained-Differential-Kinematics-Decomposition-Based NMPC for Online Manipulator Control",
    "Generation of Configuration Space Trajectories Over Semi-Constrained Cartesian Paths",
    "Mathematical modeling and simulation of the inverse kinematic of a redundant robotic manipulator",
    "Time-Optimal Asymmetric S-Curve Trajectory Planning of Redundant Manipulators under Kinematic Constraints",
    "BoundMPC: Cartesian path following with error bounds",
    "IKLink: End-Effector Trajectory Tracking with Minimal Reconfigurations",
    "Kinematic issues in 6R cuspidal robots, guidelines for path planning",
    "Optimizing Redundant Robot Kinematics and Motion Planning via Advanced D-H Analysis",
    "A Multi-Objective Hybrid PSO-DLS Optimization Framework for Redundant Inverse Kinematics",
    "Ensuring Viability: A QP-based Inverse Kinematics",
    "Handling Transitions Across Singularities for UR-Like Serial Robots",
    "Continuous Gradient Projection Method for Kinematically Efficient Redundancy Resolution",
]

ADJACENT = [
    "Inverse Kinematics for Serial Kinematic Chains via Sum of Squares Optimization",
    "Online Time-Optimal Trajectory Planning for Robotic Manipulators Using Adaptive Elite Genetic Algorithm",
    "An Adaptive Second Order Sliding Mode Inverse Kinematics Approach for Serial Kinematic Chain",
    "An Efficient and Accurate Inverse Kinematics for 7-DOF Redundant Manipulators",
    "DPSO and Inverse Jacobian-Based Real-Time Inverse Kinematics With Trajectory Tracking",
    "Globally Optimal Solution to Inverse Kinematics of 7DOF Serial Manipulator",
    "Improved singular robust inverse solutions of redundant serial manipulators",
    "A Real-Time-Capable Closed-Form Multi-Objective Redundancy Resolution Scheme",
    "An Improved Weighted Gradient Projection Method for Inverse Kinematics of Redundant Surgical Manipulators",
    "Kinematics and Singularity Analysis of a 7-DOF Redundant Manipulator",
    "Singularity Avoidance of Task-redundant Robots in Pointing Tasks",
    "A Novel Solution to the Inverse Kinematics Problem of General 7R Robots",
    "Algorithm for Determining the Types of Inverse Kinematics Solutions for Sequential Planar Robots",
    "Combinations of novel hybrid optimization algorithms-based trajectory planning analysis",
    "Evolutionary multi-objective trajectory optimization for a redundant robot",
    "IK-Geo: Unified robot inverse kinematics using subproblem decomposition",
    "Inverse Kinematics Solution of Articulated Robots Using a Heuristic Approach for Optimizing Joint Displacement",
    "Machine Learning-based Framework for Optimally Solving the Analytical Inverse Kinematics for Redundant Manipulators",
    "Meta-Heuristics Based Inverse Kinematics of Robot Manipulator’s Path Tracking Capability Under Joint Limits",
    "Singular Configuration Analysis and Singularity Avoidance with Application",
    "Singularity Analysis and Complete Methods to Compute the Inverse Kinematics for a 6-DOF UR/TM-Type Robot",
    "A Concurrent Framework for Constrained Inverse Kinematics of Minimally Invasive Surgical Robots",
    "A Time-Optimal Continuous Jerk Trajectory Planning Algorithm for Manipulators",
    "An Analytical Solution for Inverse Kinematics of SSRMS-Type Redundant Manipulators",
    "DawnIK: Decentralized Collision-Aware Inverse Kinematics Solver",
    "An iterative path-following method for hyper-redundant snake-like manipulator with joint limits",
    "Adaptive Manipulability-Based Path Planning Strategy for Industrial Robot Manipulators",
    "Kinematically Constrained Jerk–Continuous S-Curve Trajectory Planning in Joint Space",
    "Fast Path Planning for Kinematic Smoothing of Robotic Manipulator Motion",
    "Collision-free path planning for welding manipulator via hybrid algorithm of deep reinforcement learning and inverse kinematics",
    "IKFlow: Generating Diverse Inverse Kinematics Solutions",
    "A Multiple Solutions Approach to the Inverse Kinematics Problem of a General Serial Manipulator",
    "PARTICLE SWARM OPTIMIZATION FOR INVERSE KINEMATICS SOLUTION AND TRAJECTORY PLANNING",
    "J-PARSE: Jacobian-based Projection Algorithm for Resolving Singularities",
    "Many-RRT*: Robust Joint-Space Trajectory Planning for Serial Manipulators",
    "Real-Time Control of Six-DOF Serial Manipulators via Learned Spherical Kinematics",
    "Direct Collocation Methods for Trajectory Optimization in Constrained Robotic Systems",
    "Inverse kinematics and path planning of manipulator using real quantifier elimination",
    "Inverse Kinematics of an Anthropomorphic 6R Robot Manipulator",
    "Manipulability maximization in constrained inverse kinematics of surgical robots",
    "Many Faces of Singularities in Robotics",
    "Obstacle Avoidance in Operational Configuration Space Kinematic Control of Redundant Serial Manipulators",
    "Path-Constrained and Collision-Free Optimal Trajectory Planning for Robot Manipulators",
    "Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators",
    "Singularity-Robust Inverse Kinematics for Serial Manipulators",
    "Time-Optimal Asymmetric S-Curve Trajectory Planning of Redundant Manipulators",
    "Closed-form solutions for the inverse kinematics of serial robots using conformal geometric algebra",
    "A modified firefly algorithm for the inverse kinematics solutions of robotic manipulators",
    "A review of cuspidal serial and parallel manipulators",
    "Singularity Avoidance with Application to Online Trajectory Optimization",
    "A Solution of the Inverse Kinematics Problem for a 7-Degrees-of-Freedom Serial Redundant Manipulator",
    "An Efficient Inverse Kinematic Method for SSRMS-type Manipulator",
    "An explicit solution of forward and inverse kinematics for a serial manipulator",
    "Analytically Informed Inverse Kinematics Solution at Singularities",
    "Automatic Geometric Decomposition for Analytical Inverse Kinematics",
    "Dynamic Programming-Based Offline Redundancy Resolution of Redundant Manipulators Along Prescribed Paths",
    "Extended Operational Space Kinematics, Dynamics, and Control of Redundant Serial Robots",
    "Online Trajectory Generation With Local Replanning for 7-DoF Serial Manipulator",
    "Real-time inverse kinematics for robotic manipulation under remote center-of-motion constraint",
    "Real-time optimized inverse kinematics of redundant robots under inequality constraints",
    "Simple Inverse Kinematics Computation Considering Joint Motion Efficiency",
    "A Decade of Inverse Kinematics Methods for Serial Manipulators",
    "A Fast and Robust Multistage Hybrid Algorithm for Inverse Kinematics of Redundant",
    "BoundPlanner: A Convex-Set-Based Approach to Bounded Manipulator Trajectory Planning",
    "Path Planning and Optimization for Cuspidal 6R Manipulators",
    "Redundancy-Based Motion Planning with Task Constraints for Robot Manipulators",
    "Time-Jerk Optimal Robotic Trajectory Planning Under Jerk and Continuity Constraints",
    "Trajectory Tracking Control of a Tendon-Actuated Manipulator with Rolling Joints",
    "A Closed-Form Inverse Kinematic Analytical Method for a Humanoid Seven-DOF Redundant Manipulator",
    "A Framework for Combining Optimization-Based and Analytic Inverse Kinematics",
    "Actuator-Aware Inverse Kinematics with Joint-Limit Admissibility",
    "MimicIK: Real-Time Generative Inverse Kinematics from Teleoperation with FK Consistency",
    "Multi-Solution Inverse Kinematics for Robotic Manipulators via Permutation-Invariant Set Prediction",
    "Optimized inverse kinematics solutions for a 6-DOF robot",
    "Singularity Avoidance in Inverse Kinematics: A Unified Treatment",
    "UR3 Collaborative Robot Inverse Kinematics Using Metaheuristic Optimization",
    "Existence Conditions and General Solutions of Closed-form Inverse Kinematics for Revolute Serial Robots",
    "Combining closed-form and numerical solutions for the inverse kinematics of six-degrees-of-freedom collaborative handling robot",
    "Comprehensive research and analysis on obstacle-singularity-joint limit avoidance of redundant robot",
    "Geometric Approach for Inverse Kinematics of the FANUC CRX Collaborative Robot",
    "Towards accuracy improvement in solution of inverse kinematic problem in redundant robot",
    "Velocity and acceleration level inverse kinematic calculation alternatives for redundant manipulators",
    "Mapping Robot Singularities through the Monte Carlo Method",
    "A novel closed-form solution for the inverse kinematics of redundant manipulators through workspace analysis",
    "Kinematic control of redundant robots with guaranteed joint limit avoidance",
    "Position-based kinematics for 7-DoF serial manipulators with global configuration control",
    "Analysis and acceleration of TORM: optimization-based planning for path-wise inverse kinematics",
    "Encountering singularities of a serial robot along continuous paths at high precision",
    "Analytical formula for the pseudoinverse and its application for singular path tracking",
    "Optimal path crossing the orientation exclusion zone of a robot with offset wrist",
    "A novel method for tracking the solution branch of serial robot inverse kinematics",
    "A Real-time Inverse Kinematics Solver for Serial Manipulators",
]

UNCERTAIN = [
    "Kinematic control of redundant robots with guaranteed joint limit avoidance",
    "A novel closed-form solution for the inverse kinematics of redundant manipulators through workspace analysis",
    "Position-based kinematics for 7-DoF serial manipulators with global configuration control",
    "Analysis and acceleration of TORM: optimization-based planning for path-wise inverse kinematics",
    "Encountering singularities of a serial robot along continuous paths at high precision",
    "Analytically Informed Inverse Kinematics Solution at Singularities",
    "Propagative Distance Optimization for Constrained Inverse Kinematics",
    "Analytical formula for the pseudoinverse and its application for singular path tracking",
    "Optimal path crossing the orientation exclusion zone of a robot with offset wrist",
    "Velocity and acceleration level inverse kinematic calculation alternatives for redundant manipulators",
    "Continuous Gradient Projection Method for Kinematically Efficient Redundancy Resolution",
    "Closed-form solutions for the inverse kinematics of serial robots using conformal geometric algebra",
    "Comprehensive research and analysis on obstacle",
    "Geometric Approach for Inverse Kinematics of the FANUC CRX Collaborative Robot",
]

EXCLUDE_QUALITY = [
    "A Hybrid Inverse Kinematic Solution for Trajectory Tracking of Industrial Robot Manipulator",
    "Inverse Kinematic Manipulation Control and Trajectory Tracking of Robotic Arm Using Trigonometric Tangential",
    "TRAJECTORY PLANNING AND SIMULATION OF A 6-DOF ROBOTIC MANIPULATOR",
    "Obstacle Avoidance Trajectory Planning for SCARA Manipulators",
]

EXCLUDE_SCOPE = [
    "mobile manipulator", "mobile manipulators", "mobile robot", "continuum", "soft robot", "soft manipulator",
    "parallel robot", "parallel manipulator", "hybrid robot", "hybrid manipulator", "serial-parallel",
    "cable-driven segmented", "space robot", "space manipulator", "bipedal robot", "bionic continuum",
    "humanoid robot minimizing", "cooperative mobile", "rail-mounted industrial robot", "five-axis hybrid",
    "5-axis hybrid", "hybrid active and passive cable", "multi-section continuum", "tendon-driven continuum",
    "multi-arm robot", "multi-arm systems", "multi-arm space", "continuum-rigid", "articulated continuum",
    "multi-segment continuum", "humanoid teleoperation", "full-body inverse kinematics",
]

def first_match(title: str, patterns: list[str]) -> str | None:
    low = title.casefold()
    for pattern in patterns:
        if pattern.casefold() in low:
            return pattern
    return None

def evidence(row: dict) -> str:
    abstract = (row.get("abstract") or "").strip()
    if abstract:
        return re.sub(r"\s+", " ", abstract)[:500]
    return "Title only; abstract unavailable in retrieved metadata. " + (row.get("title") or "")

def main():
    rows = list(csv.DictReader(SOURCE.open(encoding="utf-8-sig", newline="")))
    screened = []
    for row in rows:
        title = row.get("title", "")
        abstract = row.get("abstract", "") or ""
        combined = (title + " " + abstract).casefold()
        decision = "EXCLUDE"
        reason = "Title/abstract does not materially address path-level IK, solution-branch continuity, singularity handling, or along-path joint constraints."
        match = first_match(title, UNCERTAIN)
        if match:
            decision = "UNCERTAIN_FULLTEXT"
            reason = "Topic is indicated by the title, but no retrieved abstract was available to assess the method and evaluation; hold for full-text or source-abstract confirmation."
        elif first_match(title, CORE):
            decision = "CORE_INCLUDE"
            if any(s in combined for s in ("singular", "branch", "cuspid", "singularity")):
                theme = "path-level singularity or solution-branch behavior"
            elif any(s in combined for s in ("joint limit", "joint constraints", "kineto-dynamic", "inequality", "velocity", "acceleration")):
                theme = "joint or kineto-dynamic constraints in trajectory IK"
            else:
                theme = "trajectory-level, path-wise, or repeatable inverse kinematics"
            reason = f"Directly addresses {theme}; title/abstract describes an explicit trajectory, path-following, repeatability, singularity, or constraint method."
        elif first_match(title, ADJACENT):
            decision = "ADJACENT"
            if any(s in combined for s in ("singular", "branch", "cuspid")):
                theme = "serial/redundant IK solution sets or singularity handling, without a direct along-path result"
            elif any(s in combined for s in ("joint limit", "joint constraints", "inequality", "remote center", "constraint")):
                theme = "redundancy resolution or constrained IK that informs along-path feasibility"
            else:
                theme = "serial-robot IK or trajectory optimization that provides methods/background but does not directly establish branch continuity"
            reason = f"Retained as background because it addresses {theme}."
        elif first_match(title, EXCLUDE_QUALITY):
            decision = "EXCLUDE"
            reason = "Direct wording is present, but title/abstract or venue metadata does not provide a sufficiently verifiable method/evaluation for the core bibliography."
        elif first_match(combined, EXCLUDE_SCOPE):
            decision = "EXCLUDE"
            reason = "Robot architecture/application is outside the frozen fixed-base serial-manipulator scope."
        elif not abstract.strip() and ("inverse kinematic" in title.casefold() or "singular" in title.casefold() or "trajectory" in title.casefold()):
            decision = "UNCERTAIN_FULLTEXT"
            reason = "No retrieved abstract; title is not enough to determine whether the work materially addresses the review question or has adequate method/evaluation evidence."
        elif any(s in combined for s in ("mobile manipulator", "continuum manipulator", "parallel manipulator", "hybrid manipulator", "space robot", "space manipulator", "bipedal robot")):
            decision = "EXCLUDE"
            reason = "Robot architecture/application is outside the frozen fixed-base serial-manipulator scope."

        venue = row.get("journal_or_venue", "")
        if decision == "EXCLUDE" and any(x.casefold() in venue.casefold() for x in ("International Review of Automatic Control", "Veredas do Direito", "Scientific Journal of Intelligent Systems Research")):
            reason = "Excluded for inadequate venue/record quality after title/abstract review; no core-worthy reproducible method/evaluation was established."
        elif decision == "EXCLUDE" and "computer graphics" in combined:
            reason = "General inverse-kinematics survey from computer graphics; the title/abstract does not establish fixed-base serial-manipulator path or branch methods."
        elif decision == "EXCLUDE" and any(x in combined for x in ("dissertation", "doctoral thesis", "ph.d. thesis")):
            reason = "Thesis record rather than a peer-reviewed journal/full-conference paper; excluded from the article bibliography."
        elif decision == "EXCLUDE" and "kinematic synthesis" in title.casefold():
            reason = "The abstract describes manipulator design-parameter synthesis, not path-level inverse-kinematics branch tracking."
        elif decision == "EXCLUDE" and "trajectory" in combined and not any(x in combined for x in ("inverse kinematic", "inverse-kinematic", "ik solver")):
            reason = "Trajectory planning/control is addressed, but the title/abstract does not describe an inverse-kinematics branch or along-path constraint method."
        elif decision == "EXCLUDE" and "path planning" in combined and not any(x in combined for x in ("inverse kinematic", "inverse-kinematic", "ik solver")):
            reason = "Motion planning is the contribution; no meaningful IK continuity or solution-branch component is established in the title/abstract."
        elif decision == "EXCLUDE" and any(x in combined for x in ("inverse kinematic", "inverse-kinematic")):
            reason = "General pose-level IK solver; no trajectory continuation, branch selection, singularity transition, or relevant joint-constraint behavior is established."
        elif decision == "EXCLUDE" and "kinematic" in combined:
            reason = "General robot kinematics analysis without a title/abstract link to trajectory-level IK or the review's branch, singularity, or joint-constraint questions."
        pub_status = "PREPRINT_OR_REPOSITORY_RECORD" if "arxiv" in venue.casefold() or (row.get("doi", "").casefold().startswith("10.48550/arxiv")) else "VENUE_RECORDED"
        if "dissertation" in venue.casefold() or "thesis" in venue.casefold() or "dissertation" in title.casefold():
            pub_status = "THESIS"
        if decision == "ADJACENT" and pub_status == "PREPRINT_OR_REPOSITORY_RECORD":
            reason += " Preprint/repository status retained as adjacent only; peer-reviewed publication not confirmed from this record."
        row.update({
            "screening_decision": decision,
            "decision_rationale": reason,
            "screening_evidence": evidence(row),
            "abstract_status": "AVAILABLE" if abstract.strip() else "MISSING",
            "publication_status": pub_status,
            "full_text_checked": "NO",
        })
        screened.append(row)
    fields = list(screened[0].keys()) if screened else []
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(screened)
    counts = Counter(row["screening_decision"] for row in screened)
    print(f"screened={len(screened)} abstract_available={sum(r['abstract_status']=='AVAILABLE' for r in screened)} decisions={dict(counts)} included={counts['CORE_INCLUDE']+counts['ADJACENT']}")
    print("unmatched_titles:")
    for row in screened:
        if row["screening_decision"] == "EXCLUDE" and not row["decision_rationale"].startswith(("Robot architecture", "Direct wording", "Excluded for inadequate")):
            print("- " + row["title"])

if __name__ == "__main__":
    main()
