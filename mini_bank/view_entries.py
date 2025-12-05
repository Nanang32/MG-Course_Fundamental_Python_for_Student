# view_entries.py
from storage import load_data

def view_entries():
    data = load_data()
    if not data:
        print("No cash data available.")
        return

    print("\n=== CLASS CASH RECORDS ===")
    for i, d in enumerate(data):
        print(f"{i+1}. {d['name']} | Grade: {d['grade']} {d['major']} | Rp {d['amount']}")
    print()
