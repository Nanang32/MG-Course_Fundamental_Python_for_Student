from datetime import datetime
from data_manager import load_data, save_data

def parkir_keluar():
    data = load_data()

    plat = input("Masukkan plat kendaraan keluar: ").upper()

    if plat not in data:
        print("❗ Kendaraan tidak ditemukan!")
        return

    if data[plat]["status"] != "parkir":
        print("❗ Kendaraan sudah keluar sebelumnya!")
        return

    waktu_masuk = datetime.strptime(data[plat]["waktu_masuk"], "%Y-%m-%d %H:%M:%S")
    waktu_keluar = datetime.now()
    durasi = (waktu_keluar - waktu_masuk).total_seconds() / 3600
    durasi_jam = round(durasi, 2)

    # tarif
    tarif_per_jam = 3000
    biaya = int(durasi_jam * tarif_per_jam)

    data[plat]["status"] = "keluar"
    data[plat]["waktu_keluar"] = waktu_keluar.strftime("%Y-%m-%d %H:%M:%S")
    data[plat]["durasi_jam"] = durasi_jam
    data[plat]["biaya"] = biaya

    save_data(data)

    print("\n==== STRUK PARKIR ====")
    print(f"Plat Kendaraan : {plat}")
    print(f"Masuk          : {data[plat]['waktu_masuk']}")
    print(f"Keluar         : {data[plat]['waktu_keluar']}")
    print(f"Durasi         : {durasi_jam} jam")
    print(f"Biaya          : Rp {biaya:,}")
    print("======================\n")
