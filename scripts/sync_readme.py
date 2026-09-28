#!/usr/bin/env python3
"""Refresh the human-readable README table from sources.json."""

import json
from pathlib import Path

START = "<!-- sources-table:start -->"
END = "<!-- sources-table:end -->"

TYPES = {
    "regulator": "Regulator", "dokumen_hukum": "Dokumen hukum",
    "asosiasi": "Asosiasi", "investigasi": "Investigasi",
    "infrastruktur": "Infrastruktur", "penegak_hukum": "Penegak hukum",
    "data": "Data", "media": "Media", "media_industri": "Media industri",
    "kantor_berita": "Kantor berita",
}
TOPICS = {
    "transportasi_logistik": "Transportasi & logistik",
    "regulasi": "Regulasi", "keselamatan_armada": "Keselamatan armada",
    "bbm_energi": "BBM & energi",
    "pertambangan_alat_berat": "Pertambangan & alat berat",
    "kendaraan_niaga": "Kendaraan niaga",
    "teknologi_armada": "Teknologi armada", "ekonomi": "Ekonomi",
}
PRIORITY = {
    "high": "Tinggi", "medium": "Sedang",
    "supporting": "Pendukung", "monitor": "Pantau akses",
}


def safe(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_table(sources):
    lines = [
        "| Sumber | Jenis | Topik | Prioritas | Tujuan konten | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    ids = set()
    for source in sources:
        source_id = source["id"]
        if source_id in ids:
            raise ValueError(f"Duplikat id sumber: {source_id}")
        ids.add(source_id)
        name = safe(source["name"])
        url = source["urls"][0]["url"]
        if not url.startswith("https://"):
            raise ValueError(f"URL tidak memakai HTTPS: {source_id}")
        kind = safe(TYPES.get(source["type"], source["type"]))
        topics = safe(", ".join(TOPICS.get(x, x) for x in source["topics"]))
        priority = safe(PRIORITY.get(source["priority"], source["priority"]))
        goals = safe(", ".join(source["content_goal"]))
        status = "Aktif" if source["status"] == "active" else "Pantau akses"
        lines.append(f"| [{name}]({url}) | {kind} | {topics} | {priority} | {goals} | {status} |")
    return "\n".join(lines)



def render_catalog_tables(catalog):
    solutions = catalog["solutions"]
    hardware = catalog["hardware"]
    industries = catalog["industry_applications"]
    tires = catalog["spare_parts"]
    for label, items in (("solusi", solutions), ("perangkat", hardware), ("industri", industries), ("ban", tires)):
        ids = [item["id"] for item in items]
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplikat id {label}")
    hardware_names = {item["id"]: item["name"] for item in hardware}
    solution_ids = {item["id"] for item in solutions}
    def device_names(ids):
        return safe(", ".join(hardware_names[id] for id in ids) or "—")
    sol_lines = ["| Solusi | Fungsi | Perangkat terkait |", "| --- | --- | --- |"]
    for item in solutions:
        sol_lines.append(f'| {safe(item["name"])} | {safe(item["description"])} | {device_names(item["hardware_ids"])} |')
    ind_lines = ["| Industri | Perangkat pada diagram |", "| --- | --- |"]
    for item in industries:
        for solution_id in item["solution_ids"]:
            if solution_id not in solution_ids:
                raise ValueError(f"Solusi tidak ditemukan: {solution_id}")
        ind_lines.append(f'| {safe(item["name"])} | {device_names(item["hardware_ids"])} |')
    tire_lines = ["| Kategori ban | Fokus | Ide awareness |", "| --- | --- | --- |"]
    for item in tires:
        tire_lines.append(f'| {safe(item["name"])} | {safe(item["priority"])} | {safe("; ".join(item["awareness_topics"]))} |')
    return {"catalog-solutions": "\n".join(sol_lines), "catalog-industries": "\n".join(ind_lines), "catalog-tires": "\n".join(tire_lines)}


def replace_table(readme, marker, table):
    start, end = f"<!-- {marker}:start -->", f"<!-- {marker}:end -->"
    if readme.count(start) != 1 or readme.count(end) != 1:
        raise ValueError(f"README harus memiliki satu pasang penanda {marker}")
    before, remainder = readme.split(start, 1)
    _, after = remainder.split(end, 1)
    return before + start + "\n" + table + "\n" + end + after

def main():
    root = Path(__file__).resolve().parents[1]
    sources = json.loads((root / "sources.json").read_text(encoding="utf-8"))["sources"]
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    refreshed = replace_table(readme, "sources-table", render_table(sources))
    catalog = json.loads((root / "product_catalog.json").read_text(encoding="utf-8"))
    for marker, table in render_catalog_tables(catalog).items():
        refreshed = replace_table(refreshed, marker, table)
    if refreshed != readme:
        readme_path.write_text(refreshed, encoding="utf-8")
    print(f"Tabel README sesuai dengan {len(sources)} sumber dan katalog produk")


if __name__ == "__main__":
    main()
