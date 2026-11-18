# Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators

Literature screening corpus for **solution-branch tracking, singularity transitions, and joint constraints**. Search window: 2016-01-01 through 2026-09-29.

## Supplementary materials for the manuscript

This repository accompanies the review "Trajectory-Consistent Inverse Kinematics for Fixed-Base Serial Manipulators". The materials that the manuscript's data availability statement refers to are in [`supplementary/`](supplementary/):

| Folder | Content |
| --- | --- |
| [`supplementary/evidence_matrix/`](supplementary/evidence_matrix/) | The evidence matrix of the 73 pathwise IK studies (`matrix_coding.csv`, 100 coded references in total: 73 matrix studies, 7 reviews, 20 background), the coding rules (`coding_rules.md`), every count of Figure 8 with its paper list (`counts_with_lists.csv`, `heatmap_cells.csv`), the script that regenerates them (`matrix_summary.py`), the coding table of the 12 additional methods (`twelve_further_methods_table.csv`), the six core cases of Table 3 (`core_cases_table3.csv`) and four removed candidates (`excluded_R155.csv`). |
| [`supplementary/ur5e_kinematic_verification/`](supplementary/ur5e_kinematic_verification/) | The UR5e kinematic verification (Levels 1 and 2): solver and methods M1 to M3, the sufficient-condition bounds (`prop_check.py`), the adversarial-obstacle test and the M2 candidate tests (`extra_tests.py`), results, logs and figure scripts. Its own README gives the commands. |
| [`supplementary/figure_scripts/`](supplementary/figure_scripts/) | Scripts of the schematic figures (pipeline and overview). `make_fig2_R130.py` takes the variant letter `A` or `B` as its argument. |

Screening and search records of the literature corpus (`SEARCH_LOG.csv`, `SCREENING.csv`, `exports/`, `READING_NOTES/` and the protocol files) are in the repository root and are described below. In `matrix_coding.csv`, `note_status` distinguishes notes archived in this repository (`archived_in_repo`, including 44 of 73 class-M studies in `READING_NOTES/` / `FULLTEXT_READING_LOG.csv`), external reading notes not yet archived in this repository (`external_unarchived`, 28 class-M and 12 class-B rows retaining their original `reference-notes/` filenames), and entries without a separate note file (`missing`, 1 class-M [Zeng 2026], 3 class-R, 4 class-B).

## Quick reproduction

Install Python dependencies (`Python >= 3.10` recommended; tested on `3.13.16`):

```bash
pip install -r requirements.txt
```

- **Regenerate evidence matrix counts and Figure 8 data**:
  ```bash
  cd supplementary/evidence_matrix
  python matrix_summary.py
  ```
- **Re-run UR5e kinematic verification (Levels 1 & 2, bounds, adversarial obstacle, M2 sensitivity, parameter-sync)**:
  ```bash
  cd supplementary/ur5e_kinematic_verification
  python ur5e_minimal.py
  python reference_clearance_profile.py
  python prop_check.py
  python extra_tests.py
  python param_sync_check.py
  python make_figure.py
  ```

Notes on scope: `matrix_coding.csv` does not contain six cited background references (the five interval-certification studies of Section 3.1 and Schreiber and Gosselin, 2022). The root-level manuscript drafts `GATE7_R2` to `GATE7_R9` and the 50-reference counts in the sections below describe an earlier stage of the work and are kept only as history; the submitted manuscript is the reference for all numbers. Native database export records (Web of Science, Scopus, IEEE Xplore) and citation-chaining logs referenced in the manuscript are pending upload by the author to supplement `SEARCH_LOG.csv` and `TARGETED_SEARCH_UPDATE.csv`.

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

The 104-record working bibliography is within the requested 100–300 size at title/abstract screening. Core/Adjacent counts are screening-stage labels, not final full-text dispositions: reading notes identify each paper's evidence and actual relevance, and can recommend an adjacent treatment. The 30 Core candidates are the direct-evidence set from title/abstract screening; 74 adjacent papers supply context. The 18 unresolved records remain outside references.ris until relevance and method quality can be judged.

## Search and screening

