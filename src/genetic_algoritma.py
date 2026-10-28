"""
PROYEK KELOMPOK ALGORITMA GENETIKA - TAHAP 1 (UTS)
Sistem Optimasi Penjadwalan Kuliah
Sesuai Ketentuan PDF: 20 MK, 8 Dosen, 5 Ruang, 5 Hari x 5 Slot.
"""

import csv
import random
import statistics
import matplotlib.pyplot as plt

# =====================================================================
# [POIN 1] PEMODELAN MASALAH & DATA
# =====================================================================
HARI = ("SENIN", "SELASA", "RABU", "KAMIS", "JUMAT")
SLOT_PER_HARI = 5
N_SLOT = len(HARI) * SLOT_PER_HARI  # 25 Slot

JAM_MULAI = ["07:00", "09:30", "12:50", "15:20", "17:50"]
JAM_SELESAI = ["09:30", "12:00", "15:20", "17:50", "20:20"]

# 20 Mata Kuliah dengan Tepat 8 Dosen Unik (Kelas A & B)
MATA_KULIAH = [
    # --- KELAS A ---
    {"kode": "MK01", "nama": "Algoritma & Pemrograman", "dosen": "NOVERA KRISTIANTI, S.T., M.T.", "kelas": "A", "mhs": 40},
    {"kode": "MK02", "nama": "Matematika Diskrit",       "dosen": "DRS. JADIAMAN PARHUSIP, M.KOM.", "kelas": "A", "mhs": 40},
    {"kode": "MK03", "nama": "Pengantar Teknologi Info", "dosen": "DEVI KAROLITA, S.KOM., M.KOM., PH.D.", "kelas": "A", "mhs": 40},
    {"kode": "MK04", "nama": "Struktur Data",            "dosen": "TOMAS LEONARDO, S.T., M.T.I.", "kelas": "A", "mhs": 38},
    {"kode": "MK05", "nama": "Basis Data",               "dosen": "CHRISTIAN NOVAN, S.KOM., M.ENG.", "kelas": "A", "mhs": 38},
    {"kode": "MK06", "nama": "Jaringan Komputer",        "dosen": "NAHUMI NUGRAHANINGSIH, S.T., M.T., PH.D.", "kelas": "A", "mhs": 38},
    {"kode": "MK07", "nama": "Kecerdasan Buatan",        "dosen": "DEDDY RONALDO, S.T., M.T.", "kelas": "A", "mhs": 35},
    {"kode": "MK08", "nama": "Pemrograman Web",          "dosen": "LICANTIK, S.KOM., M.KOM.", "kelas": "A", "mhs": 35},
    {"kode": "MK09", "nama": "Keamanan Informasi",       "dosen": "NOVERA KRISTIANTI, S.T., M.T.", "kelas": "A", "mhs": 35},
    {"kode": "MK10", "nama": "Sistem Operasi",           "dosen": "DRS. JADIAMAN PARHUSIP, M.KOM.", "kelas": "A", "mhs": 30},

    # --- KELAS B ---
    {"kode": "MK11", "nama": "Algoritma & Pemrograman", "dosen": "NOVERA KRISTIANTI, S.T., M.T.", "kelas": "B", "mhs": 38},
    {"kode": "MK12", "nama": "Matematika Diskrit",       "dosen": "DRS. JADIAMAN PARHUSIP, M.KOM.", "kelas": "B", "mhs": 38},
    {"kode": "MK13", "nama": "Pengantar Teknologi Info", "dosen": "DEVI KAROLITA, S.KOM., M.KOM., PH.D.", "kelas": "B", "mhs": 38},
    {"kode": "MK14", "nama": "Struktur Data",            "dosen": "TOMAS LEONARDO, S.T., M.T.I.", "kelas": "B", "mhs": 35},
    {"kode": "MK15", "nama": "Basis Data",               "dosen": "CHRISTIAN NOVAN, S.KOM., M.ENG.", "kelas": "B", "mhs": 35},
    {"kode": "MK16", "nama": "Jaringan Komputer",        "dosen": "NAHUMI NUGRAHANINGSIH, S.T., M.T., PH.D.", "kelas": "B", "mhs": 35},
    {"kode": "MK17", "nama": "Kecerdasan Buatan",        "dosen": "DEDDY RONALDO, S.T., M.T.", "kelas": "B", "mhs": 30},
    {"kode": "MK18", "nama": "Pemrograman Web",          "dosen": "LICANTIK, S.KOM., M.KOM.", "kelas": "B", "mhs": 30},
    {"kode": "MK19", "nama": "Keamanan Informasi",       "dosen": "NOVERA KRISTIANTI, S.T., M.T.", "kelas": "B", "mhs": 30},
    {"kode": "MK20", "nama": "Sistem Operasi",           "dosen": "DRS. JADIAMAN PARHUSIP, M.KOM.", "kelas": "B", "mhs": 28},
]
N_MK = len(MATA_KULIAH)

