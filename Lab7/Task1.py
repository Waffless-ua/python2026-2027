

class Rectangle:
    """Represents a rectangle with positive width and height."""

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> int | float:
        """Width of the rectangle. Must be greater than 0."""
        return self._width

    @width.setter
    def width(self, value: int | float) -> None:
        if not value > 0:
            raise ValueError("Width must be greater than 0")
        self._width = value

    @property
    def height(self) -> int | float:
        """Height of the rectangle. Must be greater than 0."""
        return self._height

    @height.setter
    def height(self, value: int | float) -> None:
        if not value > 0:
            raise ValueError("Height must be greater than 0")
        self._height = value


    @property
    def area(self) -> int | float:
        """Area of the rectangle. Read-only."""
        return self._width * self._height

    @property
    def perimeter(self) -> int | float:
        """Perimeter of the rectangle. Read-only."""
        return 2 * (self._width + self._height)

    @property
    def diagonal(self) -> float:
        """Length of the rectangle's diagonal. Read-only."""
        return (self._width ** 2 + self._height ** 2) ** 0.5

    @property
    def is_square(self) -> bool:
        """Whether the rectangle is a square. Read-only."""
        return self._width == self._height


    def scale(self, factor: int | float) -> "Rectangle":
        """Returns a new rectangle scaled by a positive factor."""
        if not factor > 0:
            raise ValueError("Коефіцієнт масштабування має бути більшим за 0")

        return Rectangle(self._width * factor, self._height * factor)

    def describe(self) -> str:
        """Returns a formatted description of the rectangle."""
        return (
            f"Прямокутник {self.width} × {self.height}; "
            f"площа: {self.area}; "
            f"периметр: {self.perimeter}; "
            f"діагональ: {self.diagonal:.2f}; "
            f"квадрат: {'так' if self.is_square else 'ні'}"
        )

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width!r}, height={self.height!r})"

    def __str__(self) -> str:
        return self.describe()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.width == other.width and self.height == other.height

    def __lt__(self, other: "Rectangle") -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.area < other.area

    def __add__(self, other: "Rectangle") -> "Rectangle":
        if not isinstance(other, Rectangle):
            return NotImplemented

        total_area = self.area + other.area
        return Rectangle(self.width, total_area / self.width)

    @classmethod
    def from_string(cls, dimensions: str) -> "Rectangle":
        """Return a rectangle from a string representation of the dimensions. Example: 6x4"""
        width_text, height_text = dimensions.split("x")
        return cls(float(width_text), float(height_text))

    @staticmethod
    def is_valid(w: int | float, h: int | float) -> bool:
        """Checks whether both dimensions are positive."""
        return w > 0 and h > 0


def main() -> None:
    rectangle = Rectangle(3, 4)
    same_rectangle = Rectangle(3, 4)
    square = Rectangle(5, 5)

    print("1. Ширина:", rectangle.width)
    print("2. Висота:", rectangle.height)
    print("3. Площа:", rectangle.area)
    print("4. Периметр:", rectangle.perimeter)
    print("5. Діагональ:", rectangle.diagonal)
    print("6. Чи квадрат:", rectangle.is_square)
    print("7. Чи квадрат 5 × 5:", square.is_square)

    print("8. Масштабування:", rectangle.scale(2))
    print("9. Початковий прямокутник:", rectangle.describe())

    print("10. repr:", repr(rectangle))
    print("11. str:", str(rectangle))

    print("12. Однакові розміри:", rectangle == same_rectangle)
    print("13. Різні розміри:", rectangle == Rectangle(4, 3))
    print("14. Порівняння площ:", rectangle < square)

    combined = rectangle + square
    print("15. Додавання:", combined)
    print("Ширина результату:", combined.width)
    print("Сумарна площа:", combined.area)

    print("16. Створення з рядка:", Rectangle.from_string("4x5"))
    print("17. Додатні розміри:", Rectangle.is_valid(4, 5))
    print("18. Нульова ширина:", Rectangle.is_valid(0, 5))
    print("19. Від’ємна висота:", Rectangle.is_valid(4, -5))

    rectangle.width = 6
    rectangle.height = 8
    print("20. Зміна розмірів:", rectangle)

    try:
        Rectangle(0, 4)
    except ValueError as error:
        print("21. Некоректний конструктор:", error)

    try:
        rectangle.width = -2
    except ValueError as error:
        print("22. Некоректна ширина:", error)

    try:
        rectangle.height = 0
    except ValueError as error:
        print("23. Некоректна висота:", error)

    try:
        rectangle.scale(0)
    except ValueError as error:
        print("24. Некоректний масштаб:", error)

    try:
        rectangle.area = 100
    except AttributeError as error:
        print("25. Властивість лише для читання:", error)


if __name__ == "__main__":
    main()