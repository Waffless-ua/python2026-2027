squares = [number ** 2 for number in range(1, 21) if number % 2 != 0]
print(f"Квадрати непарних чисел: {squares}")

text = input("Введіть речення: ")
lengths = [len(word) for word in text.split() if len(word) > 3]
print(f"Довжини слів (> 3): {lengths}")

matrix = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(f"Таблиця множення 5×5: {matrix}")

flattened = [number for row in matrix for number in row]
print(f"Сплощена матриця: {flattened}")

pairs = [(i, j) for i in range(1, 6) for j in range(1, 6) if i < j]
print(f"Пари (i, j), де i < j: {pairs}")