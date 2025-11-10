def rata_rata(nilai1, nilai2, nilai3):
    return (nilai1 + nilai2 + nilai3) / 3

n1 = float(input("Masukkan nilai 1: "))
n2 = float(input("Masukkan nilai 2: "))
n3 = float(input("Masukkan nilai 3: "))

print(f"Nilai rata-rata = {rata_rata(n1, n2, n3):.2f}")
