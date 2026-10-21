"""
PROYEK KELOMPOK ALGORITMA GENETIKA - TAHAP 1 (UTS)
Sistem Optimasi Penjadwalan Kuliah
Sesuai Ketentuan PDF: 20 MK, 8 Dosen, 5 Ruang, 5 Hari x 5 Slot.
Format Output Tabel: Sesuai Referensi Gambar.
"""

import csv
import random
import time
import statistics
import matplotlib.pyplot as plt

# =====================================================================
# [POIN 1] PEMODELAN MASALAH & DATA (Sesuai Target UTS)
# =====================================================================
HARI = ("SENIN", "SELASA", "RABU", "KAMIS", "JUMAT")
SLOT_PER_HARI = 5
N_SLOT = len(HARI) * SLOT_PER_HARI  # 25 Slot

# Pemetaan String Jam untuk Output
JAM_MULAI = ["07:00", "09:30", "12:50", "15:20", "17:50"]
JAM_SELESAI = ["09:30", "12:00", "15:20", "17:50", "20:20"]

# 20 Mata Kuliah, 8 Dosen, 6 Kelas
MATA_KULIAH = [
    {"kode": "MK01", "nama": "Algoritma & Pemrograman", "dosen": "Dosen 1, M.Kom.", "kelas": "IF-1A", "mhs": 40},
    {"kode": "MK02", "nama": "Matematika Diskrit",       "dosen": "Dosen 2, M.T.", "kelas": "IF-1A", "mhs": 40},
    {"kode": "MK03", "nama": "Pengantar Teknologi Info", "dosen": "Dosen 3, Ph.D.", "kelas": "IF-1A", "mhs": 40},
    {"kode": "MK04", "nama": "Algoritma & Pemrograman", "dosen": "Dosen 1, M.Kom.", "kelas": "IF-1B", "mhs": 38},
    {"kode": "MK05", "nama": "Matematika Diskrit",       "dosen": "Dosen 2, M.T.", "kelas": "IF-1B", "mhs": 38},
    {"kode": "MK06", "nama": "Pengantar Teknologi Info", "dosen": "Dosen 3, Ph.D.", "kelas": "IF-1B", "mhs": 38},
    {"kode": "MK07", "nama": "Struktur Data",            "dosen": "Dosen 1, M.Kom.", "kelas": "IF-2A", "mhs": 35},
    {"kode": "MK08", "nama": "Basis Data",               "dosen": "Dosen 4, M.Kom.", "kelas": "IF-2A", "mhs": 35},
    {"kode": "MK09", "nama": "Jaringan Komputer",        "dosen": "Dosen 5, M.T.", "kelas": "IF-2A", "mhs": 35},
    {"kode": "MK10", "nama": "Struktur Data",            "dosen": "Dosen 1, M.Kom.", "kelas": "IF-2B", "mhs": 33},
    {"kode": "MK11", "nama": "Basis Data",               "dosen": "Dosen 4, M.Kom.", "kelas": "IF-2B", "mhs": 33},
    {"kode": "MK12", "nama": "Jaringan Komputer",        "dosen": "Dosen 5, M.T.", "kelas": "IF-2B", "mhs": 33},
    {"kode": "MK13", "nama": "Kecerdasan Buatan",        "dosen": "Dosen 6, Ph.D.", "kelas": "IF-3A", "mhs": 30},
    {"kode": "MK14", "nama": "Pemrograman Web",          "dosen": "Dosen 7, M.Kom.", "kelas": "IF-3A", "mhs": 30},
    {"kode": "MK15", "nama": "Keamanan Informasi",       "dosen": "Dosen 8, M.T.", "kelas": "IF-3A", "mhs": 30},
    {"kode": "MK16", "nama": "Kecerdasan Buatan",        "dosen": "Dosen 6, Ph.D.", "kelas": "IF-3B", "mhs": 28},
    {"kode": "MK17", "nama": "Pemrograman Web",          "dosen": "Dosen 7, M.Kom.", "kelas": "IF-3B", "mhs": 28},
    {"kode": "MK18", "nama": "Keamanan Informasi",       "dosen": "Dosen 8, M.T.", "kelas": "IF-3B", "mhs": 28},
    {"kode": "MK19", "nama": "Sistem Operasi",           "dosen": "Dosen 5, M.T.", "kelas": "IF-2A", "mhs": 35},
    {"kode": "MK20", "nama": "Sistem Operasi",           "dosen": "Dosen 2, M.T.", "kelas": "IF-2B", "mhs": 33},
]
N_MK = len(MATA_KULIAH)

# 5 Ruang dengan Kapasitas Berbeda
RUANGAN = [
    {"kode": "R1 (Kap 45)", "kap": 45}, 
    {"kode": "R2 (Kap 45)", "kap": 45}, 
    {"kode": "R3 (Kap 40)", "kap": 40}, 
    {"kode": "R4 (Kap 35)", "kap": 35}, 
    {"kode": "R5 (Kap 30)", "kap": 30}
]
N_RUANG = len(RUANGAN)
