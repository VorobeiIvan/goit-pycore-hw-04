from colorama import Fore, Style
from pathlib import Path

# Повідомлення для вводу
prompt = (
    Fore.GREEN + Style.BRIGHT +
    'Виберіть опцію:\n' +
    '1.' + Fore.BLUE + Style.BRIGHT + ' Визначити поточний шлях та вивести вміст директорії\n' + 
    Fore.GREEN +
    '2.' + Fore.BLUE + Style.BRIGHT + ' Вивести вміст вказаного шляху\n' + 
    Fore.GREEN +
    '0.' + Fore.BLUE + Style.BRIGHT + ' Вийти\n' + 
    Fore.GREEN + 
    '>>> '
)

# Повідомлення для поточного шляху
current_path_message = Fore.YELLOW + Style.BRIGHT + "Поточний шлях: "

# Стилі для директорій та файлів
dir_style = Fore.BLUE + Style.BRIGHT
file_style = Fore.GREEN + Style.BRIGHT

# Повідомлення про помилки
error_choice = Fore.RED + Style.BRIGHT + "Невірний вибір, будь ласка, спробуйте ще раз."
error_path_not_exist = Fore.RED + Style.BRIGHT + f"Шлях '{Path.cwd()}' не існує або не є директорією."

# Повідомлення при виході
exit_message = Fore.YELLOW + Style.BRIGHT + "Good bye!"

