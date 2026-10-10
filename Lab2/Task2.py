number_list = []

for i in range(8):
    num = int(input(f"Введіть {i+1}-е число, щоб додати у список: "))
    number_list.append(num)

print(f"Список: {number_list}")
print(f"Довжина списку: {len(number_list)}")
print(f"Максимум: {max(number_list)}")
print(f"Мінімум: {min(number_list)}")
print(f"Сума елементів: {sum(number_list)}")

print(f"Перший елемент: {number_list[0]}")
print(f"Останній елемент: {number_list[-1]}")
print(f"Перші три елементи: {number_list[:3]}")
print(f"Останні три елементи: {number_list[-3:]}")

sort_list = sorted(number_list)
print(f"Відсортований список: {sort_list}")

no_duplicated_numbers = list(set(number_list))
print(f"Список без дублікатів: {no_duplicated_numbers}")

greater_than_average_numbers = [
    number for number in number_list if number > sum(number_list) / len(number_list)
]
print(f"Елементи, більші за середнє арифметичне: {greater_than_average_numbers}")
