import sys
from pathlib import Path
from utils.styled_messages import prompt, exit_message, error_choice
from utils.current_path import print_current_path
from utils.directory_functions import print_directory_structure

def main():
    while True:
        print(prompt)
        input_console = input()
        
        if input_console == "1":
            # Визначення поточного шляху
            print_current_path()
            current_path = Path(sys.argv[0]).parent
        
        elif input_console == "2":
            # Виведення вмісту вказаного шляху
            user_path = input("Введіть шлях до директорії: ")
            path = Path(user_path)
            print_directory_structure(path)
        
        elif input_console == "0":
            # Вихід з програми
            print(exit_message)
            break
        
        else:
            print(error_choice)

if __name__ == '__main__':
    main()
