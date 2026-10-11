# Gate 7-R2 — Search provenance reconciliation (2026-10-11)

**Authority:** separate GitHub `main` records. The two projects have different questions and are **not** successive steps in a single study-selection funnel.

## Historical project A — uncertainty-aware trajectory planning

Source: [historical screening ledger](https://github.com/Satoru-1006/sci-review-gate1-uncertainty-aware-planning/blob/main/SCREENING_LEDGER.csv).

- Independently recounted: **226 distinct record IDs**; sum of `raw_hit_count`: **306** search-hit occurrences.
- Historical decisions: 36 `INCLUDE_FOR_FULLTEXT`, 46 `UNCERTAIN_FULLTEXT_REQUIRED`, 136 `EXCLUDE`, 8 `ABSTRACT_PENDING` (=226).
- **No proven record-by-record 226→104 crosswalk.** This path is not a TCIK screening denominator.

## Final project B — trajectory-consistent IK

Sources: [SEARCH_PROTOCOL.md](SEARCH_PROTOCOL.md), [SEARCH_LOG.csv](SEARCH_LOG.csv), [exports/records_raw.csv](exports/records_raw.csv), [exports/records_deduplicated.csv](exports/records_deduplicated.csv), [SCREENING.csv](SCREENING.csv), [FULLTEXT_READING_LOG.csv](FULLTEXT_READING_LOG.csv).

- Search on **2026-09-29**: 16 Consensus Quick queries plus one Consensus Pro seeding query. The Pro displayed estimate **is not** a raw bibliography count.
- **419 rows** in `exports/records_raw.csv`; **179 rows and 179 distinct nonempty normalized DOIs** in `exports/records_deduplicated.csv`. The raw rows also have 179 distinct normalized DOIs. These counts verify exported-CSV instance and DOI-dedup accounting; no claim of independent reexecution of Consensus's interface.
- **179 rows** in `SCREENING.csv`: 30 `CORE_INCLUDE`, 74 `ADJACENT`, 57 `EXCLUDE`, 18 `UNCERTAIN_FULLTEXT`, with 179 distinct DOI keys. Equation: 179 = 30 + 74 + 57 + 18.
- **104 retained** (=30+74) map DOI-for-DOI and normalized-title-for-normalized-title to the **104 rows** in `FULLTEXT_READING_LOG.csv`, with no missing or surplus IDs. Latest read-log statuses: **87 `READ_COMPLETE`** + **17 `PAYWALLED_OR_UNAVAILABLE`**. 17 is an access status, **not necessarily a verified paywall**; 18 unresolved abstracts lie **outside** this 104.
- `exports/corpus_summary.json` retains an **earlier** full-text status snapshot (26 complete / 5 unavailable / 73 not started); use the latest full-text log and as-of **2026-10-03** README for 87/17.
- `READ_COMPLETE` denotes recorded source reading, **not universal verification of all claims**. The separate full-text 87-row evidence matrix and final six-case comparison have distinct units.

## Latest draft and supplementary discovery

- The current manuscript in [GATE7_R2_P1_TOPIC_ALIGNED_METHODS_REPAIR.md](GATE7_R2_P1_TOPIC_ALIGNED_METHODS_REPAIR.md) retains a structured **narrative** rather than systematic-review designation.
- The 2026-10-11 *public-web* S01–S04 check is logged in [TARGETED_SEARCH_UPDATE.csv](TARGETED_SEARCH_UPDATE.csv) and discussed in Supplementary Note S1.4. Its provisional candidates are **not** added retroactively to 104 or treated as read full text.
- Not performed: database-native Scopus/WoS search, exhaustive IEEE Xplore export, full citation chaining, full-text verification and final claim-impact decisions for all new candidates. `P1_TRANSPARENCY = HISTORICAL_COUNTS_VERIFIED`; `P1_COVERAGE_AND_FULLTEXT_IMPACT = PARTIAL`; `SUBMISSION_READY = NO`.

## Recalculation invariants

`306 = SUM(historical raw_hit_count)`; `226 = COUNT(historical distinct record_id)`; `419 = COUNT(raw export CSV rows)`; `179 = COUNT(DOI-unique rows)`; `179 = 30+74+57+18`; `104 = 30+74 = 87+17`. Preserve the raw records and original screening decisions.
