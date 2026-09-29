# Search and screening protocol

**Status:** Frozen initial scope, 2026-09-29. Search date range is 2016-01-01 through 2026-09-29 (10-year window); prioritize 2021-2026 during synthesis. Do not silently widen dates or robot scope to reach a desired record count.

## Review question

For fixed-base serial manipulators, what methods produce or track a trajectory-consistent inverse-kinematics solution along a prescribed Cartesian/geometric path, particularly through or near singularities and under joint constraints?

## Search concepts

- Path/task: Cartesian path, end-effector trajectory, tool path, path following, trajectory tracking.
- IK/continuation: inverse kinematics, differential IK, resolved-rate, continuation, online/real-time IK, continuous IK, branch tracking, solution selection.
- Singularity: singularity, singular configuration, branch merging/switching, singularity-robust inverse.
- Constraints: joint limits, inequality constraints, velocity/acceleration bounds, redundancy resolution, constrained optimization.

## Consensus UI query plan

1. Broad path-continuity query: fixed-base/serial robot + trajectory/path-level IK + branch/solution continuity.
2. Singularity query: IK continuation, singularity handling and branch transitions along a path.
3. Joint-constraint query: joint-limit-aware differential/trajectory IK, with path-level continuity.
4. Targeted follow-ups for exact phrases surfaced in titles/abstracts; record every query and date in SEARCH_LOG.csv.

Use Consensus through its visible web interface. Record its displayed retrieved/eligible/included counts when present, but do not treat AI summaries or an estimated count as an exported bibliography. Export/copy actual paper records before assigning final counts.

## Eligibility

### Include in the core set
- Published 2016-01-01 to 2026-09-29.
- Fixed-base serial manipulator or a method directly applicable to one.
- Title/abstract materially addresses at least one of: path/trajectory-level IK continuation, continuity/branch selection, singularity transition/handling, or joint-constrained IK along a path.
- Peer-reviewed journal or full conference paper, with identifiable venue and stable bibliographic metadata.
- Sufficient abstract-level method and evaluation description to judge relevance and basic quality.

### Keep as adjacent/background, not core
- Redundancy resolution, constrained differential IK, or trajectory optimization with only an indirect link to branch consistency.
- General formulations validated on serial robots but not clearly path-continuous.
- Strong reviews/surveys that frame the field.
- Preprints or workshop abstracts without peer-reviewed full-paper status; label their status explicitly.

### Exclude
- Single-pose IK only, without path continuation/branch behavior/constraints relevant to the question.
- Pure manipulator design/calibration/kinematics identification, learning-only pose prediction, or motion planning with no meaningful IK continuity component.
- Mobile-base, parallel, closed-chain, or continuum robots unless the abstract directly establishes transfer to fixed-base serial arms.
- Duplicate records, editorials, abstracts without enough metadata, and low-quality/incomplete papers.

## Quality screen (title and abstract first)

Record venue/type and abstract evidence. Prioritize papers with a stated algorithm, explicit constraints or singularity treatment, and reproducible quantitative or experimental evaluation. Exclude records that are only conceptual, have no identifiable method/evaluation, or cannot be bibliographically verified. Do not rank quality by citation count alone. When evidence is insufficient at title/abstract level, use UNCERTAIN_FULLTEXT and do not silently upgrade to core inclusion.

## Screening codes

- CORE_INCLUDE: directly answers at least one main theme.
- ADJACENT: useful context, partial match, or review/background.
- EXCLUDE: out of scope, duplicate, or inadequate quality/metadata.
- UNCERTAIN_FULLTEXT: abstract insufficient to resolve quality or scope.
- Record one concise rationale and the controlling title/abstract phrase for each decision.

## Deduplication

Deduplicate first by normalized DOI; then exact normalized title + year; finally compare author/title variants. Preserve the original source and raw exported record. Do not merge records solely because titles are similar.

## Reporting

Report raw retrieved count, records exported, duplicates removed, title/abstract screened, core included, adjacent/background, excluded, and unresolved separately. A target count of 100-150 core papers is a planning range, not an inclusion quota.
