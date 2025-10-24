

print("=== Program Konversi Suhu ===")


celsius = float(36.5)


# Rumus konversi
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Output hasil konversi
print("\nHasil Konversi:")
print("Celsius     :", celsius, "°C")
print("Fahrenheit  :", fahrenheit, "°F")
print("Kelvin      :", kelvin, "K")



"""
Deskripsi
| Bagian                              | Fungsi                               | Keterangan                           |
| :---------------------------------- | :----------------------------------- | :----------------------------------- |
| `input()`                           | Menerima nilai dari pengguna         | Suhu dimasukkan dalam satuan Celsius |
| `float()`                           | Mengubah input menjadi angka desimal | Agar bisa dikalikan/dibagi           |
| `fahrenheit = (celsius * 9/5) + 32` | Rumus konversi ke Fahrenheit         |                                      |
| `kelvin = celsius + 273.15`         | Rumus konversi ke Kelvin             |                                      |
| `print()`                           | Menampilkan hasil ke layar           | Format hasil konversi                |

"""