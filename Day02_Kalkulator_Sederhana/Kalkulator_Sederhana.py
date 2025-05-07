print("=== Kalkulator Sederhana ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\nPilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    hasil = angka1 + angka2
    operasi = "+"
elif pilihan == '2':
    hasil = angka1 - angka2
    operasi = "-"
elif pilihan == '3':
    hasil = angka1 * angka2
    operasi = "*"
elif pilihan == '4':
    if angka2 != 0:
        hasil = angka1 / angka2
        operasi = "/"
    else:
        hasil = "Error: Tidak bisa dibagi 0"
        operasi = "/"
else:
    hasil = "Pilihan tidak valid"
    operasi = "?"

print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")
