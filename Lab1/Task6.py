operations_count = 0

while True:
    a = float(input('Введіть число:'))
    operator = input("Введіть операцію (+, -, *, /, //, %, **): ").strip()
    b = float(input('Введіть число:'))

    result = None

    match operator:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            if b == 0:
                print("Помилка: ділення на нуль неможливе!")
            else:
                result = a / b
        case '//':
            if b == 0:
                print("Помилка: цілочисельне ділення на нуль неможливе!")
            else:
                result = a // b
        case '%':
            if b == 0:
                print("Помилка: остача від ділення на нуль неможлива!")
            else:
                result = a % b
        case '**':
            result = a ** b
        case _:
            print("Помилка: невідомий символ операції!")

    if result is not None:
        print(f"Результат: {result}")
        operations_count += 1

    continue_choice = input("Продовжити? (y/n): ").strip().lower()

    if continue_choice == 'n':
        break

print(f"\nРоботу завершено. Всього виконано успішних обчислень: {operations_count}")