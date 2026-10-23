from functools import reduce, wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - started
        print(f"\nЧас виконання: {elapsed:.6f} с")
        return result

    return wrapper


def average(grades: list[int]) -> float:
    if not grades:
        raise ValueError("Список оцінок не може бути порожнім")

    return round(
        reduce(lambda total, grade: total + grade, grades, 0) / len(grades),
        2,
    )


def classify(avg: float) -> str:
    if avg >= 90:
        return "відмінник"
    if avg >= 75:
        return "хорошист"
    if avg >= 60:
        return "задовільно"
    return "незараховано"


def get_top(students: list[dict], n: int = 3) -> list[dict]:
    return sorted(
        students,
        key=lambda student: average(student["grades"]),
        reverse=True,
    )[:max(0, n)]


def make_year_filter(year: int):
    return lambda student: student["year"] == year


def group_by_year(students: list[dict]) -> dict[int, list[dict]]:
    years = sorted(set(map(lambda student: student["year"], students)))

    return dict(map(
        lambda year: (
            year,
            list(filter(make_year_filter(year), students)),
        ),
        years,
    ))


def describe_student(student: dict) -> str:
    avg = average(student["grades"])
    grades_text = ", ".join(map(str, student["grades"]))

    return (
        f"{student['name']} — курс {student['year']}, "
        f"оцінки: {grades_text}; "
        f"середня: {avg:.2f}; {classify(avg)}"
    )


@timer
def report(students: list[dict]) -> None:
    print("ЗАГАЛЬНЕ ЗВЕДЕННЯ")
    print("Кількість студентів:", len(students))

    if not students:
        print("Немає даних для аналізу.")
        return

    averages = list(map(
        lambda student: average(student["grades"]),
        students,
    ))

    overall_average = reduce(
        lambda total, avg: total + avg,
        averages,
        0,
    ) / len(averages)

    print(f"Середнє значення середніх оцінок: {overall_average:.2f}")
    print(f"Найвища середня оцінка: {max(averages):.2f}")
    print(f"Найнижча середня оцінка: {min(averages):.2f}")

    print("\nУСІ СТУДЕНТИ")
    print("\n".join(map(describe_student, students)))

    print("\nТОП-3")
    print("\n".join(map(describe_student, get_top(students))))

    print("\nРОЗБИВКА ПО РОКАХ НАВЧАННЯ")
    groups = group_by_year(students)

    print("\n\n".join(map(
        lambda item: (
            f"Курс {item[0]} — студентів: {len(item[1])}\n"
            + "\n".join(map(describe_student, item[1]))
        ),
        groups.items(),
    )))

    print("\nРОЗПОДІЛ ЗА КАТЕГОРІЯМИ")
    categories = (
        "відмінник",
        "хорошист",
        "задовільно",
        "незараховано",
    )

    category_counts = dict(map(
        lambda category: (
            category,
            len(list(filter(
                lambda avg: classify(avg) == category,
                averages,
            ))),
        ),
        categories,
    ))

    print("\n".join(map(
        lambda item: (
            f"{item[0]}: {item[1]} "
            f"({item[1] / len(students) * 100:.2f}%)"
        ),
        category_counts.items(),
    )))


def main():
    students = [
        {"name": "Максим", "grades": [95, 92, 91], "year": 3},
        {"name": "Олена", "grades": [100, 96, 98], "year": 2},
        {"name": "Андрій", "grades": [80, 75, 85], "year": 1},
        {"name": "Марія", "grades": [90, 93, 96], "year": 3},
        {"name": "Олег", "grades": [60, 65, 70], "year": 2},
        {"name": "Ірина", "grades": [75, 78, 81], "year": 4},
        {"name": "Богдан", "grades": [40, 55, 52], "year": 1},
        {"name": "Софія", "grades": [58, 60, 62], "year": 4},
    ]

    report(students)

main()