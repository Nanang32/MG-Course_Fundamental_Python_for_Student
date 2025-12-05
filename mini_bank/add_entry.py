# add_entry.py
from storage import load_data, save_data

def add_entry():
    data = load_data()

    name = input("Student name: ")
    grade = input("Grade (example: XI): ")
    major = input("Major (example: IPA/IPS/RPL): ")

    try:
        amount = int(input("Deposit amount (Rp): "))
        if amount <= 0:
            print("❌ Amount cannot be zero or negative!")
            return
    except:
        print("❌ Amount must be a number!")
        return

    data.append({
        "name": name,
        "grade": grade,
        "major": major,
        "amount": amount
    })

    save_data(data)
    print("✔ Deposit added successfully!")
