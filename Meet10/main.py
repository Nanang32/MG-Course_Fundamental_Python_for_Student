# Membaca file input
with open("nama.txt", "r") as file:
    data = file.readlines()

# Proses: buat kalimat
hasil = []
for nama in data:
    hasil.append(f"Nama siswa: {nama.strip()}")

# Menulis output ke file baru
with open("hasil.txt", "w") as file:
    for h in hasil:
        file.write(h + "\n")

print("Proses selesai! File 'hasil.txt' dibuat.")
