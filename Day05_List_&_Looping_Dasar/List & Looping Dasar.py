# Day 05 - List & Looping Dasar

print("=== Program Daftar Kegiatan Harian ===")

# Buat list kosong
List = []

# Input kegiatan Mu
n = int(input("Seberapa banyak kegitatan mu ? "))

for i in range(n):
    kegiatan = input(f"Masukkan kegiatan ke-{i+1}: ")
    List.append(kegiatan)

# Tampilkan daftar kegiatan
print("\nDaftar kegiatan harian kamu:")
for nomor, kegiatan in enumerate(List, start=1):
    print(f"{nomor}. {kegiatan}")
