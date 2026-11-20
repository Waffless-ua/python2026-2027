from collections.abc import Iterator


class Matrix:
    """Represents a numeric matrix with arithmetic and indexing operations."""

    def __init__(
        self,
        rows: int,
        cols: int,
        data: list[list[int | float]] | None = None,
    ) -> None:
        """Creates a matrix from row data or fills it with zeros."""
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive")

        self._rows = rows
        self._cols = cols

        if data is None:
            self._data: list[list[int | float]] = [
                [0 for _ in range(cols)]
                for _ in range(rows)
            ]
        else:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError("Data dimensions do not match rows and cols")

            if any(
                not isinstance(value, (int, float))
                for row in data
                for value in row
            ):
                raise TypeError("Matrix elements must be int | floats")

            self._data = [row.copy() for row in data]

    @property
    def rows(self) -> int:
        """Returns the int | float of rows."""
        return self._rows

    @property
    def cols(self) -> int:
        """Returns the int | float of columns."""
        return self._cols

    @property
    def is_square(self) -> bool:
        """Returns whether the matrix has equal int | floats of rows and columns."""
        return self.rows == self.cols

    @property
    def trace(self) -> int | float:
        """Returns the diagonal sum of a square matrix."""
        if not self.is_square:
            raise ValueError("Trace requires a square matrix")

        return sum(self._data[i][i] for i in range(self.rows))

    def __repr__(self) -> str:
        """Returns a technical representation of the matrix."""
        return (
            f"Matrix(rows={self.rows}, cols={self.cols}, "
            f"data={self._data!r})"
        )

    def __str__(self) -> str:
        """Returns a table with values aligned within each column."""
        text_rows = [
            [str(value) for value in row]
            for row in self._data
        ]

        widths = [
            max(len(row[j]) for row in text_rows)
            for j in range(self.cols)
        ]

        return "\n".join(
            " ".join(
                value.rjust(widths[j])
                for j, value in enumerate(row)
            )
            for row in text_rows
        )

    def __eq__(self, other: object) -> bool:
        """Compares matrix dimensions and elements."""
        if not isinstance(other, Matrix):
            return NotImplemented

        return (
            self.rows == other.rows
            and self.cols == other.cols
            and self._data == other._data
        )

    def _check_same_size(self, other: "Matrix") -> None:
        """Checks that two matrices have matching dimensions."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have matching dimensions")

    def __add__(self, other: "Matrix") -> "Matrix":
        """Returns the element-wise sum of two matrices."""
        if not isinstance(other, Matrix):
            return NotImplemented

        self._check_same_size(other)

        return Matrix(
            self.rows,
            self.cols,
            [
                [
                    self._data[i][j] + other._data[i][j]
                    for j in range(self.cols)
                ]
                for i in range(self.rows)
            ],
        )

    def __sub__(self, other: "Matrix") -> "Matrix":
        """Returns the element-wise difference of two matrices."""
        if not isinstance(other, Matrix):
            return NotImplemented

        self._check_same_size(other)

        return Matrix(
            self.rows,
            self.cols,
            [
                [
                    self._data[i][j] - other._data[i][j]
                    for j in range(self.cols)
                ]
                for i in range(self.rows)
            ],
        )

    def __mul__(self, scalar: int | float) -> "Matrix":
        """Returns a matrix with every element multiplied by an int | float."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Matrix(
            self.rows,
            self.cols,
            [
                [value * scalar for value in row]
                for row in self._data
            ],
        )

    def __rmul__(self, scalar: int | float) -> "Matrix":
        """Supports multiplication with an int | float on the left."""
        return self.__mul__(scalar)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """Returns the matrix product of two compatible matrices."""
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.cols != other.rows:
            raise ValueError(
                "The left column count must equal the right row count"
            )

        return Matrix(
            self.rows,
            other.cols,
            [
                [
                    sum(
                        self._data[i][k] * other._data[k][j]
                        for k in range(self.cols)
                    )
                    for j in range(other.cols)
                ]
                for i in range(self.rows)
            ],
        )

    def _validate_key(self, key: tuple[int, int]) -> None:
        """Validates a pair of non-negative row and column indices."""
        if not isinstance(key, tuple) or len(key) != 2:
            raise TypeError("Use a pair of indices: matrix[i, j]")

        i, j = key

        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("Matrix indices must be integers")

        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError("Matrix index out of range")

    def __getitem__(self, key: tuple[int, int]) -> int | float:
        """Returns the element at the specified row and column."""
        self._validate_key(key)
        i, j = key
        return self._data[i][j]

    def __setitem__(self, key: tuple[int, int], value: int | float) -> None:
        """Updates the element at the specified row and column."""
        self._validate_key(key)

        if not isinstance(value, (int, float)):
            raise TypeError("Matrix elements must be int | floats")

        i, j = key
        self._data[i][j] = value

    def __iter__(self) -> Iterator[list[int | float]]:
        """Yields copies of rows to protect the matrix structure."""
        for row in self._data:
            yield row.copy()

    def __len__(self) -> int:
        """Returns the int | float of rows."""
        return self.rows

    def transpose(self) -> "Matrix":
        """Returns a new matrix with rows and columns exchanged."""
        return Matrix(
            self.cols,
            self.rows,
            [
                [self._data[i][j] for i in range(self.rows)]
                for j in range(self.cols)
            ],
        )

    @classmethod
    def identity(cls, n: int) -> "Matrix":
        """Creates an identity matrix of size n by n."""
        if n <= 0:
            raise ValueError("Identity matrix size must be positive")

        return cls(
            n,
            n,
            [
                [1 if i == j else 0 for j in range(n)]
                for i in range(n)
            ],
        )


