print("Contact Book Menu:")
print("1. Add contact")
print("2. View all contacts")
print("3. Search contact")
print("4. Exit")

names = []
phones = []
emails = []

while True:
    choice = input("\nChoice : ").strip()
    if choice == "1":
        name = input("Name : ")
        phone = input("Phone : ")
        email = input("Email : ")
        print("Contact Added!")
        names.append(name)
        phones.append(phone)
        emails.append(email)

    elif choice == "2":
        count = 0
        print("Contacts:")
        for name, phone, email in zip(names, phones, emails):
            count += 1
            print(f"{count}. {name:10} {phone:5} \t {email}")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for name, phone, email in zip(names, phones, emails):
            if name == search:
                print(f"Name: {name} \nPhone: {phone} \nEmail: {email}")
                found = True
                break
            elif name != search:
                print("No contacts yest!")
            elif search.lower() or name.lower() != search.lower():
                print("Name not matched!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")

#print("\u2022 Bullet")