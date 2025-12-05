import json
import os

DATA_FILE = "data_tabungan.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_record(nama, kelas, jumlah):
    data = load_data()
    data.append({"nama": nama, "kelas": kelas, "jumlah": jumlah})
    save_data(data)

def delete_record(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)

def update_record(index, nama, kelas, jumlah):
    data = load_data()
    if 0 <= index < len(data):
        data[index] = {"nama": nama, "kelas": kelas, "jumlah": jumlah}
        save_data(data)
