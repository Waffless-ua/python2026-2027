Student = tuple[str, int, float, frozenset[str]]
Students = dict[str, Student]


def add_student(
    students: Students,
    name: str,
    year: int,
    gpa: float,
    courses: tuple[str, ...],
) -> str:
    next_number = max(
        (int(existing_id.split("-")[1]) for existing_id in students),
        default=0,
    ) + 1

    student_id = f"ST-{next_number:03d}"
    students[student_id] = (name, year, gpa, frozenset(courses))

    return student_id


def find_by_name(
    students: Students,
    name: str,
) -> tuple[str, Student] | None:
    for student_id, data in students.items():
        if data[0].casefold() == name.casefold():
            return student_id, data

    return None


def top_students(
    students: Students,
    n: int = 3,
) -> list[tuple[str, float]]:
    return sorted(
        ((data[0], data[2]) for data in students.values()),
        key=lambda student: student[1],
        reverse=True,
    )[:max(0, n)]


def students_in_course(
    students: Students,
    course_name: str,
) -> set[str]:
    return {
        data[0]
        for data in students.values()
        if course_name in data[3]
    }


def common_courses(
    students: Students,
    id1: str,
    id2: str,
) -> set[str]:
    return set(students[id1][3] & students[id2][3])


def stats(students: Students) -> dict[str, int | float | set[str]]:
    total = len(students)
    avg_gpa = (
        sum(data[2] for data in students.values()) / total
        if total else 0.0
    )
    unique_courses = {
        course
        for data in students.values()
        for course in data[3]
    }

    return {
        "total": total,
        "avg_gpa": avg_gpa,
        "unique_courses": unique_courses,
    }


def main():
    students: Students = {}

    initial_students = (
        ("Максим", 3, 92.5, ("Python", "Бази даних", "Алгоритми")),
        ("Олена", 2, 95.2, ("Python", "Математика")),
        ("Андрій", 1, 84.7, ("Математика", "Фізика")),
        ("Марія", 3, 91.0, ("Алгоритми", "Python", "Бази даних")),
        ("Олег", 2, 78.5, ("Фізика", "Python")),
        ("Ірина", 2, 97.1, ("Математика", "Python")),
    )

    print("Додавання студентів:")
    for name, year, gpa, courses in initial_students:
        student_id = add_student(students, name, year, gpa, courses)
        print(f"{student_id}: {students[student_id]}")

    print("\nПошук студентів:")
    for search_name in ("Максим", "Дмитро"):
        result = find_by_name(students, search_name)

        if result is None:
            print(f"{search_name}: студента не знайдено")
        else:
            found_id, found_data = result
            print(f"{search_name}: {found_id}, {found_data}")

    print("\nНайкращі студенти:", top_students(students))
    print(
        "Студенти на курсі Python:",
        students_in_course(students, "Python"),
    )
    print(
        "Спільні курси ST-001 та ST-002:",
        common_courses(students, "ST-001", "ST-002"),
    )

    print("\nСтатистика:", stats(students))

    course_groups: dict[frozenset[str], set[tuple[str, str]]] = {}

    for student_id, data in students.items():
        course_set = data[3]

        if course_set not in course_groups:
            course_groups[course_set] = set()

        course_groups[course_set].add((student_id, data[0]))

    print("\nСтуденти з однаковим набором курсів:")
    for course_set, group in course_groups.items():
        if len(group) > 1:
            print("Курси:", ", ".join(sorted(course_set)))

            for student_id, name in sorted(group):
                print(f"{student_id}: {name}")



main()