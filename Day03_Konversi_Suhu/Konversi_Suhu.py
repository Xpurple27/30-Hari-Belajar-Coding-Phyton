# Day 2 - Program Konversi Suhu

print("=== Program Konversi Suhu ===")

# Input suhu dan satuan asal
suhu = float(input("Masukkan nilai suhu: "))
satuan_asal = input("Masukkan satuan asal (C/F/K): ").upper()

# Pilih satuan tujuan
satuan_tujuan = input("Masukkan satuan tujuan (C/F/K): ").upper()


# Fungsi konversi suhu
def konversi_suhu(nilai, asal, tujuan): #Definisikan konversi suhu
    if asal == tujuan:
        return nilai

    # Konversi ke Celsius dulu
    if asal == 'F':
        nilai_c = (nilai - 32) * 5 / 9
    elif asal == 'K':
        nilai_c = nilai - 273.15
    elif asal == 'C':
        nilai_c = nilai
    else:
        print("Satuan asal tidak valid!")
        return None

    # Konversi dari Celsius ke tujuan
    if tujuan == 'F':
        hasil = (nilai_c * 9 / 5) + 32
    elif tujuan == 'K':
        hasil = nilai_c + 273.15
    elif tujuan == 'C':
        hasil = nilai_c
    else:
        print("Satuan tujuan tidak valid!")
        return None

    return hasil


# Panggil fungsi dan tampilkan hasil
hasil_konversi = konversi_suhu(suhu, satuan_asal, satuan_tujuan)

if hasil_konversi is not None:
    print(f"{suhu}°{satuan_asal} = {round(hasil_konversi, 2)}°{satuan_tujuan}")
