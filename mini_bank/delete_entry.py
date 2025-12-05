# delete_entry.py
from storage import load_data, save_data
from view_entries import view_entries

def delete_entry():
    data = load_data()
    view_entries()

    if not data:
        return

    try:
        idx = int(input("Entry number to delete: ")) - 1
        if idx < 0 or idx >= len(data):
            print("❌ Invalid number!")
            return
    except:
        print("❌ Input must be a number!")
        return

    confirm = input("Are you sure you want to delete this entry? (y/n): ")
    if confirm.lower() == "y":
        del data[idx]
        save_data(data)
        print("✔ Entry deleted successfully!")
    else:
        print("❌ Cancelled.")
