from abc import ABC, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Grade:
    """Stores a subject, a numeric grade, and an assessment date."""

    subject: str
    value: float
    date: date = field(default_factory=date.today)

    def __post_init__(self) -> None:
        """Validates the subject and the grade range."""
        if not self.subject.strip():
            raise ValueError("Subject cannot be empty")
        if not 0 <= self.value <= 5:
            raise ValueError("Grade must be between 0 and 5")


class Person(ABC):
    """Defines a person with a unique ID and a shared registry."""

    __slots__ = ("name", "email", "__id")

    _next_id: int = 1
    _registry: list["Person"] = []

    def __init__(self, *, name: str, email: str) -> None:
        """Initializes personal information and registers the instance."""
        super().__init__()

        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not email.strip():
            raise ValueError("Email cannot be empty")

        self.name = name
        self.email = email
        self.__id = f"PER-{Person._next_id:03d}"

        Person._next_id += 1
        Person._registry.append(self)

    @property
    def id(self) -> str:
        """Returns the read-only personal ID."""
        return self.__id

    @classmethod
    def get_registry(cls) -> list["Person"]:
        """Returns a copy of the shared person registry."""
        return Person._registry.copy()

    @abstractmethod
    def role(self) -> str:
        """Returns the person's role."""
        raise NotImplementedError

    @abstractmethod
    def contact_info(self) -> str:
        """Returns formatted contact information."""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Compares persons by their unique IDs."""
        if not isinstance(other, Person):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        """Returns a hash based on the personal ID."""
        return hash(self.id)

    def __repr__(self) -> str:
        """Returns a technical representation of the person."""
        return (
            f"{type(self).__name__}("
            f"id={self.id!r}, name={self.name!r}, email={self.email!r})"
        )


class Student(Person):
    """Represents a student with grades grouped by subject."""

    def __init__(
        self,
        *,
        year: int,
        major: str,
        **kwargs,
    ) -> None:
        """Initializes student attributes and forwards remaining arguments."""
        if not 1 <= year <= 6:
            raise ValueError("Year must be between 1 and 6")
        if not major.strip():
            raise ValueError("Major cannot be empty")

        self.year = year
        self.major = major
        self._grades: dict[str, list[Grade]] = []

        self._grades = {}
        super().__init__(**kwargs)

    def role(self) -> str:
        """Returns the student role."""
        return "Student"

    def contact_info(self) -> str:
        """Returns the student's name and email."""
        return f"{self.name} <{self.email}>"

    def add_grade(self, subject: str, grade: float) -> None:
        """Adds a validated grade with the current date."""
        record = Grade(subject, grade)
        self._grades.setdefault(subject, []).append(record)

    @property
    def gpa(self) -> float:
        """Returns the average of all grades or zero when no grades exist."""
        values = [
            grade.value
            for grades in self._grades.values()
            for grade in grades
        ]
        return sum(values) / len(values) if values else 0.0

    @property
    def academic_status(self) -> str:
        """Returns an academic category based on the GPA."""
        if not self._grades:
            return "немає оцінок"
        if self.gpa >= 4.5:
            return "відмінник"
        if self.gpa >= 3.5:
            return "хорошист"
        if self.gpa >= 3:
            return "задовільно"
        return "незараховано"

    def transcript(self) -> str:
        """Returns a formatted transcript with dated grades."""
        lines = [
            f"Student: {self.name} ({self.id})",
            f"Year: {self.year}; major: {self.major}",
        ]

        for subject, grades in self._grades.items():
            entries = ", ".join(
                f"{grade.value:g} ({grade.date.isoformat()})"
                for grade in grades
            )
            lines.append(f"{subject}: {entries}")

        lines.append(
            f"GPA: {self.gpa:.2f}; status: {self.academic_status}"
        )
        return "\n".join(lines)


class Teacher(Person):
    """Represents a teacher with a salary and assigned courses."""

    def __init__(
        self,
        *,
        department: str,
        salary: float,
        **kwargs,
    ) -> None:
        """Initializes teacher attributes and forwards remaining arguments."""
        if not department.strip():
            raise ValueError("Department cannot be empty")

        self.department = department
        self.salary = salary
        self.courses: list[str] = []

        super().__init__(**kwargs)

    def role(self) -> str:
        """Returns the teacher role."""
        return "Teacher"

    def contact_info(self) -> str:
        """Returns contact information and the department name."""
        return (
            f"{self.name} <{self.email}>; "
            f"department: {self.department}"
        )

    @property
    def salary(self) -> float:
        """Returns the monthly salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Sets a non-negative monthly salary."""
        if not value >= 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def annual_salary(self) -> float:
        """Returns the salary for twelve months."""
        return self.salary * 12

    def assign_course(self, name: str) -> None:
        """Assigns a non-empty course without duplicates."""
        if not name.strip():
            raise ValueError("Course name cannot be empty")
        if name in self.courses:
            raise ValueError("Course is already assigned")
        self.courses.append(name)

    def remove_course(self, name: str) -> None:
        """Removes a previously assigned course."""
        if name not in self.courses:
            raise ValueError("Course is not assigned")
        self.courses.remove(name)


