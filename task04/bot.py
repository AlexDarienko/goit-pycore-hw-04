
contacts = {}

def add_contact(args):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args):
    if len(args) != 2:
        return "Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all():
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
