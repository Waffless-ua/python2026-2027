cities = ("Київ", "Житомир", "Львів", "Одеса", "Харків")

print("Перше місто:", cities[0])
print("Останнє місто:", cities[-1])
print("У зворотному порядку:", cities[::-1])
print("Довжина кортежу:", len(cities))


def minmax(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


lo, hi = minmax([12, 4, 19, -3, 8])

print("Мінімум:", lo)
print("Максимум:", hi)

first, *middle, last = (1, 2, 3, 4, 5)

print("Перший елемент:", first)
print("Середня частина:", middle)
print("Останній елемент:", last)

a, b, c = 10, 20, 30
print("До перестановки:", a, b, c)

a, b, c = b, c, a
print("Після перестановки:", a, b, c)

number = (5)
single_tuple = (5,)

print("(5):", number, type(number).__name__)
print("(5,):", single_tuple, type(single_tuple).__name__)
#Кортеж утворює кома. Без коми дужки лише групують вираз