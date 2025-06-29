# Day 16 - Program To-Do List Sederhana

to_do_list = []

def tampilkan_menu():
    print("\n📋 Menu To-Do List")
    print("1. Lihat daftar tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def tampilkan_tugas():
    if not to_do_list:
        print("❌ Tidak ada tugas saat ini.")
    else:
        print("\n📝 Daftar Tugas:")
        for i, tugas in enumerate(to_do_list, 1):
            print(f"{i}. {tugas}")

def tambah_tugas():
    tugas = input("Masukkan nama tugas: ")
    to_do_list.append(tugas)
    print("✅ Tugas berhasil ditambahkan!")

def hapus_tugas():
    tampilkan_tugas()
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(to_do_list):
            tugas_dihapus = to_do_list.pop(nomor - 1)
            print(f"🗑️ Tugas '{tugas_dihapus}' berhasil dihapus.")
        else:
            print("⚠️ Nomor tugas tidak valid.")
    except ValueError:
        print("⚠️ Masukkan angka yang valid.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tampilkan_tugas()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        print("👋 Keluar dari program. Sampai jumpa!")
        break
    else:
        print("⚠️ Pilihan tidak valid.")
