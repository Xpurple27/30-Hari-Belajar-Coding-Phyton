# Day 08 - Kalkulator Sederhana

def kalkulator(a, b, operasi):
    if operasi == '+':
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol!"
    else:
        return "Operasi tidak dikenal."

def main():
    print("=== Kalkulator Sederhana ===")
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")

    hasil = kalkulator(a, b, operasi)
    print(f"Hasil: {hasil}")

main()
