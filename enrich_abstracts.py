from __future__ import annotations

import csv
import html
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INFILE = ROOT / "exports" / "records_deduplicated.csv"
OUTFILE = ROOT / "exports" / "records_with_abstracts.csv"
UA = "TrajectoryConsistentIKReview/1.0 (bibliographic metadata retrieval)"


def get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as response:
        return json.load(response)


def clean_abstract(value: str) -> str:
    value = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    return re.sub(r"\s+", " ", value).strip()


def from_openalex(obj):
    inv = obj.get("abstract_inverted_index") or {}
    if not inv:
        return ""
    words = {}
    for word, positions in inv.items():
        for position in positions:
            words[position] = word
    return " ".join(words[i] for i in range(max(words) + 1) if i in words)


def norm_doi(value: str) -> str:
    return re.sub(r"^https?://doi\.org/", "", (value or "").strip(), flags=re.I).casefold()


def write_rows(rows):
    fields = list(rows[0].keys()) if rows else []
    with OUTFILE.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def openalex_batch(dois):
    # OpenAlex accepts OR-separated DOI filters, so a small number of polite
    # requests replaces hundreds of per-record requests.
    doi_filter = "|".join("https://doi.org/" + doi for doi in dois)
    params = urllib.parse.urlencode({
        "filter": "doi:" + doi_filter,
        "select": "doi,title,abstract_inverted_index",
        "per-page": "50",
    }, safe=":|/")
    url = "https://api.openalex.org/works?" + params
    data = get_json(url)
    return {norm_doi(work.get("doi", "")): work for work in data.get("results", [])}


def main():
    with INFILE.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["abstract"] = ""
        row["abstract_source"] = ""
        row["metadata_returned_title"] = ""
        row["abstract_retrieval_note"] = "Not retrieved"
    with_abstract = 0
    for start in range(0, len(rows), 30):
        batch = rows[start:start + 30]
        dois = [r["doi"].strip() for r in batch if r.get("doi", "").strip()]
        try:
            works = openalex_batch(dois)
        except Exception as exc:
            for row in batch:
                row["abstract_retrieval_note"] = "OpenAlex batch error: " + type(exc).__name__
            write_rows(rows)
            print(f"batch={start // 30 + 1} error={type(exc).__name__}", flush=True)
            continue
        for row in batch:
            work = works.get(norm_doi(row.get("doi", "")), {})
            row["metadata_returned_title"] = work.get("title", "")
            abstract = clean_abstract(from_openalex(work)) if work else ""
            if abstract:
                row["abstract"] = abstract
                row["abstract_source"] = "OpenAlex"
                row["abstract_retrieval_note"] = "Retrieved by DOI from OpenAlex metadata"
                with_abstract += 1
            else:
                row["abstract_retrieval_note"] = "No abstract in OpenAlex metadata"
        write_rows(rows)
        print(f"batch={start // 30 + 1} records={len(batch)} abstracts_so_far={with_abstract}", flush=True)
    counts = {}
    for row in rows:
        source = row["abstract_source"] or "missing"
        counts[source] = counts.get(source, 0) + 1
    print(f"unique_records={len(rows)} abstract_records={sum(bool(r['abstract']) for r in rows)} sources={counts}")
    print(f"saved={OUTFILE}")


if __name__ == "__main__":
    main()
