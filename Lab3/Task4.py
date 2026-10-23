cubes = {number: number ** 3 for number in range(1, 11)}
print("Куби чисел:", cubes)

products = {
    "яблуко": 35,
    "банан": 22,
    "ківі": 55,
    "слива": 18,
}

cheap_products = {
    name: price
    for name, price in products.items()
    if price < 40
}

print("Товари дешевше 40 грн:", cheap_products)

students = [
    {"name": "Максим", "gpa": 92.5},
    {"name": "Олена", "gpa": 95.2},
    {"name": "Андрій", "gpa": 84.7},
    {"name": "Марія", "gpa": 91.0},
    {"name": "Олег", "gpa": 78.5},
]

student_grades = {
    student["name"]: student["gpa"]
    for student in students
}

print("Середні оцінки студентів:", student_grades)

phone_book = {
    "Максим": {
        "phone": "+380000000001",
        "email": "max@example.com",
        "city": "Житомир",
    },
    "Олена": {
        "phone": "+380000000002",
        "email": "olena@example.com",
        "city": "Київ",
    },
    "Андрій": {
        "phone": "+380000000003",
        "email": "andrii@example.com",
        "city": "Львів",
    },
    "Марія": {
        "phone": "+380000000004",
        "email": "mariia@example.com",
        "city": "Київ",
    },
}

print("Контакти з Києва:")
for name, contact in phone_book.items():
    if contact["city"] == "Київ":
        print(f"{name}: {contact}")

phone_book["Олег"] = {
    "phone": "+380000000005",
    "email": "oleh@example.com",
    "city": "Одеса",
}

print("Новий контакт:", phone_book["Олег"])

missing_email = phone_book.get("Ірина", {}).get("email", "Email не знайдено")
print("Email відсутнього контакту:", missing_email)