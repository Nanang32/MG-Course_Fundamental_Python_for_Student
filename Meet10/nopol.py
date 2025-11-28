import sys

print("=== Input Plat Kendaraan ===")
print("Ketik 'stop' untuk menghentikan aplikasi.\n")

with open("plat.txt", "a") as file:
    while True:
        plat = input("Masukkan plat kendaraan: ")

        # Perintah stop → hentikan aplikasi
        if plat.lower() == "stop":
            print("\nAplikasi dihentikan.")
            print("Data berhasil disimpan ke file 'plat.txt'\n")
            sys.exit()  # langsung keluar dari aplikasi

        # Simpan ke file
        file.write(plat + "\n")
        print("✔ Plat kendaraan disimpan!\n")
