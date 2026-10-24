import logging

logging.basicConfig(
    filename="errorsTask2.log",
    encoding="utf-8",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def read_numbers_from_file(filename: str) -> list[int | float]:
    numbers: list[int | float] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                try:
                    number = float(line)
                except ValueError as e:
                    err = f"Рядок {line_number}: {e}"
                    print(err)
                    logging.error(err, exc_info=True)
                else:
                    numbers.append(
                        int(number) if number.is_integer() else number
                    )

    except FileNotFoundError:
        err = f'Файл "{filename}" не знайдено'
        print(err)
        logging.error(err, exc_info=True)
        return []
    except PermissionError:
        err = f'Немає прав доступу до "{filename}"'
        print(err)
        logging.error(err, exc_info=True)
        return []
    except UnicodeDecodeError:
        err = f'Файл "{filename}" не вдалося прочитати в кодуванні UTF-8'
        print(err)
        logging.error(err, exc_info=True)
        return []
    else:
        print(f"Файл прочитано успішно: {len(numbers)} чисел")
    finally:
        print("Файл закрито")

    return numbers


print("Прочитані числа:", read_numbers_from_file("numbers.txt"), end="\n\n")
print("Прочитані числа:", read_numbers_from_file("missing_numbers.txt"))