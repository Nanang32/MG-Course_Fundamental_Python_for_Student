import json
from datetime import datetime
from constants import DATA_FILE

class DataManager:
    def __init__(self):
        self.parking_lot = self.load()

    def load(self):
        try:
            with open(DATA_FILE, "r") as f:
            # Ubah ISO string → datetime
                raw = json.load(f)
                return {k: datetime.fromisoformat(v) for k, v in raw.items()}
        except:
            return {}

    def save(self):
        # Convert datetime → string ISO
        data = {k: v.isoformat() for k, v in self.parking_lot.items()}
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
