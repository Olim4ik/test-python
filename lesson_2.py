def main():
    contacts = {"Mark": 123, "John": 456, "Mary": 789, "Nick": 987, "Anna": 654}
    while True:
        command = input("1 - add contact\n2 - delete contact\n3 - show all contacts\n4 - exit\n")
        if command == '1':
            name = input("Enter name: ")
            tel = input("Enter tel: ")
            contacts[name] = tel
        elif command == '2':
            name = input("Enter name: ")
            if (contacts.get(name)):
                contacts.pop(name)
                print(f"Contact {name} deleted")
            else:
                print("Contact {name} not found")
        
        print(contacts)

main()