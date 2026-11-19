from pathlib import Path
from datetime import datetime


def print_tree(directory: Path, depth: int = 0) -> None:
    suffix = "/" if directory.is_dir() else ""
    print(f"{'    ' * depth}{directory.name}{suffix}")

    if directory.is_dir():
        for item in sorted(directory.iterdir(), key=lambda path: path.name):
            print_tree(item, depth + 1)


def main() -> None:
    project_dir = Path("lab6_project")

    for folder in ("src", "data", "output"):
        (project_dir / folder).mkdir(parents=True, exist_ok=True)

    print("Структура директорій:")
    print_tree(project_dir)

    data_dir = Path("lab6_data")

    if not data_dir.is_dir():
        print('\nДиректорію "lab6_data" не знайдено')
        return

    print("\nІнформація про файли:")

    for file in sorted(data_dir.iterdir(), key=lambda path: path.name):
        if file.is_file():
            file_stat = file.stat()
            modified = datetime.fromtimestamp(file_stat.st_mtime)

            print(f"\nІм’я: {file.name}")
            print(f"Розширення: {file.suffix or 'відсутнє'}")
            print(f"Розмір: {file_stat.st_size} байтів")
            print(f"Остання зміна: {modified:%d.%m.%Y %H:%M:%S}")

    print("\nТекстові файли (*.txt):")

    for file in sorted(data_dir.glob("*.txt")):
        if file.is_file():
            print(file.name)


main()