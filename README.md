# McEasy Content Idea Sources & Product Catalog

Daftar sumber untuk menemukan perkembangan industri yang berpotensi menjadi ide konten blog McEasy. Fokusnya meliputi logistik dan transportasi, pertambangan dan alat berat, teknologi armada, BBM dan energi, serta regulasi yang memengaruhi operasional armada.

**Data utama:** [sources.json](sources.json) untuk sumber berita dan [product_catalog.json](product_catalog.json) untuk peta solusi, hardware, industri, serta ide awareness ban. Daftar awal memuat 18 sumber resmi, asosiasi, data, dan media industri. Temuan dari media dapat menjadi titik awal riset; verifikasi fakta penting pada dokumen, data, atau pihak asalnya.

## Daftar sumber

Tabel ini dibuat otomatis dari `sources.json`. Edit daftar di file JSON; perubahan pada tabel akan menyusul setelah sinkronisasi berjalan.

<!-- sources-table:start -->
| Sumber | Jenis | Topik | Prioritas | Tujuan konten | Status |
| --- | --- | --- | --- | --- | --- |
| [Ditjen Perhubungan Darat](https://hubdat.dephub.go.id/id/publikasi/) | Regulator | Transportasi & logistik, Regulasi, Keselamatan armada | Tinggi | awareness, acquisition | Aktif |
| [Kementerian ESDM](https://www.esdm.go.id/id/media-center/arsip-berita) | Regulator | BBM & energi, Pertambangan & alat berat | Tinggi | awareness, acquisition | Aktif |
| [BPH Migas](https://www.bphmigas.go.id/berita/) | Regulator | BBM & energi | Tinggi | awareness, acquisition | Aktif |
| [JDIH Kemenhub](https://jdih.dephub.go.id/peraturan/index) | Dokumen hukum | Regulasi, Transportasi & logistik | Tinggi | awareness, acquisition | Aktif |
| [JDIH ESDM](https://jdih.esdm.go.id/) | Dokumen hukum | Regulasi, BBM & energi, Pertambangan & alat berat | Tinggi | awareness, acquisition | Aktif |
| [APTRINDO—News](https://aptrindo.id/news/) | Asosiasi | Transportasi & logistik, Kendaraan niaga | Tinggi | awareness, acquisition | Aktif |
| [KNKT—LLAJ](https://knkt.go.id/subkomite/llaj) | Investigasi | Keselamatan armada, Transportasi & logistik | Tinggi | awareness | Aktif |
| [Ditjen Bina Marga](https://binamarga.pu.go.id/berita) | Infrastruktur | Transportasi & logistik | Sedang | awareness, acquisition | Aktif |
| [BPJT](https://bpjt.pu.go.id/berita/) | Infrastruktur | Transportasi & logistik | Sedang | awareness, acquisition | Aktif |
| [Korlantas Polri](https://korlantas.polri.go.id/) | Penegak hukum | Regulasi, Keselamatan armada | Sedang | awareness, acquisition | Aktif |
| [BPS—Statistik Transportasi](https://www.bps.go.id/id/statistics-table?subject=560) | Data | Transportasi & logistik | Pendukung | awareness | Aktif |
| [Ditjen Minerba](https://www.minerba.esdm.go.id/) | Regulator | Pertambangan & alat berat | Pantau akses | awareness, acquisition | Pantau akses |
| [Kompas Otomotif—Niaga](https://otomotif.kompas.com/niaga) | Media | Kendaraan niaga, Teknologi armada | Pantau akses | awareness | Pantau akses |
| [detikOto—Kendaraan Niaga](https://oto.detik.com/kendaraan-niaga) | Media | Kendaraan niaga, Teknologi armada | Pantau akses | awareness | Pantau akses |
| [Logistik News—Transportasi & Logistik](https://www.logistiknews.id/topic/transportasi-logistik/) | Media industri | Transportasi & logistik | Tinggi | awareness, acquisition | Aktif |
| [Bisnis.com—Transportasi & Logistik](https://ekonomi.bisnis.com/transportasi-logistik) | Media | Transportasi & logistik | Pantau akses | awareness, acquisition | Pantau akses |
| [ANTARA—Ekonomi/Bisnis](https://www.antaranews.com/ekonomi/bisnis) | Kantor berita | Ekonomi, Transportasi & logistik, BBM & energi | Pantau akses | awareness, acquisition | Pantau akses |
| [Petromindo](https://www.petromindo.com/) | Media industri | Pertambangan & alat berat | Sedang | awareness | Aktif |
| [Oto Mounture—Komersial](https://oto.mounture.com/komersial/) | Media | Kendaraan niaga, Teknologi armada | Tinggi | awareness | Aktif |
| [Transportasi Media Indonesia](https://transportasimedia.com/) | Media industri | Kendaraan niaga, Teknologi armada | Tinggi | awareness | Aktif |
| [Investor Daily](https://investor.id/) | Media | Transportasi & logistik | Tinggi | awareness, acquisition | Aktif |
| [Holopis.com](https://holopis.com/) | Media | Ekonomi, Transportasi & logistik, BBM & energi | Sedang | awareness, acquisition | Aktif |
| [Supply Chain Indonesia](https://supplychainindonesia.com/publikasi/) | Media industri | Transportasi & logistik | Sedang | awareness, acquisition | Aktif |
<!-- sources-table:end -->

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
4. Klik **Commit changes** dan tulis ringkasan perubahan. Riwayat commit menyimpan perubahan daftar; tabel README diperbarui otomatis oleh GitHub Actions.
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

Hermes perlu membaca URL ini kembali setiap kali memakai daftar agar perubahan terbaru tersedia. Repositori ini menyimpan daftar sumber dan katalog produk editorial; tidak menyimpan salinan penuh artikel atau berita.

## Katalog produk McEasy

[product_catalog.json](product_catalog.json) adalah data utama bagi Hermes untuk memetakan temuan berita ke solusi McEasy. Daftar perangkat per industri berasal dari diagram referensi yang diberikan tim. Relasi solusi dan perangkat adalah petunjuk editorial; cocokkan klaim ketersediaan, kompatibilitas, serta spesifikasi dengan tim produk sebelum dipublikasikan.

### Solusi dan perangkat

<!-- catalog-solutions:start -->
| Solusi | Fungsi | Perangkat terkait |
| --- | --- | --- |
| Video Monitoring | Pemantauan video dan keselamatan perjalanan. | Dashcam, MDVR, Kamera Blind Spot, Kamera Belakang, ADAS, DMS |
| Spare Part (Ban) | Pengadaan ban kendaraan; prioritas konten dan penawaran untuk ban truk dan bus. | — |
| Fleet Management | Pelacakan armada dan pengelolaan operasional kendaraan. | GPS Tracker, GPS Portable, OBD 4G, RFID |
| Delivery Hub | Portal pengiriman terintegrasi. | — |
| Fuel Management | Pemantauan penggunaan dan stok BBM armada. | Fuel Level Sensor, iFuel ODO |
| Delivery Management (TMS) | Pengelolaan order dan proses pengiriman. | — |
| Report and Analytics | Laporan dan analisis operasional armada. | — |
| Delivery Optimization | Perencanaan dan optimasi rute pengiriman. | — |
| Maintenance Management | Perencanaan pemeliharaan dan perawatan kendaraan. | — |
| Customer Management | Pengelolaan interaksi dan informasi untuk pelanggan. | — |
| Driver Management | Pemantauan dan pengembangan kinerja pengemudi. | RFID, DMS |
| Cost Management | Pencatatan dan analisis biaya operasional. | — |
| Vendor Management | Pengelolaan mitra dan vendor. | — |
| Open Ecosystem | Integrasi sistem melalui API. | — |
| Control Tower | Tampilan pemantauan operasional lintas proses. | — |
<!-- catalog-solutions:end -->

### Aplikasi per industri

Kolom perangkat mengikuti diagram referensi; industri yang juga ditandai untuk ban truk atau bus merupakan peluang konten editorial tambahan, bukan klaim bahwa ban muncul dalam diagram.

<!-- catalog-industries:start -->
| Industri | Perangkat pada diagram |
| --- | --- |
| Agrikultur | GPS Tracker, RFID, Fuel Level Sensor, iFuel ODO |
| Pengangkutan B3 | GPS Tracker, GPS Portable, RFID, Dashcam, MDVR, iBuzzer, Fuel Level Sensor, Sensor Suhu, Sensor Pintu, iBeacon |
| Rantai Dingin | GPS Tracker, GPS Portable, RFID, Dashcam, MDVR, iBuzzer, Fuel Level Sensor, Kamera Penghitung Penumpang, Kamera Blind Spot, iBeacon |
| Cash Transit | Tombol SOS, Dashcam, iBuzzer, GPS Tracker, RFID, iFuel ODO, Sensor Pintu |
| Migas | GPS Tracker, GPS Portable, RFID, MDVR, Kamera Blind Spot, Kamera Belakang, Fuel Level Sensor |
| Bus dan Otobus | Kamera Penghitung Penumpang, Kamera Blind Spot, GPS Tracker, GPS Portable, RFID, Dashcam, iBuzzer, MDVR, Fuel Level Sensor |
| Pertambangan dan Alat Berat | RFID, GPS Tracker, Dashcam, Sensor Power Take Off (PTO), iBeacon, ADAS, DMS, MDVR, OBD 4G, Kamera Belakang, Kamera Blind Spot, Fuel Level Sensor |
| Logistik | GPS Tracker, GPS Portable, RFID, Dashcam, iBuzzer, MDVR, Fuel Level Sensor, Sensor Suhu, Sensor Pintu, iBeacon |
<!-- catalog-industries:end -->

### Ban dan ide awareness

McEasy menyediakan ban mobil, truk, dan bus. Fokus konten dan penawaran di sini adalah ban truk serta ban bus. Ide berikut merupakan usulan topik, bukan klaim spesifikasi ban tertentu.

<!-- catalog-tires:start -->
| Kategori ban | Fokus | Ide awareness |
| --- | --- | --- |
| Ban Truk | utama | cara memilih ban truk sesuai rute dan beban; tekanan ban dan keselamatan armada; umur pakai dan inspeksi ban; biaya ban per kilometer; penyebab ban truk cepat aus; kapan ban truk perlu diganti |
| Ban Bus | utama | pemilihan ban bus untuk rute antarkota dan pariwisata; pemeriksaan ban sebelum perjalanan; tekanan ban dan keselamatan penumpang; umur pakai dan jadwal penggantian; biaya ban per kilometer untuk operator bus |
| Ban Mobil | pendukung | perawatan dan penggantian ban armada mobil |
<!-- catalog-tires:end -->

### Memperbarui katalog

1. Edit [product_catalog.json](product_catalog.json) di GitHub. Gunakan `id` unik dan stabil untuk setiap solusi, perangkat, jenis ban, dan industri.
2. Hubungkan industri serta solusi dengan `hardware_ids` dan `solution_ids` yang sudah ada. Untuk produk baru, tambahkan objek perangkat terlebih dahulu.
3. Simpan perubahan melalui **Commit changes**. GitHub Actions memperbarui tabel README otomatis dari JSON.

URL data langsung untuk Hermes:

```text
https://raw.githubusercontent.com/angxsupriyanto/content-idea-sources/main/product_catalog.json
```
