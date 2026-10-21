# Proyek Algoritma Genetika: Optimasi Penjadwalan Kuliah (UTS)

## 📌 Deskripsi Proyek

Repositori ini berisi implementasi sistem penjadwalan kuliah otomatis menggunakan **Algoritma Genetika (AG)** yang dibangun dari awal (*from scratch*) tanpa menggunakan library khusus Algoritma Genetika seperti DEAP atau PyGAD.

Proyek ini dikembangkan untuk memenuhi **Tahap 1 (UTS)** pada mata kuliah Algoritma Genetika.

Program dirancang untuk menghasilkan jadwal kuliah yang valid tanpa bentrok berdasarkan data skala kecil dengan spesifikasi berikut:

- **20** mata kuliah
- **8** dosen
- **5** ruang kuliah dengan kapasitas berbeda
- **5** hari perkuliahan
- **5** slot waktu per hari

Program menghasilkan jadwal kuliah, mengekspor jadwal ke file CSV, serta menampilkan grafik konvergensi proses Algoritma Genetika.

## 🚀 Cara Menjalankan Program

### 1. Clone Repository

Jalankan perintah berikut pada terminal:

```bash
git clone https://github.com/noyanm99/Kelompok-14.git
cd Kelompok-14
```

### 2. Instal Dependensi

Pastikan Python sudah terinstal di komputer. Program ini menggunakan library `matplotlib` untuk membuat grafik konvergensi.

Jika file `requirements.txt` tersedia, jalankan:

```bash
pip install -r requirements.txt
```

Jika file tersebut belum tersedia, instal dependensi secara langsung:

```bash
pip install matplotlib
```

### 3. Jalankan Program

Pastikan terminal berada di direktori utama repositori, kemudian jalankan:

```bash
python src/genetic_algoritma.py
```

Program akan menjalankan proses optimasi penjadwalan, melakukan pengujian dengan beberapa seed, dan menampilkan hasilnya di terminal.

**Catatan:** Pastikan nama file, lokasi direktori, dan dependensi sesuai dengan kondisi repositori yang digunakan.

## 🎯 Fitur dan Pemenuhan Ketentuan UTS

Implementasi program mencakup komponen utama Algoritma Genetika untuk menyelesaikan permasalahan optimasi penjadwalan kuliah.

### 1. Pemodelan Masalah

- Menggunakan 20 mata kuliah, 8 dosen, dan 5 ruang kuliah.
- Menggunakan 5 hari dengan 5 slot waktu per hari.
- Mempertimbangkan kapasitas ruang kuliah yang berbeda.

### 2. Kendala Penjadwalan (*Hard Constraints*)

Program memeriksa beberapa kendala utama berikut:

- **Bentrok dosen:** Seorang dosen tidak boleh mengajar lebih dari satu mata kuliah pada slot waktu yang sama.
- **Bentrok ruang:** Satu ruang tidak boleh digunakan oleh lebih dari satu mata kuliah pada slot waktu yang sama.
- **Bentrok kelas:** Kelas yang sama tidak boleh mengikuti lebih dari satu mata kuliah pada slot waktu yang sama.
- **Kapasitas ruang:** Kapasitas ruang harus mencukupi jumlah mahasiswa pada mata kuliah yang dijadwalkan.

### 3. Representasi Kromosom

Setiap kromosom merepresentasikan satu kandidat jadwal kuliah. Setiap gen menyimpan pasangan nilai berupa:

- Slot waktu perkuliahan.
- Ruang kuliah yang digunakan.

Representasi ini memungkinkan setiap individu dalam populasi merepresentasikan satu solusi penjadwalan.

### 4. Fungsi Fitness

Fungsi fitness menggunakan pendekatan berbasis penalti:

\[
\text{Fitness} = \frac{1}{1 + \text{Total Pelanggaran}}
\]

Semakin sedikit pelanggaran kendala, semakin tinggi nilai fitness yang diperoleh. Jadwal tanpa pelanggaran memiliki nilai fitness sebesar 1.

### 5. Operator Algoritma Genetika

