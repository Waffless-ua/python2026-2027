import datetime
from enum import Enum
from typing import Final


class Level(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


FILENAME: Final[str] = 'logTask2.txt'

def log_event(filename: str, level: Level, message: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{level.value}] {message}\n")
    except FileNotFoundError:
        print(f'Файл "{filename}" не знайдено')
        return
    except PermissionError:
        print(f'Немає прав на читання "{filename}"')
        return
    except UnicodeDecodeError:
        print(f'Не вдалося прочитати "{filename}" у кодуванні UTF-8')
        return

    return


log_event(FILENAME, Level.INFO, "Програму запущено")
log_event(FILENAME, Level.INFO, "Налаштування завантажено")
log_event(FILENAME, Level.INFO, "Користувач увійшов у систему")
log_event(FILENAME, Level.WARNING, "Не заповнено необов'язкове поле")
log_event(FILENAME, Level.ERROR, "Не вдалося відкрити файл")
log_event(FILENAME, Level.INFO, "Створено резервну копію")
log_event(FILENAME, Level.WARNING, "Мало вільного місця на диску")
log_event(FILENAME, Level.ERROR, "Помилка збереження даних")
log_event(FILENAME, Level.WARNING, "Перевищено час очікування")
log_event(FILENAME, Level.INFO, "Роботу програми завершено")


def read_log(filename: str, level: Level | None = None) -> list[str]:
    records: list[str] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("] ", maxsplit=2)

                if level is None:
                    records.append(line)
                elif len(parts) == 3 and parts[1] == f"[{level.value}":
                    records.append(line)

    except FileNotFoundError:
        print(f'Файл "{filename}" не знайдено')
    except PermissionError:
        print(f'Немає прав доступу до "{filename}"')
    except UnicodeDecodeError:
        print(f'Файл "{filename}" не вдалося прочитати в кодуванні UTF-8')

    return records

for level in Level:
    records = read_log(FILENAME, level)

    print(f"\n{level.value}: {len(records)} записів")
    for record in records:
        print(record)

print("\nКількість записів кожного рівня:")
for level in Level:
    records = read_log(FILENAME, level)
    print(f"{level.value}: {len(records)}")