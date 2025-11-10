angka = int(input("Masukkan angka: "))

print(f"Tabel perkalian {angka}")
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")


"""
| Bagian Kode              | Fungsi                                         |
| ------------------------ | ---------------------------------------------- |
| `input()`                | Menerima input dari pengguna                   |
| `int()`                  | Mengubah input jadi bilangan bulat             |
| `for i in range(1, 11):` | Mengulang 10 kali (1–10)                       |
| `print(f"...")`          | Menampilkan hasil perkalian dengan format rapi |

"""