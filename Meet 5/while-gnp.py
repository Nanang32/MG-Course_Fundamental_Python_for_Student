n = int(input("Masukkan batas angka: "))

i = 1
print("Bilangan Genap:")
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

i = 1
print("\nBilangan Ganjil:")
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
