from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCREEN = ROOT / "SCREENING.csv"
OUT = ROOT / "exports"
INCLUDED = {"CORE_INCLUDE", "ADJACENT"}


def read_rows(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows):
    fields = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def ris_type(row):
    doi = (row.get("doi") or "").casefold()
    venue = (row.get("journal_or_venue") or "").casefold()
    if doi.startswith("10.48550/arxiv") or "arxiv" in venue:
        return "RPRT"
    if "springer proceedings in advanced robotics" in venue:
        return "CHAP"
    if any(x in venue for x in (
        "international conference", "conference on", "conference (", "conference (",
        "journal of physics: conference series", "mendel", "humanoids", "icra", "icma", "iccc",
        "control, robotics and cybernetics", "advanced robotics (icar)",
    )):
        return "CPAPER"
    return "JOUR"


def build_ris(rows, path: Path):
    lines = []
    for row in rows:
        lines.append(f"TY  - {ris_type(row)}")
        for author in (row.get("authors") or "").split("; "):
            if author.strip():
                lines.append("AU  - " + author.strip())
        lines.append("TI  - " + (row.get("title") or ""))
        if row.get("journal_or_venue"):
            lines.append("JO  - " + row["journal_or_venue"])
        if row.get("year"):
            lines.append("PY  - " + row["year"][:4])
        if row.get("doi"):
            lines.append("DO  - " + row["doi"])
            lines.append("UR  - https://doi.org/" + row["doi"])
        elif row.get("url"):
            lines.append("UR  - " + row["url"])
        if row.get("abstract"):
            lines.append("AB  - " + re.sub(r"\s+", " ", row["abstract"]).strip())
        decision = row["screening_decision"]
        lines.append("KW  - trajectory-consistent-ik-review")
        lines.append("KW  - TC-IK-" + ("CORE" if decision == "CORE_INCLUDE" else "ADJACENT" if decision == "ADJACENT" else "UNCERTAIN"))
        lines.append("N1  - screening_decision=" + decision)
        lines.append("N1  - abstract_source=" + (row.get("abstract_source") or "missing"))
        lines.append("N1  - metadata_source=" + (row.get("bibliographic_metadata_source") or "unknown"))
        lines.append("ER  - ")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8-sig")


def bib_escape(value):
    value = value or ""
    for ch in ("\\", "&", "%", "#", "_"):
        if ch == "\\":
            value = value.replace(ch, r"\textbackslash{}")
        else:
            value = value.replace(ch, "\\" + ch)
    return value


def cite_key(row, used):
    first_author = (row.get("authors") or "Unknown").split("; ")[0]
    family = re.sub(r"[^A-Za-z0-9]+", "", first_author.split(",")[0]) or "Anon"
    year = (row.get("year") or "nd")[:4]
    word = re.sub(r"[^A-Za-z0-9]+", "", (row.get("title") or "").split(" ")[0]) or "Paper"
    base = f"{family}{year}{word}"
    key, n = base, 2
    while key in used:
        key = f"{base}{n}"
        n += 1
    used.add(key)
    return key


def build_bib(rows, path: Path):
    used = set()
    entries = []
    for row in rows:
        kind = ris_type(row)
        entry_type = {"CPAPER": "inproceedings", "CHAP": "incollection", "RPRT": "misc"}.get(kind, "article")
        fields = {
            "title": "{" + (row.get("title") or "") + "}",
            "author": (row.get("authors") or "").replace("; ", " and "),
            "year": (row.get("year") or "")[:4],
            ("booktitle" if entry_type in {"inproceedings", "incollection"} else "journal"): row.get("journal_or_venue") or "",
            "doi": row.get("doi") or "",
            "url": row.get("url") or ("https://doi.org/" + row["doi"] if row.get("doi") else ""),
        }
        key = cite_key(row, used)
        body = [f"@{entry_type}{{{key},"]
        for name, value in fields.items():
            if value:
                body.append(f"  {name} = {{{bib_escape(value)}}},")
        body.append("}")
        entries.append("\n".join(body))
    path.write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def main():
    rows = read_rows(SCREEN)
    included = [r for r in rows if r["screening_decision"] in INCLUDED]
    core = [r for r in included if r["screening_decision"] == "CORE_INCLUDE"]
    adjacent = [r for r in included if r["screening_decision"] == "ADJACENT"]
    uncertain = [r for r in rows if r["screening_decision"] == "UNCERTAIN_FULLTEXT"]
    missing = [r for r in rows if r["abstract_status"] == "MISSING"]
    write_csv(OUT / "screened_included.csv", included)
    write_csv(OUT / "abstracts_missing.csv", missing)
    build_ris(included, ROOT / "references.ris")
    build_ris(core, ROOT / "references_core.ris")
    build_ris(adjacent, ROOT / "references_adjacent.ris")
    build_ris(uncertain, ROOT / "uncertain_records.ris")
    build_bib(included, ROOT / "references.bib")

    counts = Counter(r["screening_decision"] for r in rows)
    years = Counter((r.get("year") or "MISSING")[:4] for r in rows)
    summary = {
        "screen_date": "2026-09-29",
        "search_window": ["2016-01-01", "2026-09-29"],
        "consensus_quick_queries": 16,
        "exported_ris_instances": 419,
        "unique_doi_records": len(rows),
        "all_unique_records_have_doi": all(bool(r.get("doi")) for r in rows),
        "abstracts_available": sum(bool(r.get("abstract")) for r in rows),
        "abstracts_missing": len(missing),
        "abstract_sources": dict(Counter(r.get("abstract_source") or "missing" for r in rows)),
        "screening_decisions": dict(counts),
        "included_core_plus_adjacent": len(included),
        "screened_years": dict(sorted(years.items())),
        "full_text_checked": 0,
        "bibliographic_metadata_crossref_corrected": sum(r.get("bibliographic_metadata_source") == "Crossref DOI record" for r in rows),
    }
    (OUT / "corpus_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
