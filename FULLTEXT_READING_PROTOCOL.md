# Full-text reading protocol

**Status:** Active from 2026-09-29. This phase follows the title-and-abstract screen; it does not retroactively turn an abstract-only decision into a full-text assessment.

## Corpus

- 104 screened-in articles: 30 Core and 74 Adjacent.
- 18 additional records remain unresolved because a source abstract was not retrieved; they are not silently counted as read or included.
- Ten included records are preprints or repository records and remain labeled as such.
- Read every included article. Work through Core first, then Adjacent, while retaining a row for every record in `FULLTEXT_READING_LOG.csv`.

## Source and access rules

1. Prefer the DOI publisher page, the publisher-hosted full text, or a repository copy linked by the publisher or author.
2. For preprints, use the cited repository version and record its version/date. Do not treat a preprint as peer reviewed.
3. Record the exact landing page or PDF URL and access status. Do not infer full-text access from an abstract page or bibliographic record.
4. Do not bypass paywalls. If no lawful full text is available, record `PAYWALLED_OR_UNAVAILABLE` and keep the paper unread until a legitimate copy is supplied or located.
5. Preserve the DOI, article title, and venue from the screened bibliography; note any full-text/bibliographic mismatch instead of silently replacing the record.

## Reading pass

For each accessible full text, read the abstract and introduction, related work, problem formulation, method, assumptions, experiments or proof, results, discussion/limitations, and conclusion. Inspect equations and figures that determine the inverse-kinematics or trajectory-continuity claim. For relevant evidence, record page/section/equation/figure/table locators.

Capture these points in Chinese while retaining English technical terms where useful:

- Research question and robot/task assumptions (serial topology, fixed or moving base, DoF, redundancy, revolute/prismatic joints).
- IK representation and solution notion (pointwise, differential, continuation, branch set, configuration-space path, redundancy parameterization).
- How branch continuity, singularity approach/crossing, and joint position/velocity/acceleration limits are handled.
- Objective function, constraints, solver, guarantees or conditions, and failure cases.
- Evaluation setup, baselines, metrics, reported outcomes, and whether evidence is simulation, experiment, proof, or repository artifact.
- Authors' stated limitations and an evidence-bounded assessment of applicability to this review.

## Status vocabulary

- `NOT_STARTED`: no full text located or read.
- `LOCATED_NOT_READ`: a candidate full text exists; substantive reading has not started.
- `READING`: reading is in progress; notes are provisional.
- `READ_COMPLETE`: all relevant sections and evidence locators were checked and the record has a substantive note.
- `PAYWALLED_OR_UNAVAILABLE`: lawful full text not located; not counted as read.
- `METADATA_MISMATCH`: located full text does not confidently match the DOI/title; stop and resolve identity before counting it as read.

Only `READ_COMPLETE` counts as a completed full-text reading. Abstract-only summaries, search snippets, publisher landing pages, and AI-generated summaries do not count.
