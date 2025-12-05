# main.py
from add_entry import add_entry
from view_entries import view_entries
from edit_entry import edit_entry
from delete_entry import delete_entry
from total_cash import total_cash

def main():
    while True:
        print("\n===== CLASS CASH APPLICATION =====")
        print("1. Add Deposit")
        print("2. View All Deposits")
        print("3. Edit Deposit")
        print("4. Delete Deposit")
        print("5. Total Class Cash")
        print("6. Exit")

        choice = input("Choose menu: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            total_cash()
        elif choice == "6":
            print("Thank you! Program closed.")
            break
        else:
            print("❌ Invalid menu!")

if __name__ == "__main__":
    main()
