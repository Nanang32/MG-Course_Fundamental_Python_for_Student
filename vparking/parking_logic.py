from datetime import datetime
from fee_calculation import calculate_fee
from constants import MAX_CAPACITY_DEFAULT

class ParkingLogic:
    def __init__(self, data_manager, max_capacity=MAX_CAPACITY_DEFAULT):
        self.data = data_manager
        self.max_capacity = max_capacity

    def set_capacity(self, new_max):
        self.max_capacity = new_max

    def park_in(self, plat):
        if plat in self.data.parking_lot:
            return False, f"Kendaraan {plat} sudah masuk."

        if len(self.data.parking_lot) >= self.max_capacity:
            return False, "Parkir penuh!"

        self.data.parking_lot[plat] = datetime.now()
        self.data.save()
        return True, f"{plat} berhasil masuk."

    def park_out(self, plat):
        if plat not in self.data.parking_lot:
            return False, "Plat tidak ditemukan."

        waktu_masuk = self.data.parking_lot.pop(plat)
        waktu_keluar = datetime.now()
        durasi = (waktu_keluar - waktu_masuk).total_seconds()

        biaya, jam_tagihan = calculate_fee(durasi)

        self.data.save()

        return True, {
            "plat": plat,
            "masuk": waktu_masuk.strftime("%H:%M:%S"),
            "keluar": waktu_keluar.strftime("%H:%M:%S"),
            "durasi_menit": round(durasi/60, 2),
            "jam_tagihan": jam_tagihan,
            "biaya": biaya
        }
