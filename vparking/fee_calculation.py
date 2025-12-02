import math
from constants import TARIF_MINIMUM, TARIF_PER_JAM, SATU_JAM_DETIK

def calculate_fee(duration_seconds):
    hours = duration_seconds / SATU_JAM_DETIK

    if hours <= 1:
        return TARIF_MINIMUM, 1

    jam_tagihan = math.ceil(hours)
    biaya = TARIF_MINIMUM + ((jam_tagihan - 1) * TARIF_PER_JAM)

    return biaya, jam_tagihan
