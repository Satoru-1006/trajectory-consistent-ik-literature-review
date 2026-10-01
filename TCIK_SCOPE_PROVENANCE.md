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
