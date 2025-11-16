

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

# --- 1. Struktur Data dan Konstanta ---

parking_lot = {}
# Konstanta Biaya Parkir (Tidak berubah)
TARIF_PER_JAM = 5000
TARIF_MINIMUM = 3000
SATU_JAM_DETIK = 3600

# --- 2. Fungsi Logika Inti ---

def calculate_fee(duration_seconds):
    """Menghitung biaya parkir berdasarkan durasi dalam detik."""
    duration_hours = duration_seconds / SATU_JAM_DETIK

    if duration_hours <= 1:
        biaya = TARIF_MINIMUM
        jam_tagihan = 1
    else:
        jam_tagihan = math.ceil(duration_hours)
        biaya = TARIF_MINIMUM + ((jam_tagihan - 1) * TARIF_PER_JAM)
        
    return int(biaya), jam_tagihan

# --- 3. Kelas Aplikasi GUI (ParkingApp) ---

class ParkingApp:
    def __init__(self, master):
        self.master = master
        master.title("🅿️ Aplikasi Simulasi Parkir (Kapasitas)")
        
        # --- KAPASITAS PARKIR BARU ---
        self.max_capacity = 10  # Kapasitas Awal (Bisa disesuaikan)
        
        self.plat_var = tk.StringVar()
        
        # Konfigurasi Font
        self.font_h2 = ('Helvetica', 12, 'bold')
        self.font_normal = ('Helvetica', 10)
        self.font_mono = ('Courier', 10)

        main_frame = tk.Frame(master, padx=15, pady=15)
        main_frame.pack(fill='both', expand=True)

        # --- Bagian Kapasitas (Baru) ---
        capacity_frame = tk.LabelFrame(main_frame, text="Kapasitas Parkir", font=self.font_h2, padx=10, pady=5)
        capacity_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.capacity_label = tk.Label(capacity_frame, text="", font=('Helvetica', 14, 'bold'), fg='blue')
        self.capacity_label.pack(pady=5)
        
        # Input untuk mengubah kapasitas (opsional)
        tk.Label(capacity_frame, text="Ubah Kapasitas Maksimal:").pack(side=tk.LEFT, padx=5)
        self.capacity_entry = tk.Entry(capacity_frame, width=5)
        self.capacity_entry.insert(0, str(self.max_capacity))
        self.capacity_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(capacity_frame, text="Set", command=self.set_max_capacity).pack(side=tk.LEFT, padx=5)

        # --- Bagian Input Kontrol ---
        input_frame = tk.LabelFrame(main_frame, text="Kontrol", font=self.font_h2, padx=10, pady=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(input_frame, text="Nomor Plat:", font=self.font_normal).pack(pady=5, anchor='w')
        self.plat_entry = tk.Entry(input_frame, textvariable=self.plat_var, width=30, font=self.font_mono)
        self.plat_entry.pack(pady=5, padx=5)

        button_frame = tk.Frame(input_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="🚗 Masuk (Park In)", command=self.park_in_gui, 
                  bg='#4CAF50', fg='white', font=self.font_normal).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="🚪 Keluar (Park Out)", command=self.park_out_gui, 
                  bg='#F44336', fg='white', font=self.font_normal).pack(side=tk.LEFT, padx=10)

        # --- Bagian Status Parkir ---
        status_frame = tk.LabelFrame(main_frame, text="Kendaraan Aktif", font=self.font_h2, padx=10, pady=10)
        status_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.status_listbox = tk.Listbox(status_frame, width=50, height=8, font=self.font_mono)
        self.status_listbox.pack(padx=5, pady=5)
        
        self.update_status() # Panggil untuk memuat data awal dan status kapasitas

    def set_max_capacity(self):
        """Mengatur nilai kapasitas maksimal yang baru dari input."""
        try:
            new_capacity = int(self.capacity_entry.get())
            if new_capacity <= 0:
                 raise ValueError
            self.max_capacity = new_capacity
            messagebox.showinfo("Kapasitas Diperbarui", f"Kapasitas parkir diatur menjadi {self.max_capacity} slot.")
            self.update_status()
        except ValueError:
            messagebox.showerror("Input Invalid", "Kapasitas harus berupa angka bilangan bulat positif.")
            self.capacity_entry.delete(0, tk.END)
            self.capacity_entry.insert(0, str(self.max_capacity))

    def update_status(self):
        """Memperbarui Listbox dan Label Kapasitas."""
        current_cars = len(parking_lot)
        slots_available = self.max_capacity - current_cars
        
        # Update Label Kapasitas
        self.capacity_label.config(text=f"Slot Terisi: {current_cars} / {self.max_capacity} (Tersedia: {slots_available})")

        # Update Listbox
        self.status_listbox.delete(0, tk.END)
        if not parking_lot:
            self.status_listbox.insert(tk.END, "Tempat parkir kosong.")
        else:
            self.status_listbox.insert(tk.END, "PLAT NOMOR\t\tWAKTU MASUK")
            self.status_listbox.insert(tk.END, "--------------------------------------------------")
            for plat, waktu in parking_lot.items():
                waktu_str = waktu.strftime('%H:%M:%S')
                self.status_listbox.insert(tk.END, f"{plat:<15}\t\t{waktu_str}")

    def park_in_gui(self):
        """Handler untuk tombol Masuk. Termasuk pemeriksaan slot."""
        plat_nomor = self.plat_var.get().strip().upper()
        
        if not plat_nomor:
            messagebox.showerror("Input Error", "Nomor Plat tidak boleh kosong.")
            return

        # --- LOGIKA PENGECEKAN SLOT BARU ---
        if len(parking_lot) >= self.max_capacity:
            messagebox.showwarning("PARKIR PENUH", 
                                   f"Maaf, tempat parkir sudah penuh ({self.max_capacity}/{self.max_capacity} slot terisi).")
            return
        # ------------------------------------

        if plat_nomor in parking_lot:
            messagebox.showwarning("Gagal Masuk", f"Kendaraan plat {plat_nomor} sudah terdaftar masuk.")
        else:
            waktu_masuk = datetime.now()
            parking_lot[plat_nomor] = waktu_masuk
            messagebox.showinfo("Berhasil", 
                                f"Kendaraan **{plat_nomor}** berhasil masuk pada {waktu_masuk.strftime('%H:%M:%S')}.")
            self.update_status()
            self.plat_var.set("")
            self.plat_entry.focus_set()

    def park_out_gui(self):
        """Handler untuk tombol Keluar dan perhitungan biaya."""
        plat_nomor = self.plat_var.get().strip().upper()
        
        if not plat_nomor:
            messagebox.showerror("Input Error", "Nomor Plat tidak boleh kosong.")
            return
        
        if plat_nomor not in parking_lot:
            messagebox.showwarning("Gagal Keluar", f"Kendaraan plat {plat_nomor} tidak ditemukan.")
            return

        waktu_masuk = parking_lot.pop(plat_nomor)
        waktu_keluar = datetime.now()
        durasi = waktu_keluar - waktu_masuk
        durasi_detik = durasi.total_seconds()
        
        biaya, jam_tagihan = calculate_fee(durasi_detik)

        # Format output kuitansi
        kuitansi = (f"Plat Nomor: **{plat_nomor}**\n"
                    f"Waktu Masuk: {waktu_masuk.strftime('%H:%M:%S')}\n"
                    f"Waktu Keluar: {waktu_keluar.strftime('%H:%M:%S')}\n"
                    f"Durasi Parkir: {durasi.total_seconds() / 60:.2f} menit\n"
                    f"Jam Tagihan: **{jam_tagihan} jam**\n"
                    f"---------------------------------------\n"
                    f"TOTAL BIAYA: **Rp {biaya:,.0f}**")
                    
        messagebox.showinfo("💸 Kuitansi Parkir", kuitansi)
        self.update_status() # Perbarui status setelah kendaraan keluar
        self.plat_var.set("")
        self.plat_entry.focus_set()

# --- 4. Main Program ---

if __name__ == '__main__':
    root = tk.Tk()
    app = ParkingApp(root)
    root.mainloop()