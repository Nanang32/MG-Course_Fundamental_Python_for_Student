# Program untuk input nama dan simpan ke nama.txt

print("=== Input Nama Siswa ===")
print("Ketik 'stop' untuk selesai.\n")

with open("nama.txt", "a") as file:  # gunakan "a" agar menambah, bukan menimpa
    while True:
        nama = input("Masukkan nama: ")

        if nama.lower() == "stop":
            print("\nInput selesai! Data disimpan ke nama.txt")
            break

        # Tulis nama ke file
        file.write(nama + "\n")
        print("✔ Nama disimpan!\n")
