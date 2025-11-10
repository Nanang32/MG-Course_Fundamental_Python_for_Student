def cek_genap_ganjil(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

# Input dari pengguna
n = int(input("Masukkan angka: "))
print(f"Angka {n} adalah {cek_genap_ganjil(n)}")