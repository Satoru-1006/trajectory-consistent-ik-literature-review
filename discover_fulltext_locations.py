from __future__ import annotations

import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INFILE = ROOT / "FULLTEXT_READING_LOG.csv"
OUTFILE = ROOT / "FULLTEXT_SOURCES.csv"
UA = "TrajectoryConsistentIKReview/1.0 (full-text-location discovery)"


def get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def batches(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def norm_doi(value: str) -> str:
    value = (value or "").strip().casefold()
    return value.removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def openalex_location(work):
    locations = work.get("locations") or []
    best = work.get("best_oa_location") or {}
    candidates = [best] + [loc for loc in locations if loc != best]
    candidates = [loc for loc in candidates if loc]
    pdfs = [loc for loc in candidates if loc.get("pdf_url")]
    chosen = (pdfs or candidates or [{}])[0]
    source = chosen.get("source") or {}
    return {
        "openalex_doi": work.get("doi", ""),
        "openalex_title": work.get("title", ""),
        "open_access_status": (work.get("open_access") or {}).get("oa_status", ""),
        "is_oa": (work.get("open_access") or {}).get("is_oa", ""),
        "oa_url": (work.get("open_access") or {}).get("oa_url", ""),
        "location_landing_page": chosen.get("landing_page_url", ""),
        "location_pdf_url": chosen.get("pdf_url", ""),
        "location_license": chosen.get("license", ""),
        "location_version": chosen.get("version", ""),
        "location_source": source.get("display_name", ""),
        "all_location_count": len(locations),
    }


def main():
    with INFILE.open(encoding="utf-8-sig", newline="") as stream:
        records = list(csv.DictReader(stream))
    fields = [
        "queue_rank", "doi", "title", "year", "venue", "screening_decision",
        "publication_status", "openalex_match", "openalex_doi", "openalex_title",
        "open_access_status", "is_oa", "oa_url", "location_landing_page",
        "location_pdf_url", "location_license", "location_version", "location_source",
        "all_location_count", "retrieval_status", "retrieval_note",
    ]
    output = []
    for batch in batches(records, 30):
        dois = [norm_doi(r["doi"]) for r in batch if r.get("doi")]
        filter_value = "|".join("https://doi.org/" + doi for doi in dois)
        params = urllib.parse.urlencode({
            "filter": "doi:" + filter_value,
            "select": "doi,title,open_access,best_oa_location,locations",
            "per-page": "50",
        }, safe=":|/")
        url = "https://api.openalex.org/works?" + params
        error = ""
        for attempt in range(3):
            try:
                response = get_json(url)
                error = ""
                break
            except (urllib.error.URLError, TimeoutError) as exc:
                error = type(exc).__name__
                if attempt < 2:
                    time.sleep(2 ** attempt)
        works = {norm_doi(w.get("doi", "")): w for w in response.get("results", [])} if not error else {}
        for record in batch:
            doi = norm_doi(record.get("doi", ""))
            work = works.get(doi)
            loc = openalex_location(work) if work else {}
            output.append({
                "queue_rank": record["queue_rank"], "doi": record["doi"],
                "title": record["title"], "year": record["year"],
                "venue": record["venue"], "screening_decision": record["screening_decision"],
                "publication_status": record["publication_status"],
                "openalex_match": "YES" if work else "NO",
                **loc,
                "retrieval_status": "LOCATION_CANDIDATE" if loc.get("location_pdf_url") else "NO_OA_PDF_LOCATED",
                "retrieval_note": error or ("Metadata location only; PDF not yet opened or read." if work else "OpenAlex DOI match not returned."),
            })
        print(f"batch={len(output) // 30} records={len(output)}", flush=True)

    with OUTFILE.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    print(f"saved={OUTFILE} rows={len(output)} pdf_candidates={sum(bool(r.get('location_pdf_url')) for r in output)}")


if __name__ == "__main__":
    main()
