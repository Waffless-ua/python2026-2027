students_math = {
    "Коваленко",
    "Іваненко",
    "Петренко",
    "Коваль",
    "Мельник",
}

students_physics = {
    "Коваленко",
    "Іваненко",
    "Шевченко",
    "Бондар",
    "Мельник",
}

students_cs = {
    "Коваленко",
    "Петренко",
    "Шевченко",
    "Ткаченко",
    "Кравченко",
}

all_three = students_math & students_physics & students_cs
at_least_one = students_math | students_physics | students_cs
math_without_physics = students_math - students_physics

exactly_two = (
    (students_math & students_physics)
    | (students_math & students_cs)
    | (students_physics & students_cs)
) - all_three

print("Відвідують усі три предмети:", sorted(all_three))
print("Відвідують хоча б один предмет:", sorted(at_least_one))
print("Відвідують математику, але не фізику:", sorted(math_without_physics))
print("CS є підмножиною математики:", students_cs.issubset(students_math))
print("Відвідують рівно два предмети:", sorted(exactly_two))

numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = sorted(set(numbers))

print("Список без дублікатів:", unique_numbers)