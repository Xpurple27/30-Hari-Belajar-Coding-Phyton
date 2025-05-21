# Day 14 - Penghitung Kata

def hitung_kata(kalimat):
    kata = kalimat.split()
    return len(kata)

print("Program Penghitung Kata")
kalimat = input("Masukkan kalimat: ")
jumlah = hitung_kata(kalimat)
print(f"Jumlah kata dalam kalimat adalah: {jumlah}")
