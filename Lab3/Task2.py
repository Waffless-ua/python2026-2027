grades = {
    "Математика": 92,
    "Фізика": 85,
    "Програмування": 98,
    "Англійська мова": 90,
    "Історія": 78,
    "Алгоритми": 95,
}

print("Предмети:", list(grades.keys()))
print("Оцінки:", list(grades.values()))

for subject, grade in grades.items():
    print(f"{subject}: {grade}")



best_subject = max(grades, key=lambda subject_name: grades[subject_name])
print(f"Найвища оцінка: {best_subject} — {grades[best_subject]}")

average = sum(grades.values()) / len(grades)
print(f"Середня оцінка: {average:.2f}")

grades["Бази даних"] = 94
grades["Фізика"] = 89
removed_grade = grades.pop("Історія")

print("Видалена оцінка з історії:", removed_grade)
print("Оновлений словник:", grades)

sorted_grades = dict(
    sorted(grades.items(), key=lambda item: item[1], reverse=True)
)

print("Предмети за спаданням оцінок:")
for subject, grade in sorted_grades.items():
    print(f"{subject}: {grade}")
