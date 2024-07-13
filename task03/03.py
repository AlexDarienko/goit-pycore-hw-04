import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(path, indent=''):
    try:
        # Отримання списку всіх файлів і директорій у поточній директорії
        items = list(path.iterdir())
        for item in items:
            if item.is_dir():
                # Друк імені директорії синім кольором
                print(f"{indent}{Fore.BLUE}{item.name}")
                # Рекурсивний виклик для піддиректорій
                print_directory_structure(item, indent + '  ')
            else:
                # Друк імені файлу зеленим кольором
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Permission Denied: {path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python 03.py test_dir")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: Path '{path}' does not exist.")
        sys.exit(1)

    if not path.is_dir():
        print(f"Error: Path '{path}' is not a directory.")
        sys.exit(1)

    print_directory_structure(path)

if __name__ == "__main__":
    main()

# Example usage:
# python 03.py test_dir
