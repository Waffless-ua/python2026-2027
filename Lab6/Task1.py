import os


def process_students_file() -> None:
    line_count = 0
    word_count = 0
    upper_lines: list[str] = []

    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line.rstrip()}")

                line_count += 1
                word_count += len(line.split())
                upper_lines.append(line.upper())
    except FileNotFoundError:
        print('Файл "students.txt" не знайдено')
        return
    except PermissionError:
        print('Немає прав на читання "students.txt"')
        return
    except UnicodeDecodeError:
        print('Не вдалося прочитати "students.txt" у кодуванні UTF-8')
        return

    print("\nКількість рядків:", line_count)
    print("Кількість слів:", word_count)
    print("Розмір файлу в байтах:", os.path.getsize("students.txt"))

    try:
        with open("students_upper.txt", "w", encoding="utf-8") as file:
            file.writelines(upper_lines)
    except PermissionError:
        print('Немає прав на запис "students_upper.txt"')
    else:
        print('Файл "students_upper.txt" успішно записано')


process_students_file()