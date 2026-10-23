schedule = {
    "Понеділок": [
        ("08:30", "Математика", "201"),
        ("10:10", "Програмування", "305"),
        ("11:50", "Англійська мова", "102"),
    ],
    "Вівторок": [
        ("08:30", "Фізика", "204"),
        ("10:10", "Алгоритми", "305"),
    ],
    "Середа": [
        ("08:30", "Бази даних", "310"),
        ("10:10", "Математика", "201"),
        ("11:50", "Програмування", "305"),
        ("13:30", "Історія", "105"),
    ],
    "Четвер": [
        ("10:10", "Англійська мова", "102"),
        ("11:50", "Фізика", "204"),
    ],
    "П’ятниця": [
        ("08:30", "Алгоритми", "305"),
        ("10:10", "Бази даних", "310"),
    ],
}

classrooms = {
    classroom
    for lessons in schedule.values()
    for time, subject, classroom in lessons
}

print("Унікальні аудиторії:", sorted(classrooms))

print("Заняття в понеділок:")
for time, subject, classroom in schedule["Понеділок"]:
    print(f"{time} — {subject}, аудиторія {classroom}")

busiest_day = max(schedule, key=lambda day: len(schedule[day]))
print(f"Найбільше занять: {busiest_day} — {len(schedule[busiest_day])}")

transactions = [
    ("2026-10-01", "Продукти", 350),
    ("2026-10-01", "Транспорт", 40),
    ("2026-10-02", "Навчання", 500),
    ("2026-10-02", "Розваги", 200),
    ("2026-10-03", "Продукти", 420),
    ("2026-10-03", "Транспорт", 60),
    ("2026-10-04", "Навчання", 250),
    ("2026-10-04", "Розваги", 180),
    ("2026-10-05", "Продукти", 280),
    ("2026-10-05", "Транспорт", 40),
    ("2026-10-06", "Навчання", 300),
    ("2026-10-06", "Розваги", 150),
    ("2026-10-07", "Продукти", 390),
    ("2026-10-07", "Транспорт", 80),
    ("2026-10-08", "Продукти", 210),
]

expenses = {}

for date, category, amount in transactions:
    expenses[category] = expenses.get(category, 0) + amount

print("\nВитрати за категоріями:")
for category, amount in expenses.items():
    print(f"{category}: {amount:.2f} грн")

unique_dates = {date for date, category, amount in transactions}
print("Унікальні дати:", sorted(unique_dates))

largest_category = max(expenses, key=lambda category_name: expenses[category_name])

print(
    f"Найбільші витрати: {largest_category} — "
    f"{expenses[largest_category]:.2f} грн"
)