def main() -> None:
    """Demonstrates matrix properties, operators, and protocols."""
    m = Matrix(2, 2, [[1, 2], [3, 4]])
    other = Matrix(2, 2, [[5, 6], [7, 8]])

    print("Zero matrix:")
    print(Matrix(2, 3))

    print("\nMatrix m:")
    print(m)

    print("\nTechnical representation:")
    print(repr(m))

    print("\nRows:", m.rows)
    print("Columns:", m.cols)
    print("Is square:", m.is_square)
    print("Trace:", m.trace)

    print("\nEqual matrices:", m == Matrix(2, 2, [[1, 2], [3, 4]]))
    print("Different matrices:", m == other)

    print("\nAddition:")
    print(m + other)

    print("\nSubtraction:")
    print(m - other)

    print("\nScalar multiplication:")
    print(m * 3)

    print("\nScalar multiplication from the left:")
    print(2 * m)

    print("\nMatrix multiplication:")
    print(m @ other)

    print("\nElement m[0, 1]:", m[0, 1])

    m[0, 1] = 5
    print("\nAfter m[0, 1] = 5:")
    print(m)

    print("\nIteration over rows:")
    for row in m:
        print(row)

    print("\nlen(m):", len(m))

    rectangular = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])

    print("\nRectangular matrix:")
    print(rectangular)
    print("Is square:", rectangular.is_square)

    print("\nTransposed matrix:")
    print(rectangular.transpose())

    identity = Matrix.identity(2)

    print("\nIdentity matrix:")
    print(identity)

    print("\nMultiplication by identity preserves the matrix:")
    print(m @ identity == m)

    try:
        print(rectangular.trace)
    except ValueError as error:
        print("\nTrace error:", error)

    try:
        print(m + rectangular)
    except ValueError as error:
        print("Addition error:", error)

    try:
        print(rectangular @ m)
    except ValueError as error:
        print("Multiplication error:", error)

    try:
        print(m[5, 0])
    except IndexError as error:
        print("Index error:", error)


if __name__ == "__main__":
    main()