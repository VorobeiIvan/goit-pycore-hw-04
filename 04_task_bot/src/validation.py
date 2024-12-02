def validate_input(command, args, contacts):
    """Validate command and arguments."""
    if command not in commands.values() and command not in commands["quit"]:
        return False, "Unknown command. Please try again."

    if command == commands["add"] or command == commands["change"]:
        if len(args) != 2:
            return False, "Invalid format. Use: [command] [name] [phone]"
        if not args[1].isdigit():
            return False, "Phone number must contain only digits."
    
    if command == commands["phone"] or command == commands["delete"]:
        if len(args) != 1:
            return False, "Invalid format. Use: [command] [name]"
        if args[0] not in contacts:
            return False, f"Contact '{args[0]}' not found."
    
    return True, None
