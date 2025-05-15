# Day 11 - Game Tebak Angka

import random

print("🎯 Game Tebak Angka (1-100)")
angka_rahasia = random.randint(1, 100)
tebakan = None
percobaan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka antara 1 sampai 100: "))
    percobaan += 1
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"🎉 Selamat! Angka yang benar adalah {angka_rahasia}")
        print(f"Jumlah percobaan: {percobaan}")
