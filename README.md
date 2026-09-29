# Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators

Literature screening corpus for **solution-branch tracking, singularity transitions, and joint constraints**. Search window: 2016-01-01 through 2026-09-29.

## Screening result

| Stage | Records |
| --- | ---: |
| Consensus RIS export instances | 419 |
| Unique DOI records after deduplication | 179 |
| Title/abstract screened | 179 |
| Core | 30 |
| Adjacent/background | 74 |
| Included bibliography (core + adjacent) | 104 |
| Unresolved because the abstract was not retrievable | 18 |
| Excluded | 57 |

The included bibliography meets the requested 100–300 range. All 104 included records have retrievable abstracts; the 30 core papers are the direct evidence set, while 74 adjacent papers supply methods and context on redundancy resolution, singularity-robust IK, solution sets, and constrained trajectory optimization. The 18 unresolved records are kept out of `references.ris` until an abstract or full text can settle relevance and method quality.

## Search and screening

- Consensus Pro was used to seed the subtopics; its displayed “113 eligible” count is a platform estimate, not a publication count.
- Sixteen targeted Consensus Quick searches were run through the visible website and exported as RIS. Search strings, visible result counts, and export counts are in [`SEARCH_LOG.csv`](SEARCH_LOG.csv).
- RIS exports contained titles and DOI metadata but no abstracts. DOI-linked abstracts were retrieved from OpenAlex for 161 of 179 unique records. The remaining 18 have explicit missing-abstract status; Consensus AI Key Takeaways were not treated as abstracts.
- DOI deduplication retained all source-query provenance. Ten publication year/venue fields were corrected against Crossref DOI metadata; original Consensus values remain in `consensus_year` and `consensus_venue` in the enriched and screening tables.
- Screening used title and abstract only. No full text, citation chaining, or hardware evidence was assessed. This is a focused discovery corpus, not an exhaustive systematic review.

The scope, eligibility rules, screening codes, and quality criteria were frozen in [`SEARCH_PROTOCOL.md`](SEARCH_PROTOCOL.md). Counts and rationale for every screened paper are in [`SCREENING.csv`](SCREENING.csv).

## Files

- [`references.ris`](references.ris) and [`references.bib`](references.bib): 104 included records, with abstract text, DOI, and core/adjacent tags.
- [`references_core.ris`](references_core.ris): 30 direct papers.
- [`references_adjacent.ris`](references_adjacent.ris): 74 background papers.
- [`uncertain_records.ris`](uncertain_records.ris): 18 title-relevant records awaiting abstract/full-text confirmation.
- `exports/raw/`: original Consensus RIS exports.
- `exports/records_raw.csv`: all exported record instances before deduplication.
- `exports/records_deduplicated.csv`: 179 DOI-unique records before abstract enrichment.
- `exports/records_with_abstracts.csv`: enriched records, abstract provenance, and corrected DOI metadata.
- `exports/screened_included.csv`: included core and adjacent rows.
- `exports/abstracts_missing.csv`: 18 unresolved records.
- `exports/corpus_summary.json`: machine-readable counts.

## Zotero and cloud copies

The Zotero import is tagged with `trajectory-consistent-ik-review`, `TC-IK-CORE`, and `TC-IK-ADJACENT`. The GitHub repository and Drive folder hold this same screened corpus and protocol.

## Full-text reading (in progress)

- The full-text phase began after title-and-abstract screening. It reads accessible papers in full, core first, and records evidence locators and scope limits in [`FULLTEXT_READING_LOG.csv`](FULLTEXT_READING_LOG.csv) and [`READING_NOTES/`](READING_NOTES/).
- As of 2026-09-29, 12 of the 104 included papers have completed full-text notes; one additional paper is currently `PAYWALLED_OR_UNAVAILABLE` after a lawful full-text search, and 91 remain `NOT_STARTED`. `READ_COMPLETE` is used only after checking the substantive sections, methods, evaluation, and relevant figures/equations. An unavailable full text remains unread.
- Lawfully located copies are used for reading. Copyright PDFs are not included in this repository or the Drive project; local PDF and extraction scratch files are ignored under `tmp/`.
- [`FULLTEXT_READING_PROTOCOL.md`](FULLTEXT_READING_PROTOCOL.md) specifies access rules, status meanings, and the per-paper extraction fields. [`FULLTEXT_SOURCES.csv`](FULLTEXT_SOURCES.csv) records OpenAlex full-text location candidates; a candidate link does not mean that a paper has been read.
