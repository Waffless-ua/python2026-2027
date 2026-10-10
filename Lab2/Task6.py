text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
)


words = [word.lower().strip(".,!?;:") for word in text.split()]
words = [word for word in words if word]


print(f"Кількість символів з пробілами: {len(text)}")
print(f"Кількість символів без пробілів: {len(''.join(text.split()))}")
print(f"Кількість слів: {len(words)}")
print(f"Кількість речень: {sum(text.count(char) for char in '.!?')}")
print(f"Кількість унікальних слів: {len(set(words))}")


word_frequency = [(word, words.count(word)) for word in set(words)]
top_5 = sorted(word_frequency, key=lambda item: item[1], reverse=True)[:5]


print(f"Топ-5 слів: {top_5}")

if words:
    print(f"Найдовше слово: {max(words, key=len)}")
    print(f"Найчастіше слово: {top_5[0][0]}")
else:
    print("Слів не знайдено")

palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
print(f"Кількість паліндромів: {len(palindromes)}")

summary = text[:80] + ("..." if len(text) > 80 else "")
print(f"Резюме: {summary}")

print("\nВведіть студентів у форматі Прізвище:оцінка")
print("Порожній рядок для завершення")

students = []

while True:
    line = input()
    if not line:
        break

    surname, grade = line.split(":")
    students.append((surname.strip(), float(grade)))

rating = sorted(students, key=lambda student: student[1], reverse=True)

print("\nРейтинг студентів:")
for student in rating:
    print(f"{student[0]}: {student[1]}")

if students:
    average = sum([student[1] for student in students]) / len(students)

    above = [student for student in students if student[1] > average]
    below = [student for student in students if student[1] < average]

    print(f"Середній бал: {average:.2f}")
    print(f"Студентів вище середнього: {len(above)}")
    print(f"Студентів нижче середнього: {len(below)}")

    report = "\n".join([
        "\nФінальний звіт:",
        f"Кількість студентів: {len(students)}",
        f"Середній бал: {average:.2f}",
        f"Вище середнього: {len(above)}",
        f"Нижче середнього: {len(below)}",
        "Рейтинг: " + ", ".join([f"{student[0]} ({student[1]})" for student in rating])
    ])

    print(report)
else:
    print("Список студентів порожній")