class GradStudent(Student, Teacher):
    """Represents a graduate student who also works as a teacher."""

    def __init__(
        self,
        *,
        thesis_topic: str,
        supervisor: Teacher,
        **kwargs,
    ) -> None:
        """Initializes research data through cooperative inheritance."""
        if not thesis_topic.strip():
            raise ValueError("Thesis topic cannot be empty")

        self.thesis_topic = thesis_topic
        self.supervisor = supervisor

        super().__init__(**kwargs)

    def role(self) -> str:
        """Returns the combined graduate student and teacher role."""
        return "Graduate student / Teacher"

    def contact_info(self) -> str:
        """Extends inherited contact information with supervisor details."""
        return (
            f"{super().contact_info()}; "
            f"department: {self.department}; "
            f"supervisor: {self.supervisor.name}"
        )


class Department:
    """Stores department members and calculates department statistics."""

    def __init__(self, name: str, head: Teacher) -> None:
        """Initializes a department with its head as the first member."""
        if not name.strip():
            raise ValueError("Department name cannot be empty")

        self.name = name
        self.head = head
        self.members: list[Person] = [head]
        head.department = name

    def add_member(self, person: Person) -> None:
        """Adds a person who is not already a member."""
        if person in self.members:
            raise ValueError("Person is already a department member")
        self.members.append(person)

    def remove_member(self, person: Person) -> None:
        """Removes a member other than the current department head."""
        if person == self.head:
            raise ValueError("Cannot remove the current department head")
        if person not in self.members:
            raise ValueError("Person is not a department member")
        self.members.remove(person)

    def average_student_gpa(self) -> float:
        """Returns the mean GPA of student members."""
        students = [
            person for person in self.members
            if isinstance(person, Student)
        ]
        if not students:
            return 0.0
        return sum(student.gpa for student in students) / len(students)

    def teacher_count(self) -> int:
        """Counts teachers, including graduate students."""
        return sum(
            isinstance(person, Teacher)
            for person in self.members
        )

    def student_count(self) -> int:
        """Counts students, including graduate students."""
        return sum(
            isinstance(person, Student)
            for person in self.members
        )

    def __iter__(self) -> Iterator[Person]:
        """Returns an iterator over department members."""
        return iter(self.members)

    def report(self) -> str:
        """Returns department statistics and detailed member information."""
        lines = [
            f"DEPARTMENT: {self.name}",
            f"Head: {self.head.name}",
            f"Members: {len(self.members)}",
            f"Students: {self.student_count()}",
            f"Teachers: {self.teacher_count()}",
            f"Average student GPA: {self.average_student_gpa():.2f}",
        ]

        for person in self:
            lines.append(
                f"\n[{person.role()}] {person.contact_info()}"
            )

            if isinstance(person, Student):
                lines.append(person.transcript())

            if isinstance(person, Teacher):
                courses = ", ".join(person.courses) or "None"
                lines.append(
                    f"Courses: {courses}\n"
                    f"Monthly salary: {person.salary:.2f}\n"
                    f"Annual salary: {person.annual_salary:.2f}"
                )

            if isinstance(person, GradStudent):
                lines.append(f"Thesis: {person.thesis_topic}")

        return "\n".join(lines)


