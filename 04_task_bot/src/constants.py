commands = {
    "add": "add",
    "change": "change",
    "phone": "phone",
    "all": "all",
    "quit": ["quit", "exit", "close"],
    "hello": "hello"
}

message = {
    "welcome": """
Welcome to the assistant bot!

Commands:
- hello: Start the bot
- add: Add a new contact (add [name] [phone])
- change: Update an existing contact (change [name] [new phone])
- phone: Show phone by name (phone [name])
- all: Show all contacts
- quit: Exit the bot (quit, close, or exit)
    """,
    "hello": "How can I assist you?",
    "quit": "Goodbye!",
    "input": "Enter a command: ",
    "add": "Contact added successfully.",
    "change": "Contact updated successfully.",
    "no_contacts": "No contacts available.",
    "invalid": "Invalid command. Please try again."
}
