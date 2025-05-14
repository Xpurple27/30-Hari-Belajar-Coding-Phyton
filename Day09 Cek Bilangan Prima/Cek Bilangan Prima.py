# Day 09 - Cek Bilangan Prima

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("🔍 Program Cek Bilangan Prima")
angka = int(input("Masukkan sebuah bilangan bulat positif: "))

if is_prime(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")
