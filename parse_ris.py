from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "exports" / "raw"
OUT = ROOT / "exports"


def parse_file(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    records = []
    current = defaultdict(list)
    for line in text.splitlines():
        m = re.match(r"^([A-Z0-9]{2})\s+-\s?(.*)$", line)
        if not m:
            if line[:2].isspace() and current:
                key = next(reversed(current))
                current[key][-1] += " " + line.strip()
            continue
        tag, value = m.groups()
        if tag == "ER":
            if current:
                records.append(dict(current))
            current = defaultdict(list)
        else:
            current[tag].append(value.strip())
    if current:
        records.append(dict(current))
    query = re.sub(r" - 2026年9月29日(?: \(\d+\))?$", "", path.stem)
    return [
        {
            "source_file": path.name,
            "source_query": query,
            "ris_type": first(r, "TY"),
            "title": first(r, "TI") or first(r, "T1"),
            "authors": "; ".join(r.get("AU", r.get("A1", []))),
            "year": first(r, "PY") or first(r, "Y1"),
            "journal_or_venue": first(r, "JO") or first(r, "JF") or first(r, "T2"),
            "doi": first(r, "DO"),
            "url": first(r, "UR"),
            "abstract": first(r, "AB"),
        }
        for r in records
    ]


def first(record, key):
    values = record.get(key, [])
    return values[0] if values else ""


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").casefold()).strip()


def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    raw = [r for p in sorted(RAW.glob("*.ris")) for r in parse_file(p)]
    groups = {}
    for row in raw:
        key = "doi:" + norm(row["doi"]) if row["doi"] else "title:" + norm(row["title"]) + ":" + row["year"]
        if key not in groups:
            groups[key] = dict(row)
            groups[key]["source_queries"] = row["source_query"]
            groups[key]["occurrences"] = 1
        else:
            groups[key]["occurrences"] += 1
            queries = groups[key]["source_queries"].split(" || ")
            if row["source_query"] not in queries:
                queries.append(row["source_query"])
            groups[key]["source_queries"] = " || ".join(queries)
            for field in ("title", "authors", "journal_or_venue", "doi", "url", "abstract"):
                if not groups[key][field] and row[field]:
                    groups[key][field] = row[field]
    deduped = sorted(groups.values(), key=lambda r: (r["year"], r["title"].casefold()))
    fields = ["title", "authors", "year", "journal_or_venue", "doi", "url", "abstract", "ris_type", "source_query", "source_queries", "source_file", "occurrences"]
    write_csv(OUT / "records_raw.csv", raw, fields)
    write_csv(OUT / "records_deduplicated.csv", deduped, fields)
    title_hits = []
    direct = re.compile(r"inverse kinematic|\bik\b|singular|branch|path wise|path following|trajectory|joint limit|joint range|continuous", re.I)
    for row in deduped:
        if direct.search(row["title"]):
            title_hits.append(row)
    write_csv(OUT / "title_candidates.csv", title_hits, fields)
    years = defaultdict(int)
    for r in deduped:
        years[r["year"][:4] or "MISSING"] += 1
    print(f"raw_records={len(raw)} unique_records={len(deduped)} title_candidates={len(title_hits)}")
    print("unique_by_year=" + ", ".join(f"{y}:{n}" for y, n in sorted(years.items())))
    print(f"records_with_doi={sum(bool(r['doi']) for r in deduped)} records_with_abstract={sum(bool(r['abstract']) for r in deduped)}")


if __name__ == "__main__":
    main()
