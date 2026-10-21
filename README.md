# Proyek Algoritma Genetika: Optimasi Penjadwalan Kuliah

## Deskripsi
Repositori ini berisi implementasi sistem penjadwalan kuliah otomatis menggunakan Algoritma Genetika (AG) dari nol (tanpa library DEAP/PyGAD). Proyek ini dibuat untuk memenuhi tugas UTS dan UAS mata kuliah terkait.

## Cara Menjalankan Program
1. Clone repositori ini.
2. Install dependensi: `pip install -r requirements.txt`
3. Jalankan program utama: `python src/genetic_algorithm.py`

## Struktur Direktori
- `src/`: Kode utama (operator, fitness, constraints).
- `data/`: Dataset jadwal kuliah.
- `experiments/`: Skrip untuk eksperimen UTS & UAS.
- `app/`: Aplikasi antarmuka (Streamlit).

## Pembagian Tugas Kelompok
1. **Nama 1** - Ketua / Analis Masalah (Pemodelan kendala & data)
2. **Nama 2** - Programmer Inti AG (Kromosom, seleksi, crossover, mutasi)
3. **Nama 3** - Programmer Fitness & Validasi (Fungsi fitness, cek bentrok)
4. **Nama 4** - Analis Eksperimen (Skenario uji, grafik konvergensi)
5. **Nama 5** - (Jika ada) UI/UX & Dokumentasi
