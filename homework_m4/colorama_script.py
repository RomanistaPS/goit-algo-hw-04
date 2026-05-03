import sys
from pathlib import Path
from colorama import Fore


def print_directory_structure(path: Path, indent: str = ""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}")
            print_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: потрібно передати шлях до директорії.")
        print("Приклад:")
        print("python homework_m4/colorama_script.py D:/goit-algo-hw-04/homework_m4")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: такого шляху не існує.")
        return

    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: вказаний шлях не є директорією.")
        return

    print(f"Структура директорії: {directory_path}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()