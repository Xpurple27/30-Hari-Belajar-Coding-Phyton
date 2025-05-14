# Day 08 - Random Number Generator

import random

print("🎲 Selamat datang di Program Random Number Generator!")

# Meminta input batas bawah dan atas
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

# Cek validitas batas
if batas_bawah >= batas_atas:
    print("Batas bawah harus lebih kecil dari batas atas!")
else:
    hasil = random.randint(batas_bawah, batas_atas)
    print(f"Angka acak antara {batas_bawah} dan {batas_atas} adalah: {hasil}")
