# Day 06 - Dictionary Dasar

print("=== Program Biodata Mahasiswa ===")

# Input biodata dari pengguna
nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
prodi = input("Masukkan program studi: ")
angkatan = input("Masukkan angkatan (tahun masuk): ")

# Simpan data dalam dictionary
biodata = {
    "Nama": nama,
    "NIM": nim,
    "Prodi": prodi,
    "Angkatan": angkatan
}

# Tampilkan biodata
print("\n=== Biodata Mahasiswa ===")
for key, value in biodata.items():
    print(f"{key}: {value}")
