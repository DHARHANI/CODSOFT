contacts = []  # Stores all contacts

def add_contact():
    print("\n➕ Add New Contact")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    print("\n📋 Contact List")
    if not contacts:
        print("No contacts found. Add some first!")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - 📞 {contact['phone']}")

def search_contact():
    print("\n🔍 Search Contact")
    query = input("Enter name or phone number: ").lower()
    results = [
        contact for contact in contacts
        if query in contact["name"].lower() or query in contact["phone"]
    ]
    if not results:
        print("❌ No matching contacts found.")
    else:
        for contact in results:
            print(f"📛 Name: {contact['name']}")
            print(f"📞 Phone: {contact['phone']}")
            print(f"📧 Email: {contact['email']}")
            print(f"🏠 Address: {contact['address']}\n")

def update_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        choice = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= choice < len(contacts):
            contact = contacts[choice]
            print(f"\n✏️ Updating {contact['name']}")
            contact["name"] = input(f"Name ({contact['name']}): ") or contact["name"]
            contact["phone"] = input(f"Phone ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"Email ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"Address ({contact['address']}): ") or contact["address"]
            print("✅ Contact updated successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        choice = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= choice < len(contacts):
            deleted_name = contacts.pop(choice)["name"]
            print(f"❌ Contact '{deleted_name}' deleted successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    while True:
        print("\n📞 Contact Management System")
        print("1. ➕ Add Contact")
        print("2. 👀 View Contacts")
        print("3. 🔍 Search Contact")
        print("4. ✏️ Update Contact")
        print("5. ❌ Delete Contact")
        print("6. 🚪 Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
