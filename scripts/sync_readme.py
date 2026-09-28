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


def main():
    root = Path(__file__).resolve().parents[1]
    sources = json.loads((root / "sources.json").read_text(encoding="utf-8"))["sources"]
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README harus memiliki satu pasang penanda tabel sumber")
    before, remainder = readme.split(START, 1)
    _, after = remainder.split(END, 1)
    refreshed = before + START + "\n" + render_table(sources) + "\n" + END + after
    if refreshed != readme:
        readme_path.write_text(refreshed, encoding="utf-8")
    print(f"Tabel README sesuai dengan {len(sources)} sumber")


if __name__ == "__main__":
    main()
