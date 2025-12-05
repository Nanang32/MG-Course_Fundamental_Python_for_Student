from data_manager import load_data

def lihat_daftar():
    data = load_data()

    print("\n=== DAFTAR KENDARAAN PARKIR ===")
    kosong = True
    for plat, info in data.items():
        if info["status"] == "parkir":
            print(f"- {plat} | Masuk: {info['waktu_masuk']}")
            kosong = False

    if kosong:
        print("Tidak ada kendaraan yang sedang parkir.\n")
