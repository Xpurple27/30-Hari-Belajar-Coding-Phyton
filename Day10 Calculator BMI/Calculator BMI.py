# Day 10 - Kalkulator BMI

def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

print("⚖️ Kalkulator BMI (Body Mass Index)")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

bmi = hitung_bmi(berat, tinggi)
print(f"\nBMI Anda: {bmi:.2f}")

if bmi < 18.5:
    status = "Kurus"
elif 18.5 <= bmi < 25:
    status = "Normal"
elif 25 <= bmi < 30:
    status = "Kelebihan berat badan"
else:
    status = "Obesitas"

print(f"Status: {status}")
