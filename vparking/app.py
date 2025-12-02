import tkinter as tk
from tkinter import messagebox
from gui_base import *
from data_manager import DataManager
from parking_logic import ParkingLogic

class ParkingApp:

    
    def __init__(self, master):
        
        self.master = master
        master.title("Aplikasi Parkir Modular 7 File")

        # Data & logika
        self.data = DataManager()
        self.logic = ParkingLogic(self.data)

        # Frame utama
        main = tk.Frame(master, padx=15, pady=15)
        main.pack(fill='both')

        # ---- FRAME KAPASITAS ----
        cap_frame = make_frame(main, "Kapasitas Parkir")
        cap_frame.pack(fill='x', pady=10)

        tk.Label(cap_frame, text="Kapasitas Maksimum:", font=FONT_NORMAL).pack(side='left')
        self.cap_var = tk.StringVar(value=str(self.logic.max_capacity))
        tk.Entry(cap_frame, width=5, textvariable=self.cap_var).pack(side='left', padx=5)
        tk.Button(cap_frame, text="Set", command=self.set_capacity).pack(side='left', padx=5)

        self.cap_label = tk.Label(cap_frame, text="", font=FONT_H2, fg='blue')
        self.cap_label.pack(pady=5)

        # ---- FRAME INPUT ----
        input_frame = make_frame(main, "Input Kendaraan")
        input_frame.pack(fill='x', pady=10)
        
        tk.Label(input_frame, text="Plat Nomor:", font=FONT_NORMAL).pack(anchor='w')
        self.plat_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.plat_var, font=('Helvetica', 18), width=20).pack(ipady=5)

        btn_frame = tk.Frame(input_frame)
        btn_frame.pack(pady=10)
        # pengagnti tombol parkir masuk kursor bawah
        master.bind('<Down>', lambda event: self.park_in())
        # pengagnti tombol parkir keluar kursor atas
        master.bind('<Up>', lambda event: self.park_out())

        tk.Button(btn_frame, text="Parkir Masuk", width=12, bg="#4CAF50", fg="black",
                  command=self.park_in).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Parkir Keluar", width=12, bg="#F44336", fg="black",
                  command=self.park_out).pack(side='left', padx=5)

        # ---- FRAME STATUS ----
        status_frame = make_frame(main, "Status Parkir Sekarang")
        status_frame.pack(fill='both', pady=10)

        self.listbox = tk.Listbox(status_frame, width=50, height=10, font=FONT_MONO)
        self.listbox.pack()

        self.update_status()

    # ---- METHOD ---
    def set_capacity(self):
        try:
            new_max = int(self.cap_var.get())
            if new_max <= 0:
                raise ValueError
            self.logic.set_capacity(new_max)
            self.update_status()
        except:
            tk.messagebox.showerror("Error", "Kapasitas harus bilangan positif.")

    def park_in(self):
        plat = self.plat_var.get().strip().upper()
        if not plat:
            tk.messagebox.showerror("Error", "Plat tidak boleh kosong.")
            return

        status, msg = self.logic.park_in(plat)
        tk.messagebox.showinfo("Informasi" if status else "Gagal", msg)

        self.update_status()

    def park_out(self):
        plat = self.plat_var.get().strip().upper()
        if not plat:
            tk.messagebox.showerror("Error", "Plat tidak boleh kosong.")
            return

        status, data = self.logic.park_out(plat)

        if not status:
            messagebox.showwarning("Gagal", data)
            return

        msg = (
            f"Plat: {data['plat']}\n"
            f"Masuk: {data['masuk']}\n"
            f"Keluar: {data['keluar']}\n"
            f"Durasi: {data['durasi_menit']} menit\n"
            f"Tagihan: {data['jam_tagihan']} jam\n"
            f"TOTAL: Rp {data['biaya']:,}"
        )
        tk.messagebox.showinfo("Kuitansi", msg)

        self.update_status()

    def update_status(self):
        self.listbox.delete(0, tk.END)

        current = len(self.data.parking_lot)
        maxcap = self.logic.max_capacity
        self.cap_label.config(text=f"{current}/{maxcap} slot terisi")

        if current == 0:
            self.listbox.insert(tk.END, "Parkiran kosong.")
            return

        for plat, waktu in self.data.parking_lot.items():
            self.listbox.insert(tk.END, f"{plat}\t{waktu.strftime('%H:%M:%S')}")
