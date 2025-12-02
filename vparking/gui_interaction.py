from tkinter import messagebox

def handle_park_in(app):
    plat = app.plat_var.get().strip().upper()
    if plat == "":
        return messagebox.showerror("Error", "Plat tidak boleh kosong")

    status, msg = app.logic.park_in(plat)
    if status:
        app.data.save_data()
        app.update_status()
        messagebox.showinfo("Berhasil", msg)
    else:
        messagebox.showwarning("Gagal", msg)


def handle_park_out(app):
    plat = app.plat_var.get().strip().upper()
    if plat == "":
        return messagebox.showerror("Error", "Plat tidak boleh kosong")

    status, result = app.logic.park_out(plat)
    if not status:
        return messagebox.showwarning("Gagal", result)

    app.data.save_data()
    app.update_status()

    msg = (f"Plat: {result['plat']}\n"
           f"Waktu Masuk: {result['masuk']}\n"
           f"Waktu Keluar: {result['keluar']}\n"
           f"Biaya: Rp {result['biaya']:,}")

    messagebox.showinfo("Kuitansi", msg)
