# TCIK Scope and Provenance

**Updated:** 2026-10-02  
**Canonical project:** [Satoru-1006/trajectory-consistent-ik-literature-review](https://github.com/Satoru-1006/trajectory-consistent-ik-literature-review), branch main  
**Frozen corpus:** 104 included records (30 Core, 74 Adjacent). This update changes no paper identities, screening categories, bibliography membership, or corpus count.

## Authority and Drive reconciliation

GitHub main is the canonical source. Before this update, the current TCIK Drive folder [Trajectory-Consistent IK Literature Review (2016-2026)](https://drive.google.com/drive/folders/1hV8dgVDy2icS30s6cxFPztyId6bHkWEQ) contained copies of README.md, FULLTEXT_READING_LOG.csv, and FULLTEXT_SOURCES.csv whose normalized text exactly matched GitHub main. The current Drive folder was used only for TCIK artifacts; after this update, the same files and the new reading/provenance notes are synced there and read back.

A Drive search also surfaced GATE2A_FULLTEXT_DEEP_READING_REPORT.md in a different folder. That Gate 2A report belongs to the older uncertainty-aware project context; it was treated as read-only legacy evidence and was not imported into this TCIK paper record or synthesis. No Legacy Drive content was used to change the canonical corpus.

## Version discrepancy for DOI 10.1109/LRA.2026.3653295

The pre-update FULLTEXT_SOURCES.csv row preserved OpenAlex's location-version value submittedVersion. The [University of Bologna repository record](https://cris.unibo.it/handle/11585/1039115) for the exact same title, DOI, authors, and PDF filename explicitly labels its attachment as the publisher Version of Record and gives the licence as CC BY-NC-ND 4.0. The IEEE DOI landing-page metadata also identifies IEEE Robotics and Automation Letters, volume 11, issue 3 (March 2026), pages 2714–2721. For the reading, the institutional repository's direct file-level version label is used. The existing OpenAlex candidate field is retained as source metadata rather than silently rewritten; the conflict is made explicit in the row note and the full-text reading note.

Web Search exposed indexed full-text text for the relevant sections of the repository/publisher PDF. Subsequent normal direct PDF requests returned HTTP 403, and no access challenge was attempted. The paper note therefore records the sections read and the exact Table III numeric cells that were not available; no numerical speedup is asserted.

## This update

Only the already-included Core record at queue rank 30, DOI 10.1109/LRA.2026.3653295, was deepened. It now has a full-text note and a READ_COMPLETE row; FULLTEXT_SOURCES.csv records the repository source as read while preserving the original OpenAlex version label. The classification remains evidence for branch transitions across singularities; it does not support a claim of joint-limit, collision-clearance, or whole-path dynamic-feasibility guarantees.

## Tool use report

- UNDERMIND_USED: YES
- UNDERMIND_FULLTEXT_PAPERS: 0 (no PDF available for the five exact-DOI targets)
- UNDERMIND_CITATION_TRAILS_USED: 0
- CONSENSUS_USED: YES
- CONSENSUS_IDENTITY_CHECKS: 1 exact DOI/title/author/year/venue match
- CONSENSUS_ABSTRACT_CHECKS: 1
- CONSENSUS_FULLTEXT_PASSAGE_CHECKS: 0 (the fetch returned abstract and takeaway only)
- GITHUB_USED: YES
- CURRENT_REPO_VERIFIED: YES (private repo, main)
- LEGACY_REPO_READ_ONLY: YES (not written)
- GOOGLE_DRIVE_USED: YES
- CURRENT_DRIVE_SYNC: PASS (content readback after update)
- LEGACY_DRIVE_READ_ONLY: YES
- WEB_SEARCH_USED: YES
- VOR_CHECKS: 2 (publisher DOI metadata and institutional repository file metadata)
- REPOSITORY_FULLTEXT_RECOVERED: YES (indexed full-text extraction; direct PDF request returned 403)
- ZOTERO_USED: NO
- ZOTERO_AVAILABLE: NO (no Zotero connector in this session)
- NEW_SUPPLEMENTARY_DISCOVERIES: 0 papers
- CANONICAL_CORPUS_CHANGED: NO

## Gate 2A adjacent batch — 2026-10-02

The frozen corpus and screening categories were unchanged. The fixed batch covered ranks 50, 53, 71, 72, 78, 82, 87, 89, 90, and 91. Nine papers reached READ_COMPLETE with individual notes; rank 71 received an access note and remains PAYWALLED_OR_UNAVAILABLE. No identity check failed. ZOTERO_USED=NO; ZOTERO_AVAILABLE=NO (no connector surfaced in this session). Post-batch counts:

- Total: 104 = 36 READ_COMPLETE + 5 PAYWALLED_OR_UNAVAILABLE + 63 NOT_STARTED.
- Core: 30 = 27 / 3 / 0.
- Adjacent: 74 = 9 / 2 / 63.

Full texts were read from the publisher for ranks 53 and 82, arXiv for 50, 72, 78, 87, 90, and 91, and an author-uploaded ResearchGate copy whose journal header matches rank 89. Rank 50 is arXiv v1 rather than the 2022 RA-L Version of Record; rank 87 is a later arXiv v2 associated with its 2025 RA-L DOI. Those versions were not compared line by line and are identified in their notes. Rank 71 IEEE access returned HTTP 403, ResearchGate offered only a request for the exact journal full text, and the Academia author profile lists the exact journal metadata but no PDF link on that card; its visible PDF download belongs to a different adjacent record, and the related 2021 conference paper is not verified full text of the journal record. It remains unread; HTTP 403 is not interpreted as proof of a paywall.

PROVISIONAL evidence synthesis: ranks 89 and 91 add explicit multiple-solution/path-graph evidence and singularity-aware path choices; rank 78 adds finite-grid branch selection with joint/velocity constraints and Franka hardware while excluding singular nodes; rank 90 adds local stable near-singularity control with hardware but no joint/collision constraints. Rank 91 is a potential counterexample at the sampled graph level because it combines branch selection, optional singularity-permitting edges, and sampled joint/derivative constraints. It does not prove continuous-time, collision-free constrained feasibility between samples. Rank 87 couples collision-bounded Cartesian planning with joint-space MPC, but the authors expressly leave existence of a joint realization along every bounded path open. These observations remain provisional until the adjacent set is read.

No screening category, bibliography membership, source scope, or canonical corpus identity changed. The nine new notes and rank 71 access note contain per-paper evidence and version boundaries. The Google Drive project remains a mirror; normalized content is checked after the canonical GitHub push and the result is reported in the batch closeout.


## Remaining-63 batch 1 — 2026-10-02

Ranks 32-41 processed in rank order. Current counts: 104 = 43 READ_COMPLETE + 8 PAYWALLED_OR_UNAVAILABLE + 53 NOT_STARTED. Individual notes have the required 20 fields and source/evidence locators; inaccessible bodies remain unread. Corpus membership and screening labels unchanged. No Gate 2B work.

Current-session tool boundary: no Consensus/Undermind/Zotero MCP surfaced. Consensus website used for targeted identity discovery, but generated study snapshots contained unrelated content and were excluded; no Consensus article body counted. Undermind official website timed out. Publisher, arXiv and lawful author-hosted full text supplied the read bodies. OpenAlex/Semantic Scholar were used only to locate sources. Google Drive is the existing mirror.


## Remaining-63 batch 2 — 2026-10-02

Ranks 42-49,51-52 processed in rank order. Current counts: 104 = 53 READ_COMPLETE + 8 PAYWALLED_OR_UNAVAILABLE + 43 NOT_STARTED. Individual notes have the required 20 fields and source/evidence locators; inaccessible bodies remain unread. Corpus membership and screening labels unchanged. No Gate 2B work.


## Remaining-63 batch 3 — 2026-10-03

Ranks 54-63 processed in rank order. Current counts: 104 = 61 READ_COMPLETE + 10 PAYWALLED_OR_UNAVAILABLE + 33 NOT_STARTED. Individual notes have the required 20 fields and source/evidence locators; inaccessible bodies remain unread. Corpus membership and screening labels unchanged. No Gate 2B work.


## Remaining-63 batch 4 — 2026-10-03

Ranks 64-70,73-75 processed in rank order. Current counts: 104 = 68 READ_COMPLETE + 13 PAYWALLED_OR_UNAVAILABLE + 23 NOT_STARTED. Individual notes have the required 20 fields and source/evidence locators; inaccessible bodies remain unread. Corpus membership and screening labels unchanged. No Gate 2B work.
