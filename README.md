# McEasy Content Idea Sources

Daftar sumber untuk menemukan perkembangan industri yang berpotensi menjadi ide konten blog McEasy. Fokusnya meliputi logistik dan transportasi, pertambangan dan alat berat, teknologi armada, BBM dan energi, serta regulasi yang memengaruhi operasional armada.

**Daftar utama:** [sources.json](sources.json) — satu-satunya file sumber yang dipelihara di repositori ini. Daftar awal memuat 18 sumber resmi, asosiasi, data, dan media industri. Temuan dari media dapat menjadi titik awal riset; verifikasi fakta penting pada dokumen, data, atau pihak asalnya.

## Membaca daftar

Setiap objek dalam `sources` mewakili satu sumber.

| Field | Arti |
| --- | --- |
| `id` | Pengenal unik yang stabil. |
| `name` | Nama sumber yang ditampilkan kepada pengguna. |
| `type` | Jenis sumber, misalnya `regulator`, `asosiasi`, `media`, atau `data`. |
| `priority` | `high`, `medium`, `supporting`, atau `monitor`. Ini adalah prioritas pemantauan, bukan jaminan mutu setiap artikel. |
| `status` | `active` untuk sumber yang dipantau; `monitor` untuk sumber yang aksesnya perlu diperiksa kembali. |
| `topics` | Topik yang relevan, disimpan sebagai daftar agar satu sumber bisa mencakup beberapa topik. |
| `content_goal` | Potensi tujuan ide konten: `awareness`, `acquisition`, atau keduanya. Tujuan akhir ditentukan per temuan, bukan otomatis oleh sumber. |
| `urls` | Satu atau lebih alamat, masing-masing dengan `url` dan `purpose`. |
| `keywords` | Kata kunci tambahan untuk pencarian pada sumber tersebut; daftar kosong berarti belum ditetapkan. |
| `notes` | Catatan penggunaan atau verifikasi sumber. |

## Menambah atau memperbarui sumber

1. Buka [sources.json](sources.json), klik ikon pensil (**Edit this file**), lalu ubah isinya.
2. Untuk sumber baru, salin satu objek yang ada, buat `id` yang berbeda, dan sesuaikan semua field. Jangan gunakan ulang `id` milik sumber lain.
3. Pastikan format JSON valid: pisahkan objek dengan koma, gunakan tanda kutip ganda, dan jangan beri koma setelah objek atau item terakhir.
4. Klik **Commit changes** dan tulis ringkasan perubahan. Riwayat commit menyimpan perubahan daftar.
5. Bila situs sementara tidak dapat diakses, gunakan `status: "monitor"` dan jelaskan kondisinya di `notes`. Perbarui lagi setelah akses pulih.

Contoh satu entri:

```json
{
  "id": "contoh-sumber",
  "name": "Nama Sumber",
  "type": "media",
  "priority": "medium",
  "status": "active",
  "topics": ["transportasi_logistik"],
  "content_goal": ["awareness"],
  "urls": [
    {
      "url": "https://contoh.id/berita",
      "purpose": "liputan_industri"
    }
  ],
  "keywords": [],
  "notes": "Catatan singkat tentang penggunaan sumber."
}
```

## Akses untuk Hermes

URL file JSON langsung:

```text
https://raw.githubusercontent.com/angxsupriyanto/content-idea-sources/main/sources.json
```

Hermes perlu membaca URL ini kembali setiap kali memakai daftar agar perubahan terbaru tersedia. Repositori ini hanya menyimpan daftar sumber; tidak menyimpan salinan penuh artikel atau berita.
