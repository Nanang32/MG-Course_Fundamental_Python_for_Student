import tkinter as tk
from tkinter import messagebox

# Fungsi ketika tombol Submit ditekan
def submit():
    nama = entry_nama.get()
    nisn = entry_nisn.get()
    mapel = entry_mapel.get()

    if nama == "" or nisn == "" or mapel == "":
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
    else:
        messagebox.showinfo("Sukses", f"Data berhasil disimpan!\n\n"
                                      f"Nama: {nama}\n"
                                      f"Semester: {nisn}\n"
                                      f"Mata Kuliah: {mapel}")
        print("=== DATA PENDAFTARAN ===")
        print("Nama       :", nama)
        print("NISN        :", nisn)
        print("Mata Pelajaran:", mapel)

# Membuat window
root = tk.Tk()
root.title("Form Pendaftaran SISWA SMKN 1 MAROS")
root.geometry("400x300")

# Label dan Entry
tk.Label(root, text="Nama").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="NISN").pack()
entry_nisn = tk.Entry(root)
entry_nisn.pack()

tk.Label(root, text="Mata Pelajaran").pack()
entry_mapel = tk.Entry(root)
entry_mapel.pack()

# Tombol Submit
tk.Button(root, text="Submit", command=submit).pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
