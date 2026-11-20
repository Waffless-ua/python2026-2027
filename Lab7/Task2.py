class Student:
    """Represents a student with validated data and a private ID."""

    _registry: dict[str, "Student"] = {}
    _next_id: int = 1

    def __init__(self, name: str, year: int) -> None:
        if not self.validate_name(name):
            raise ValueError("Name must be a valid student name")

        self.name: str = name
        self.year = year
        self.gpa = 0
        self._courses: list[str] = []

        self.__student_id = f"STU-{Student._next_id:03d}"
        Student._next_id += 1
        Student._registry[self.__student_id] = self

    @property
    def student_id(self) -> str:
        """Student ID. Read-only."""
        return self.__student_id

    @property
    def year(self) -> int:
        """Year of study, from 1 to 6."""
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if not isinstance(value, int) or not 1 <= value <= 6:
            raise ValueError("Year must be a number from 1 and 6")
        self._year = value

    @property
    def gpa(self) -> int | float:
        """Grade point average, from 0 to 5."""
        return self._gpa

    @gpa.setter
    def gpa(self, value: int | float) -> None:
        if not 0 <= value <= 5:
            raise ValueError("GPA must be a number from 0 to 5")
        self._gpa = value

    @property
    def courses(self) -> list[str]:
        """Returns a copy of the student's course list."""
        return self._courses.copy()

    def add_course(self, name: str) -> None:
        if name in self._courses:
            raise ValueError(f"Course '{name}' already added")
        self._courses.append(name)

    def remove_course(self, name: str) -> None:
        if name not in self._courses:
            raise ValueError(f"Course '{name}' not found")
        self._courses.remove(name)

    def get_transcript(self) -> str:
        courses_text = ", ".join(self._courses) or "None"

        return (
            f"Студент: {self.name}\n"
            f"ID: {self.student_id}\n"
            f"Рік навчання: {self.year}\n"
            f"Середній бал: {self.gpa:.2f}\n"
            f"Курси: {courses_text}"
        )

    def __str__(self) -> str:
        return self.get_transcript()

    @classmethod
    def get_count(cls) -> int:
        return len(cls._registry)

    @classmethod
    def find_by_id(cls, student_id: str) -> "Student | None":
        return cls._registry.get(student_id)

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and name.isalpha()


def main() -> None:
    first = Student("Максим", 3)
    second = Student("Олена", 2)

    first.gpa = 4.5
    second.gpa = 4.8

    first.add_course("Python")
    first.add_course("Бази даних")
    first.remove_course("Бази даних")

    print(first.get_transcript())
    print()
    print(second.get_transcript())

    print("\nКількість студентів:", Student.get_count())

    found = Student.find_by_id(first.student_id)
    print("Пошук за ID:", found.name if found is not None else "Не знайдено")
    print("Пошук відсутнього ID:", Student.find_by_id("STU-999"))

    print("\nПеревірка імені 'Максим':", Student.validate_name("Максим"))
    print("Перевірка імені 'Максим123':", Student.validate_name("Максим123"))

    try:
        first.__student_id
    except AttributeError as error:
        print("\nПрямий доступ до private:", error)

    print("Доступ через property:", first.student_id)

    try:
        first.year = 7
    except ValueError as error:
        print("\nНекоректний рік:", error)

    try:
        first.gpa = 6
    except ValueError as error:
        print("Некоректний середній бал:", error)


if __name__ == "__main__":
    main()