# 5 Ruang
RUANGAN = [
    {"kode": "R1 (Kap 45)", "kap": 45}, 
    {"kode": "R2 (Kap 45)", "kap": 45}, 
    {"kode": "R3 (Kap 40)", "kap": 40}, 
    {"kode": "R4 (Kap 35)", "kap": 35}, 
    {"kode": "R5 (Kap 30)", "kap": 30}
]
N_RUANG = len(RUANGAN)

# =====================================================================
# [POIN 2 & 3] REPRESENTASI KROMOSOM & FUNGSI FITNESS
# =====================================================================
def hitung_pelanggaran_keras(kromosom):
    per_slot = {}
    for i, (slot, ruang) in enumerate(kromosom):
        if slot not in per_slot: per_slot[slot] = []
        per_slot[slot].append(i)

    dosen_bentrok = 0
    ruang_bentrok = 0
    kelas_bentrok = 0
    
    for slot, mk_indices in per_slot.items():
        if len(mk_indices) < 2: continue
        
        dosen_counts, ruang_counts, kelas_counts = {}, {}, {}
        for i in mk_indices:
            mk = MATA_KULIAH[i]
            dosen_counts[mk['dosen']] = dosen_counts.get(mk['dosen'], 0) + 1
            ruang_counts[kromosom[i][1]] = ruang_counts.get(kromosom[i][1], 0) + 1
            kelas_counts[mk['kelas']] = kelas_counts.get(mk['kelas'], 0) + 1
            
        dosen_bentrok += sum(c * (c - 1) // 2 for c in dosen_counts.values())
        ruang_bentrok += sum(c * (c - 1) // 2 for c in ruang_counts.values())
        kelas_bentrok += sum(c * (c - 1) // 2 for c in kelas_counts.values())

    kapasitas_kurang = 0
    for i, (_, r) in enumerate(kromosom):
        if MATA_KULIAH[i]['mhs'] > RUANGAN[r]['kap']:
            kapasitas_kurang += 1

    return dosen_bentrok + ruang_bentrok + kelas_bentrok + kapasitas_kurang

def hitung_fitness(kromosom):
    pelanggaran = hitung_pelanggaran_keras(kromosom)
    return 1.0 / (1.0 + pelanggaran)
    
# =====================================================================
# [POIN 4] OPERATOR GENETIKA & LOOP EVOLUSI
# =====================================================================
def inisialisasi_populasi(ukuran_populasi):
    populasi = []
    for _ in range(ukuran_populasi):
        kromosom = [(random.randint(0, N_SLOT - 1), random.randint(0, N_RUANG - 1)) for _ in range(N_MK)]
        populasi.append(kromosom)
    return populasi

def seleksi_turnamen(populasi, k=3):
    peserta = random.sample(populasi, k)
    return max(peserta, key=hitung_fitness)

def crossover_uniform(p1, p2):
    anak1, anak2 = [], []
    for gen1, gen2 in zip(p1, p2):
        if random.random() < 0.5:
            anak1.append(gen1); anak2.append(gen2)
        else:
            anak1.append(gen2); anak2.append(gen1)
    return anak1, anak2

def mutasi_acak(kromosom, prob_mutasi):
    for i in range(N_MK):
        if random.random() < prob_mutasi:
            kromosom[i] = (random.randint(0, N_SLOT - 1), random.randint(0, N_RUANG - 1))
    return kromosom

def jalankan_ga(seed):
    random.seed(seed)
    POP_SIZE = 100
    MAX_GEN = 200
    P_CROSSOVER = 0.8
    P_MUTASI = 0.05
    ELITISM = 2
    
    populasi = inisialisasi_populasi(POP_SIZE)
    riwayat_terbaik, riwayat_rata2 = [], []
    gen_valid_pertama = None
    
    for gen in range(MAX_GEN):
        populasi = sorted(populasi, key=hitung_fitness, reverse=True)
        fitness_terbaik = hitung_fitness(populasi[0])
        fitness_rata2 = statistics.mean(hitung_fitness(k) for k in populasi)
        
        riwayat_terbaik.append(fitness_terbaik)
        riwayat_rata2.append(fitness_rata2)
        
        if gen_valid_pertama is None and hitung_pelanggaran_keras(populasi[0]) == 0:
            gen_valid_pertama = gen
            
        populasi_baru = populasi[:ELITISM]
        
        while len(populasi_baru) < POP_SIZE:
            p1 = seleksi_turnamen(populasi) 
            p2 = seleksi_turnamen(populasi)
            
            if random.random() < P_CROSSOVER:
                a1, a2 = crossover_uniform(p1, p2)
            else:
                a1, a2 = list(p1), list(p2)
                
            a1 = mutasi_acak(a1, P_MUTASI)
            a2 = mutasi_acak(a2, P_MUTASI)
            populasi_baru.extend([a1, a2])
            
        populasi = populasi_baru[:POP_SIZE]
        
    populasi = sorted(populasi, key=hitung_fitness, reverse=True)
    return {
        "best_kromosom": populasi[0],
        "fitness": hitung_fitness(populasi[0]),
        "pelanggaran": hitung_pelanggaran_keras(populasi[0]),
        "gen_valid": gen_valid_pertama,
        "riwayat_terbaik": riwayat_terbaik,
        "riwayat_rata2": riwayat_rata2
    }

# =====================================================================
# [POIN 5 & 6] PENGUJIAN AWAL & OUTPUT TABEL  
# =====================================================================
def eksperimen_10_run():
    print("=== [POIN 5] PENGUJIAN AWAL: 10 RUN DENGAN SEED BERBEDA ===")
    best_res_overall = None
    
    for i in range(10):
        seed = i + 1
        res = jalankan_ga(seed)
        print(f"Run {seed:2d} | Fitness: {res['fitness']:.4f} | Bentrok: {res['pelanggaran']:2d} | Gen Valid Pertama: {res['gen_valid']}")
        
        if best_res_overall is None or res['fitness'] > best_res_overall['fitness']:
            best_res_overall = res
            
    print("-" * 65)
    return best_res_overall

def tampilkan_output_tabel(best_res):
    print("\n" + "="*150)
    print("OUTPUT JADWAL KULIAH TERBAIK (Format Tabel)")
    print("="*150)
    
    jadwal_list = []
    for i, (slot, ruang) in enumerate(best_res["best_kromosom"]):
        hari_idx = slot // SLOT_PER_HARI
        jam_idx = slot % SLOT_PER_HARI
        
        jadwal_string = f"{HARI[hari_idx]}, {JAM_MULAI[jam_idx]}-{JAM_SELESAI[jam_idx]} DI {RUANGAN[ruang]['kode']}"
        
        jadwal_list.append({
            "kode": MATA_KULIAH[i]['kode'],
            "mata_kuliah": MATA_KULIAH[i]['nama'],
            "kelas": MATA_KULIAH[i]['kelas'],
            "dosen": MATA_KULIAH[i]['dosen'],
            "jadwal": jadwal_string,
            "sort_key": slot
        })
        
    # Urutkan jadwal berdasarkan urutan hari & jam
    jadwal_list.sort(key=lambda x: x["sort_key"])

 # =====================================================================
    # PRINT TAMPIL TABEL DAN CSV DAN GRAFIK
    # =====================================================================
    # Cetak Format Tabel (Nomor urut pakai enumerate)
    print(f"{'No':<4} | {'Kode':<6} | {'Mata Kuliah':<30} | {'Kelas':<6} | {'Dosen Ampu':<45} | {'Jadwal Kuliah'}")
    print("-" * 150)
    for idx, row in enumerate(jadwal_list, start=1):
        print(f"{idx:<4} | {row['kode']:<6} | {row['mata_kuliah']:<30} | {row['kelas']:<6} | {row['dosen']:<45} | {row['jadwal']}")

    # Ekspor ke CSV
    with open("jadwal_uts_terbaik.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["No", "Kode", "Mata Kuliah", "Kelas", "Dosen Ampu", "Jadwal Kuliah"])
        for idx, row in enumerate(jadwal_list, start=1):
            writer.writerow([idx, row['kode'], row['mata_kuliah'], row['kelas'], row['dosen'], row['jadwal']])
    print("\n[INFO] Jadwal diekspor ke 'jadwal_uts_terbaik.csv'")

    # Grafik Konvergensi
    plt.figure(figsize=(10, 5))
    plt.plot(best_res["riwayat_terbaik"], label="Fitness Terbaik", color='#2ca02c', linewidth=2)
    plt.plot(best_res["riwayat_rata2"], label="Fitness Rata-rata", color='#ff7f0e', linestyle='--')
    plt.title("Grafik Konvergensi AG (Hasil Terbaik dari 10 Run)")
    plt.xlabel("Generasi")
    plt.ylabel("Nilai Fitness")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("grafik_konvergensi_uts.png")
    print("[INFO] Grafik konvergensi disimpan sebagai 'grafik_konvergensi_uts.png'")
    plt.show()

if __name__ == "__main__":
    hasil_terbaik = eksperimen_10_run()
    tampilkan_output_tabel(hasil_terbaik) 
