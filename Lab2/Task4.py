students = [
    ("Шевченко", 4.8),
    ("Коваленко", 4.2),
    ("Бондаренко", 3.7),
    ("Мельник", 5.0),
    ("Ткаченко", 3.2),
    ("Кравченко", 4.5),
    ("Олійник", 3.9),
    ("Савченко", 4.7)
]

print("За середнім балом:", sorted(students, key=lambda student: student[1], reverse=True))

print("За прізвищем:", sorted(students, key=lambda student: student[0]))

print("Максимальний бал:", max(students, key=lambda student: student[1]))
print("Мінімальний бал:", min(students, key=lambda student: student[1]))

print("Студенти з балом >= 4.0:", [student for student in students if student[1] >= 4.0])

average = sum([student[1] for student in students]) / len(students)
print(f"Середній бал групи: {average:.2f}")

surnames = [student[0] for student in students]
print("Прізвища:", ", ".join(surnames))