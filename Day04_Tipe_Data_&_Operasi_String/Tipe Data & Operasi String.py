# Day 04 - Tipe Data & Operasi String

print("=== Program Operasi String ===")

# Input nama lengkap
nama_lengkap = input("Masukkan nama lengkap: ")

# Operasi dasar string
print(f"\nPanjang nama kamu adalah: {len(nama_lengkap)} karakter")
print(f"\nHuruf kapital semua: {nama_lengkap.upper()}")
print(f"\nHuruf kecil semua: {nama_lengkap.lower()}")
print(f"\nHuruf pertama kapital: {nama_lengkap.title()}")
print(f"\nNama dibalik: {nama_lengkap[::-1]}")

# Cek apakah nama mengandung huruf tertentu
huruf_cari = input("\nMasukkan huruf yang ingin dicari di nama kamu: ")
jumlah = nama_lengkap.lower().count(huruf_cari.lower())
print(f"\nHuruf '{huruf_cari}' ditemukan sebanyak {jumlah} kali dalam nama kamu.")
