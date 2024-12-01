from pathlib import Path
from utils.styled_messages import dir_style, file_style, error_path_not_exist

def print_directory_structure(path: Path, level=0, is_last=False):
    """Функція для виведення вмісту директорії у вигляді дерева."""
    indent = "│   " * level  
    if level > 0:
        if is_last:
            branch = "└── "
        else:
            branch = "├── "
        print(f"{indent}{branch}{dir_style}{path.name}/") 
    else:
        print(f"{dir_style}{path.name}/") 

    if path.exists() and path.is_dir():
        children = list(path.iterdir())
        for index, element in enumerate(children):
            is_last_child = index == len(children) - 1 
            if element.is_dir():
                print_directory_structure(element, level + 1, is_last=is_last_child) 
            else:
                if is_last_child:
                    branch = "└── "
                else:
                    branch = "├── "
                print(f"{indent}│   {branch}{file_style}{element.name}")
    else:
        print(error_path_not_exist)
