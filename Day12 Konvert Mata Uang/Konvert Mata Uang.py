# Day 12 - Konversi Mata Uang

# Kurs sederhana (misalnya 1 USD = 15.000 IDR)
kurs = {"USD": 15000,"EUR": 16500,"JPY": 110,"SGD": 11200}

print("💱 Konversi Mata Uang ke Rupiah")
mata_uang = input("Masukkan kode mata uang (USD, EUR, JPY, SGD): ").upper()
jumlah = float(input(f"Masukkan jumlah dalam {mata_uang}: "))

if mata_uang in kurs:
    rupiah = jumlah * kurs[mata_uang]
    print(f"{jumlah} {mata_uang} = Rp {rupiah:,.2f}")
else:
    print("⚠️ Mata uang tidak tersedia.")
