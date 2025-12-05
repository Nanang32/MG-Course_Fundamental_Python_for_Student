import tkinter as tk
from tkinter import ttk, messagebox
from data_manager import load_data, add_record, delete_record
from edit_window import open_edit_window

def refresh_table(tree):
    for row in tree.get_children():
        tree.delete(row)
    for i, item in enumerate(load_data()):
        tree.insert("", "end", values=(i, item["nama"], item["kelas"], item["jumlah"]))

def add_data(nama_e, kelas_e, jumlah_e, tree):
    nama = nama_e.get()
    kelas = kelas_e.get()
    jumlah = jumlah_e.get()

    if not nama or not kelas or not jumlah:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    add_record(nama, kelas, jumlah)
    refresh_table(tree)

    nama_e.delete(0, tk.END)
    kelas_e.delete(0, tk.END)
    jumlah_e.delete(0, tk.END)

def delete_data(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
        return

    index = int(tree.item(selected[0])["values"][0])
    delete_record(index)
    refresh_table(tree)

def run_app():
    root = tk.Tk()
    root.title("Aplikasi Tabungan Siswa")
    root.geometry("600x400")

    frame_input = tk.Frame(root)
    frame_input.pack(pady=10)

    tk.Label(frame_input, text="Nama").grid(row=0, column=0)
    tk.Label(frame_input, text="Kelas").grid(row=1, column=0)
    tk.Label(frame_input, text="Jumlah (RP)").grid(row=2, column=0)

    nama_e = tk.Entry(frame_input)
    kelas_e = tk.Entry(frame_input)
    jumlah_e = tk.Entry(frame_input)

    nama_e.grid(row=0, column=1)
    kelas_e.grid(row=1, column=1)
    jumlah_e.grid(row=2, column=1)

    tree = ttk.Treeview(root, columns=("ID", "Nama", "Kelas", "Jumlah"), show="headings")
    for col in ("ID", "Nama", "Kelas", "Jumlah"):
        tree.heading(col, text=col)
    tree.pack()

    refresh_table(tree)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Tambah", command=lambda: add_data(nama_e, kelas_e, jumlah_e, tree)).grid(row=0, column=0)
    tk.Button(btn_frame, text="Hapus", command=lambda: delete_data(tree)).grid(row=0, column=1)
    tk.Button(btn_frame, text="Edit", command=lambda: open_edit_window(tree)).grid(row=0, column=2)

    root.mainloop()
