# Прості числа
n = float(input('Введіть число:'))

for k in range(2, round(n) + 1):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            break
    else:
        print(k, end=" ")


# Трикутник Паскаля
rows = 6
triangle = []

for i in range(rows):
    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    triangle.append(row)

print("\nТрикутник Паскаля:")
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(triangle[i][j], end=" ")
    print()