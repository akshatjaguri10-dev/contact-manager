from contacts import add_contact, view_contacts, search_contact, delete_contact


def show_menu():
    print("\n===== CONTACT MANAGER =====")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")