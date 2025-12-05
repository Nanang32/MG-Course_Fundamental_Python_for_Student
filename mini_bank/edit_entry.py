# edit_entry.py
from storage import load_data, save_data
from view_entries import view_entries

def edit_entry():
    data = load_data()
    view_entries()

    if not data:
        return

    try:
        idx = int(input("Entry number to edit: ")) - 1
        if idx < 0 or idx >= len(data):
            print("❌ Invalid number!")
            return
    except:
        print("❌ Input must be a number!")
        return

    print("\nPress ENTER to skip editing a field")

    new_name = input("New student name: ")
    new_grade = input("New grade: ")
    new_major = input("New major: ")
    new_amount = input("New deposit amount: ")

    if new_name:
        data[idx]["name"] = new_name
    if new_grade:
        data[idx]["grade"] = new_grade
    if new_major:
        data[idx]["major"] = new_major
    if new_amount:
        try:
            data[idx]["amount"] = int(new_amount)
        except:
            print("❌ Amount must be a number!")
            return

    save_data(data)
    print("✔ Entry updated successfully!")
