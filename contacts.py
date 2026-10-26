from storage import load_contacts, save_contacts

def add_contact():
    contacts = load_contacts()

    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact added successfully!")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACTS =====")

    for number, contact in enumerate(contacts, start=1):
        print(f"{number}. {contact['name']} - {contact['phone']}")


def search_contact():
    contacts = load_contacts()

    search_name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("\nContact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            return

    print("Contact not found.")


def delete_contact():
    contacts = load_contacts()

    delete_name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            save_contacts(contacts)

            print(f"{delete_name} deleted successfully!")
            return

    print("Contact not found.")