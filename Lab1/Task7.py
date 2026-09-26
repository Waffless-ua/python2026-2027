secret_number = 14
max_attempts = 7
attempts = 0


while attempts < max_attempts:
    guess = int(input(f"Спроба {attempts + 1}. Введіть ваше число: "))

    attempts += 1

    if guess == secret_number:
        print(f"Вітаємо! Ви вгадали число за {attempts} спроб(и).")
        break
    elif guess < secret_number:
        print("Більше!")
    else:
        print("Менше!")
else:
    print(f"Ви вичерпали всі {max_attempts} спроб. Секретне число було: {secret_number}")

# Статистика числової послідовності
N = int(input("Введіть кількість чисел (N): "))

if N > 0:
    numbers = []

    total_sum = 0
    min_val = None
    max_val = None

    count_3 = 0
    count_5 = 0
    count_3_5 = 0

    for i in range(N):
        num = float(input(f"Введіть число {i + 1}: "))
        numbers.append(num)

        total_sum += num

        if min_val is None or num < min_val:
            min_val = num
        if max_val is None or num > max_val:
            max_val = num

        if num.is_integer():
            int_num = int(num)
            if int_num % 3 == 0 and int_num % 5 == 0:
                count_3_5 += 1
            elif int_num % 3 == 0:
                count_3 += 1
            elif int_num % 5 == 0:
                count_5 += 1

    average = total_sum / N

    print("\n--- Результати ---")
    print(f"Сума: {total_sum}")
    print(f"Середнє: {average}")
    print(f"Мінімум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Кількість чисел, кратних 3: {count_3}")
    print(f"Кількість чисел, кратних 5: {count_5}")
    print(f"Кількість чисел, кратних одночасно 3 і 5: {count_3_5}")

    print("Числа у зворотньому порядку:", end=" ")
    for number in numbers[::-1]:
        print(number, end=" ")
    print()
else:
    print("Ви не ввели жодного числа для аналізу.")