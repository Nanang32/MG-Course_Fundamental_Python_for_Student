
nama = input("Masukkan nama siswa: ")
nilai = float(input("Masukkan nilai siswa: "))

# Logika kondisi
if nilai >= 60:
    print(f"Selamat {nama}, Anda dinyatakan LULUS dengan nilai {nilai}.")
else:
    print(f"Maaf {nama}, Anda dinyatakan TIDAK LULUS dengan nilai {nilai}.")