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
            print(f"{count}. {name:10} {phone:2} \t {email}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")

