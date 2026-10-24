import shutil
from datetime import datetime
from pathlib import Path

BACKUP_DIR = Path("backup")

def backup_file(src_path: str) -> Path | None:
    source = Path(src_path)

    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        destination = BACKUP_DIR / f"{source.stem}_{timestamp}{source.suffix}"

        shutil.copy2(source, destination)
    except FileNotFoundError:
        print(f'Файл "{source}" не знайдено')
    except PermissionError:
        print(f'Немає прав для копіювання "{source}"')
    except OSError as error:
        print(f"Помилка копіювання файлу: {error}")
    else:
        print(f"Резервну копію створено: {destination}")
        return destination

    return None


def backup_folder(src_dir: str, dst_dir: str) -> Path | None:
    source = Path(src_dir)
    destination = Path(dst_dir)

    try:
        shutil.copytree(
            source,
            destination,
            ignore=shutil.ignore_patterns("*.tmp", "*.log"),
        )
    except FileNotFoundError:
        print(f'Директорію "{source}" не знайдено')
    except PermissionError:
        print(f'Немає прав для копіювання "{source}"')
    except FileExistsError:
        print(f'Директорія призначення "{destination}" уже існує')
    except shutil.Error as error:
        print(f"Помилки копіювання директорії: {error}")
    except OSError as error:
        print(f"Помилка файлової системи: {error}")
    else:
        print(f"Директорію скопійовано: {destination}")
        return destination

    return None


def restore_latest(filename: str) -> Path | None:
    destination = Path(filename)
    pattern = f"{destination.stem}_*{destination.suffix}"

    try:
        backups = sorted(
            (file for file in BACKUP_DIR.glob(pattern) if file.is_file()),
            key=lambda file: file.name,
            reverse=True,
        )

        if not backups:
            raise FileNotFoundError(f'Резервних копій для "{destination.name}" не знайдено')

        latest = backups[0]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(latest, destination)
    except FileNotFoundError as error:
        print(error)
    except PermissionError:
        print(f'Немає прав для відновлення "{destination}"')
    except OSError as error:
        print(f"Помилка відновлення: {error}")
    else:
        print(f"Відновлено: {latest} → {destination}")
        return destination

    return None


def main() -> None:
    backup_file("students.txt")
    backup_file("students.txt")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    backup_folder("lab6_project",f"backup/lab6_project_{timestamp}")

    restore_latest("students.txt")

    print("\nПеревірка відсутніх джерел:")
    backup_file("missing_file.txt")
    backup_folder("missing_folder", "backup/missing_folder")
    restore_latest("missing_file.txt")


main()