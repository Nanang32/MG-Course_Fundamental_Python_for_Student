# total_cash.py
from storage import load_data

def total_cash():
    data = load_data()
    total = sum(d["amount"] for d in data)
    print(f"\nTotal class cash: Rp {total}\n")
