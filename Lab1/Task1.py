# Оголошення змінних
n1 = 2
n2 = 34
nf1 = 5.4
nf2 = 56.6

str1 = "smth"
str2 = "not smth"

bl1 = True
bl2 = False

# Виведення типу і значення змінних
print(type(n1), n1, type(n2), n2, sep='-')
print('[',type(nf1), n1, type(nf2), n2, end=']\n')

print(type(str1), str1)
print(type(str2), str2)

print(type(bl1), bl1)
print(type(bl2), bl2)

# Перетворення чисел
num_to_string = str(n1)
print("Число у рядок:", num_to_string, type(num_to_string))

string_num = "100"
string_to_int = int(string_num)
print("Рядок у ціле число:", string_to_int, type(string_to_int))

string_float = "12.5"
string_to_float = float(string_float)
print("Рядок у дробове число:", string_to_float, type(string_to_float))