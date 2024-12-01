
from pathlib import Path
import sys
from utils.styled_messages import current_path_message


def get_current_path():
    """Функція для визначення поточного шляху."""
    return Path(sys.argv[0]).parent

def print_current_path():
    """Функція для виведення поточного шляху з повідомленням."""
    print(current_path_message + str(get_current_path()))
