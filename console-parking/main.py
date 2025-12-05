import sys
from parkir_masuk import parkir_masuk
from parkir_keluar import parkir_keluar
from lihat_daftar import lihat_daftar

def menu():
    while True:
        print("=== APLIKASI VIRTUAL PARKIR ===")
        print("1. Parkir Masuk")
        print("2. Parkir Keluar")
        print("3. Lihat Daftar Parkir")
        print("4. Keluar Aplikasi")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            parkir_masuk()
        elif pilihan == "2":
            parkir_keluar()
        elif pilihan == "3":
            lihat_daftar()
        elif pilihan == "4":
            print("Aplikasi dihentikan.")
            sys.exit()
        else:
            print("❗ Pilihan tidak valid!\n")

menu()
