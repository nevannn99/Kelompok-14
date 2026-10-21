# Proyek Algoritma Genetika: Optimasi Penjadwalan Kuliah (UTS)

## 📌 Deskripsi Proyek
Repositori ini berisi implementasi sistem penjadwalan kuliah otomatis menggunakan Algoritma Genetika (AG) yang dibangun dari nol (tanpa library DEAP/PyGAD). Proyek ini dibuat untuk memenuhi **Tahap 1 (UTS)** mata kuliah Algoritma Genetika.

Program ini mampu menghasilkan jadwal tanpa bentrok (solusi valid) untuk data skala kecil: **20 Mata Kuliah, 8 Dosen, 5 Ruang, dan 5 Hari × 5 Slot Waktu**. Output yang dihasilkan meliputi tabel jadwal harian, ekspor ke CSV, dan grafik konvergensi.

## 🚀 Cara Menjalankan Program

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/noyanm99/Kelompok-14.git
   cd Kelompok-14
Install dependensi:
Pastikan Python sudah terinstall di komputer Anda. Program ini hanya membutuhkan library matplotlib untuk menggambar grafik.

bash
pip install -r requirements.txt
(Jika file requirements.txt belum ada, jalankan: pip install matplotlib)

Jalankan program utama:
Pastikan Anda berada di folder utama (root), lalu jalankan:

bash
python src/genetic_algoritma.py
🎯 Fitur & Pemenuhan Ketentuan UTS
Program ini telah mengimplementasikan seluruh instruksi pada dokumen tugas:

Pemodelan Masalah: Menggunakan 20 MK, 8 Dosen, 5 Ruangan (kapasitas berbeda), dan 5 Hari × 5 Slot.

Kendala Keras (Hard Constraints): Dosen bentrok, Ruang bentrok, Kelas bentrok, dan Kapasitas ruang tidak mencukupi.

Representasi Kromosom: Integer-pair (setiap gen berisi pasangan [slot waktu, ruang]).

Fungsi Fitness: Berbasis penalti 1 / (1 + total pelanggaran).

Operator Genetika:

Seleksi: Tersedia fungsi Roulette Wheel dan Turnamen (digunakan Turnamen pada loop utama).

Crossover: Tersedia Single-point dan Uniform (digunakan Uniform pada loop utama).

Mutasi: Mutasi acak per gen.

Elitisme: 2 individu terbaik dilestarikan di setiap generasi.

Pengujian Awal: Program otomatis menjalankan eksperimen minimal 10 kali run dengan seed berbeda dan mencetak hasilnya di terminal.

Output:

Menampilkan jadwal dalam format tabel referensi.

Mengekspor jadwal ke file jadwal_uts_terbaik.csv.

Menyimpan grafik konvergensi ke grafik_konvergensi_uts.png.

📁 Struktur Direktori
src/ : Berisi file utama genetic_algoritma.py (Data, Fitness, Operator AG, Eksperimen, Output).

data/ : (Disediakan untuk pengembangan UAS) Dataset jadwal kuliah eksternal.

experiments/ : (Disediakan untuk pengembangan UAS) Skrip khusus eksperimen parameter.

app/ : (Disediakan untuk pengembangan UAS) Aplikasi antarmuka (Streamlit/Flask).

👥 Pembagian Tugas Kelompok
[Nama 1] - Ketua / Analis Masalah (Pemodelan kendala & data)

[Nama 2] - Programmer Inti AG (Kromosom, seleksi, crossover, mutasi)

[Nama 3] - Programmer Fitness & Validasi (Fungsi fitness, cek bentrok)

[Nama 4] - Analis Eksperimen (Skenario uji 10-run, grafik konvergensi)

[Nama 5] - Penulis & Presenter (Laporan, slide, dokumentasi README)
