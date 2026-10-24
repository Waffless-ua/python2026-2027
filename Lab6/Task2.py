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


log_event(FILENAME, Level.INFO, "idk")
log_event(FILENAME, Level.WARNING, "idk")
log_event(FILENAME, Level.ERROR, "idk")


def read_log(filename: str, level: Level | None = None) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            if level is None:
                print(file.read())
                return

            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if level.value in line:
                    print(line)

    except FileNotFoundError:
        print(f'Файл "{filename}" не знайдено')
        return
    except PermissionError:
        print(f'Немає прав на читання "{filename}"')
        return
    except UnicodeDecodeError:
        print(f'Не вдалося прочитати "{filename}" у кодуванні UTF-8')
        return

read_log(FILENAME, Level.INFO)
read_log(FILENAME, Level.WARNING)
read_log(FILENAME, Level.ERROR)

read_log(FILENAME)