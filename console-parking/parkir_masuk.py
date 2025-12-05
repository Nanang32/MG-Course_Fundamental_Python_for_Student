from datetime import datetime
from data_manager import load_data, save_data

def parkir_masuk():
    data = load_data()

    plat = input("Masukkan plat kendaraan: ").upper()

    if plat in data and data[plat]["status"] == "parkir":
        print("❗ Kendaraan sudah terparkir!")
        return

    waktu_masuk = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data[plat] = {
        "waktu_masuk": waktu_masuk,
        "status": "parkir"
    }

    save_data(data)
    print(f"✔ Kendaraan {plat} berhasil masuk pada {waktu_masuk}.\n")
