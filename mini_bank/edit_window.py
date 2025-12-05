import tkinter as tk
from tkinter import messagebox
from data_manager import load_data, update_record

def open_edit_window(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin diedit!")
        return

    index = int(tree.item(selected[0])["values"][0])
    data = load_data()[index]

    win = tk.Toplevel()
    win.title("Edit Data")

    tk.Label(win, text="Nama").grid(row=0, column=0)
    tk.Label(win, text="Kelas").grid(row=1, column=0)
    tk.Label(win, text="Jumlah").grid(row=2, column=0)

    nama_e = tk.Entry(win)
    kelas_e = tk.Entry(win)
    jumlah_e = tk.Entry(win)

    nama_e.grid(row=0, column=1)
    kelas_e.grid(row=1, column=1)
    jumlah_e.grid(row=2, column=1)

    nama_e.insert(0, data["nama"])
    kelas_e.insert(0, data["kelas"])
    jumlah_e.insert(0, data["jumlah"])

    def save_changes():
        update_record(index, nama_e.get(), kelas_e.get(), jumlah_e.get())
        tree.event_generate("<<Refresh>>")
        win.destroy()

    tk.Button(win, text="Simpan", command=save_changes).grid(row=3, column=0, columnspan=2)