class University:
    """Manages departments, enrollment, hiring, and university reports."""

    def __init__(self, name: str) -> None:
        """Initializes a university with no departments."""
        self.name = name
        self._departments: dict[str, Department] = {}

    def add_department(self, department: Department) -> None:
        """Adds a department with a unique name."""
        if department.name in self._departments:
            raise ValueError("Department already exists")
        self._departments[department.name] = department

    def _get_department(self, name: str) -> Department:
        """Returns a department or raises an error if it does not exist."""
        if name not in self._departments:
            raise ValueError(f"Department not found: {name}")
        return self._departments[name]

    def enroll_student(self, dept_name: str, student: Student) -> None:
        """Enrolls a student in the specified department."""
        self._get_department(dept_name).add_member(student)

    def hire_teacher(self, dept_name: str, teacher: Teacher) -> None:
        """Adds a teacher and updates their department affiliation."""
        department = self._get_department(dept_name)
        department.add_member(teacher)
        teacher.department = dept_name

    def _all_people(self) -> set[Person]:
        """Returns unique people across university departments."""
        return {
            person
            for department in self._departments.values()
            for person in department
        }

    def overall_stats(self) -> dict[str, int | float]:
        """Returns statistics with unique people counted only once."""
        people = self._all_people()
        students = [
            person for person in people
            if isinstance(person, Student)
        ]

        return {
            "departments": len(self._departments),
            "people": len(people),
            "students": len(students),
            "teachers": sum(
                isinstance(person, Teacher)
                for person in people
            ),
            "graduate_students": sum(
                isinstance(person, GradStudent)
                for person in people
            ),
            "average_student_gpa": (
                sum(student.gpa for student in students) / len(students)
                if students else 0.0
            ),
        }

    def find_person(self, name: str) -> list[Person]:
        """Finds people by exact name, ignoring letter case."""
        return sorted(
            (
                person
                for person in self._all_people()
                if person.name.casefold() == name.casefold()
            ),
            key=lambda person: person.id,
        )

    def report(self) -> str:
        """Returns a complete university report."""
        lines = [f"UNIVERSITY: {self.name}"]

        for key, value in self.overall_stats().items():
            text = f"{value:.2f}" if isinstance(value, float) else str(value)
            lines.append(f"{key}: {text}")

        for department in self._departments.values():
            lines.append("\n" + department.report())

        return "\n".join(lines)


def main() -> None:
    """Demonstrates university management and the class hierarchy."""
    university = University("Zhytomyr Polytechnic")

    teacher1 = Teacher(
        name="Олена", email="olena@example.com",
        department="Computer Science", salary=25000,
    )
    teacher2 = Teacher(
        name="Андрій", email="andrii@example.com",
        department="Computer Science", salary=22000,
    )
    teacher3 = Teacher(
        name="Марія", email="maria@example.com",
        department="Mathematics", salary=26000,
    )
    teacher4 = Teacher(
        name="Олег", email="oleh@example.com",
        department="Mathematics", salary=23000,
    )

    teacher1.assign_course("Python")
    teacher2.assign_course("Databases")
    teacher3.assign_course("Calculus")
    teacher4.assign_course("Linear Algebra")

    teacher4.assign_course("Optional Course")
    teacher4.remove_course("Optional Course")

    cs = Department("Computer Science", teacher1)
    math = Department("Mathematics", teacher3)

    university.add_department(cs)
    university.add_department(math)
    university.hire_teacher(cs.name, teacher2)
    university.hire_teacher(math.name, teacher4)

    student_data = [
        ("Максим", 3, "Software Engineering", cs.name, 4.8),
        ("Ірина", 2, "Computer Science", cs.name, 4.5),
        ("Богдан", 1, "Computer Science", cs.name, 3.2),
        ("Софія", 4, "Software Engineering", cs.name, 3.8),
        ("Дмитро", 2, "Mathematics", math.name, 4.9),
        ("Анна", 3, "Mathematics", math.name, 4.1),
        ("Роман", 1, "Applied Mathematics", math.name, 2.5),
        ("Юлія", 4, "Applied Mathematics", math.name, 3.4),
    ]

    for index, (name, year, major, department, grade) in enumerate(
        student_data, start=1
    ):
        student = Student(
            name=name,
            email=f"student{index}@example.com",
            year=year,
            major=major,
        )

        subject = "Python" if department == cs.name else "Calculus"
        student.add_grade(subject, grade)
        student.add_grade(subject, min(5, grade + 0.2))
        student.add_grade("English", 4.0)

        university.enroll_student(department, student)

    graduate = GradStudent(
        name="Назар",
        email="nazar@example.com",
        year=5,
        major="Computer Science",
        department=cs.name,
        salary=15000,
        thesis_topic="Machine Learning in Education",
        supervisor=teacher1,
    )
    graduate.add_grade("Research Methods", 5)
    graduate.add_grade("Advanced Python", 4.8)
    graduate.assign_course("Python Practice")

    university.enroll_student(cs.name, graduate)

    cs.remove_member(teacher2)
    university.hire_teacher(cs.name, teacher2)

    print(university.report())

    print("\nSEARCH RESULTS:")
    for person in university.find_person("Максим"):
        print(repr(person))

    print("\nDEPARTMENT ITERATION:")
    for person in cs:
        print(f"{person.name}: {person.role()}")

    print("\nGRADUATE STUDENT MRO:")
    print(" -> ".join(cls.__name__ for cls in GradStudent.__mro__))

    print("\nIDENTITY AND HASHING:")
    print("Same person:", graduate == graduate)
    print("Different people:", graduate == teacher1)
    print("Unique people:", len({graduate, graduate, teacher1}))

    print("\nPERSON REGISTRY:")
    for person in Person.get_registry():
        print(f"{person.id}: {person.name} — {person.role()}")

    print("Registered people:", len(Person.get_registry()))


if __name__ == "__main__":
    main()