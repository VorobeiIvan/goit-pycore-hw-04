from constants import message

def welcome_message():
    """Print the welcome message."""
    print(message["welcome"])

def start():
    """Start the bot."""
    return message["hello"]

def quit_bot():
    """Quit the bot."""
    print(message["quit"])

def add_contact(args, contacts):
    """Add a new contact."""
    name, phone = args
    contacts[name] = phone
    return message["add"]

def change_contact(args, contacts):
    """Change an existing contact."""
    name, phone = args
    contacts[name] = phone
    return message["change"]

def show_phone(args, contacts):
    """Show the phone number of a specific contact."""
    name = args[0]
    return f"{name}: {contacts[name]}"

def show_all(contacts):
    """Show all saved contacts."""
    if not contacts:
        return message["no_contacts"]
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input):
    """Parse user input and return command and arguments."""
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args