- Consensus Pro was used to seed the subtopics; its displayed “113 eligible” count is a platform estimate, not a publication count.
- Sixteen targeted Consensus Quick searches were run through the visible website and exported as RIS. Search strings, visible result counts, and export counts are in [`SEARCH_LOG.csv`](SEARCH_LOG.csv).
- RIS exports contained titles and DOI metadata but no abstracts. DOI-linked abstracts were retrieved from OpenAlex for 161 of 179 unique records. The remaining 18 have explicit missing-abstract status; Consensus AI Key Takeaways were not treated as abstracts.
- DOI deduplication retained all source-query provenance. Ten publication year/venue fields were corrected against Crossref DOI metadata; during full-text review, a publisher issue header resolved one further year mismatch (Consensus/OpenAlex 2023; journal issue 2018). Original Consensus values remain in `consensus_year` and `consensus_venue` in the enriched and screening tables.
- Initial screening used title and abstract only; it did not assess full text, citation chaining, or hardware evidence. The ongoing full-text phase records those assessments separately. This is a focused discovery corpus, not an exhaustive systematic review.

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

- On 2026-10-01, Consensus MCP records were fetched and DOI-matched for all 104 included papers. The per-paper Chinese abstract-level synthesis is in [CONSENSUS_ABSTRACT_REVIEW.md](CONSENSUS_ABSTRACT_REVIEW.md), with a machine-readable companion in [CONSENSUS_ABSTRACT_REVIEW.csv](CONSENSUS_ABSTRACT_REVIEW.csv). Consensus MCP returned abstracts and takeaways, not article bodies; this abstract pass does not change full-text status.
- The full-text phase began after title-and-abstract screening. It reads accessible papers in full, core first, and records evidence locators and scope limits in [`FULLTEXT_READING_LOG.csv`](FULLTEXT_READING_LOG.csv) and [`READING_NOTES/`](READING_NOTES/).
- As of 2026-10-03, 87 of the 104 included papers have completed full-text notes; 17 additional records have status PAYWALLED_OR_UNAVAILABLE, and 0 remain NOT_STARTED. This includes a fixed ten-paper Adjacent batch at ranks 50, 53, 71, 72, 78, 82, 87, 89, 90, and 91: nine READ_COMPLETE notes and one unavailable access note (rank 71). Earlier batch counts were Core 27/3/0 and Adjacent 9/2/63 for READ_COMPLETE / PAYWALLED_OR_UNAVAILABLE / NOT_STARTED. Rank 71 HTTP 403 is recorded as access failure, not proof of a paywall. The batch synthesis is provisional; it does not freeze a research gap or taxonomy. In queue ranks 22-31, eight of ten papers have been read in full (22-27, 29, and 30); ranks 28 and 31 remain unread after the recorded access attempts. Rank 30, “Handling Transitions Across Singularities for UR-Like Serial Robots,” was read from claim-relevant sections of the publisher Version of Record identified in the University of Bologna repository. Its note records the branch-switch algorithm, wrist/shoulder singularity evidence, UR5e task, scope limits, and the Table III extraction gap. No numeric speedup is inferred from unavailable table cells. Rank 31 still has a CC BY publisher location, but its PDF request returned HTTP 403 during this session; this records an access failure, not a paywall finding. Paper 17 was read in full from the public Preprints.org v1 manuscript after the publisher PDF was blocked in the current session; the final publisher version was checked for identity and abstract but not compared line by line. Paper 18 was read from the publisher-version PDF deposited in the KITopen institutional repository. Paper 19 was read from author-uploaded public full text on ResearchGate; its version is not labelled, and numeric table cells were not available in the browser text view. Paper 20 was read from the Bournemouth University repository PDF; its record labels the copy submittedVersion, while the PDF is journal-formatted. Paper 21 was read from arXiv HTML v5, which states acceptance for IFAC World Congress 2023; the publisher PDF landing page presented a CAPTCHA, and versions were not compared line by line. READ_COMPLETE is used only after checking the substantive sections, methods, evaluation, and relevant figures/equations; source-view limits are recorded per paper. An unavailable full text remains unread.
- Lawfully located copies are used for reading. Copyright PDFs are not included in this repository or the Drive project; local PDF and extraction scratch files are ignored under `tmp/`.
- [`FULLTEXT_READING_PROTOCOL.md`](FULLTEXT_READING_PROTOCOL.md) specifies access rules, status meanings, and the per-paper extraction fields. [`FULLTEXT_SOURCES.csv`](FULLTEXT_SOURCES.csv) records OpenAlex full-text location candidates; a candidate link does not mean that a paper has been read.