| Komponen | Metode | Keterangan |
|---|---|---|
| Seleksi | Roulette Wheel dan Turnamen | Memilih individu untuk menghasilkan keturunan. |
| Crossover | Single-Point dan Uniform | Menggabungkan informasi gen dari dua induk. |
| Mutasi | Mutasi acak per gen | Mengubah nilai gen untuk menjaga variasi populasi. |
| Elitisme | 2 individu terbaik | Mempertahankan dua individu terbaik ke generasi berikutnya. |

Pada proses utama, program menggunakan **seleksi Turnamen** dan **crossover Uniform**.

### 6. Pengujian Eksperimen

Program menjalankan eksperimen awal minimal 10 kali dengan seed yang berbeda untuk mengamati hasil optimasi dari beberapa percobaan.

Hasil pengujian ditampilkan di terminal untuk membantu mengevaluasi performa Algoritma Genetika.

### 7. Output Program

Program menghasilkan keluaran berikut:

- **Tabel jadwal kuliah:** Menampilkan hasil penjadwalan dalam format tabel.
- **File CSV:** Menyimpan jadwal terbaik dalam file `jadwal_uts_terbaik.csv`.
- **Grafik konvergensi:** Menyimpan visualisasi perkembangan nilai fitness selama proses evolusi dalam file `grafik_konvergensi_uts.png`.

## 📁 Struktur Direktori

Struktur direktori proyek direncanakan sebagai berikut:

```text
Kelompok-14/
├── src/
│   └── genetic_algoritma.py
├── data/
│   └── Dataset jadwal kuliah untuk pengembangan
├── experiments/
│   └── Skrip eksperimen parameter untuk pengembangan
├── app/
│   └── Aplikasi antarmuka untuk pengembangan
├── requirements.txt
└── README.md
```

**Keterangan direktori:**

- `src/` — Berisi kode utama, meliputi data, fungsi fitness, operator Algoritma Genetika, eksperimen, dan pembuatan output.
- `data/` — Disiapkan untuk pengembangan lanjutan, seperti penggunaan dataset eksternal.
- `experiments/` — Disiapkan untuk pengujian dan eksperimen parameter Algoritma Genetika.
- `app/` — Disiapkan untuk pengembangan antarmuka pengguna menggunakan Streamlit atau Flask.
- `requirements.txt` — Berisi daftar dependensi Python yang diperlukan.
- `README.md` — Dokumentasi proyek.

*Catatan: Sesuaikan struktur di atas dengan file dan folder yang benar-benar tersedia di repositori.*

## 👥 Pembagian Tugas Kelompok

| No. | Anggota | Tanggung Jawab |
|---|---|---|
| 1 | Nama 1 | Ketua dan Analis Masalah: pemodelan masalah, kendala, dan data. |
| 2 | Nama 2 | Programmer Inti AG: representasi kromosom, seleksi, crossover, dan mutasi. |
| 3 | Nama 3 | Programmer Fitness dan Validasi: fungsi fitness dan pemeriksaan bentrok jadwal. |
| 4 | Nama 4 | Analis Eksperimen: pengujian minimal 10 kali, analisis hasil, dan grafik konvergensi. |
| 5 | Nama 5 | Penulis dan Presenter: laporan, slide presentasi, dan dokumentasi README. |

Ganti `Nama 1` hingga `Nama 5` dengan nama anggota kelompok yang sebenarnya.

## 📌 Tujuan Proyek

Proyek ini bertujuan untuk menerapkan konsep dasar Algoritma Genetika dalam menyelesaikan permasalahan optimasi penjadwalan kuliah, mulai dari representasi kromosom, evaluasi fitness, seleksi, crossover, mutasi, hingga evaluasi hasil eksperimen.

Keberhasilan tahap UTS ditunjukkan melalui kemampuan program menghasilkan **jadwal valid tanpa bentrok** untuk skenario data skala kecil yang telah ditentukan.

---

**Mata Kuliah:** Algoritma Genetika  
**Tahap:** Ujian Tengah Semester (UTS)  
**Proyek:** Optimasi Penjadwalan Kuliah Menggunakan Algoritma Genetika
