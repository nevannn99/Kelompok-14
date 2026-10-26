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
