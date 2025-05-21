# Day 13 - Kalkulator Waktu

def total_waktu(jam1, menit1, jam2, menit2):
    total_menit = (jam1 * 60 + menit1) + (jam2 * 60 + menit2)
    hasil_jam = total_menit // 60
    hasil_menit = total_menit % 60
    return hasil_jam, hasil_menit

print("Kalkulator Penjumlahan Waktu")
jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))
jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))

jam, menit = total_waktu(jam1, menit1, jam2, menit2)
print(f"Total waktu adalah {jam} jam {menit} menit")
