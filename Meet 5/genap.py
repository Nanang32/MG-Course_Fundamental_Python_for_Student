# Program bilangan genap dan ganjil

n = int(input("Masukkan batas angka: "))

print("Bilangan Genap:")
for i in range(1, n + 1):
    # Simbol % di Python disebut operator modulus (modulo).
    # Fungsinya adalah untuk menghitung sisa hasil pembagian dari dua angka.
    if i % 2 == 0:
        print(i, end=" ")

print("\nBilangan Ganjil:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
