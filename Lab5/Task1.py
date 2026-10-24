import logging

logging.basicConfig(
    filename="errorsTask1.log",
    encoding="utf-8",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def safe_calculator() -> None:
    successful = 0
    errors = 0

    print("Для завершення введіть 'q'.")

    while True:
        first_input = input("\nВведіть перше число: ").strip()
        if first_input.lower() == "q":
            break

        second_input = input("Введіть друге число: ").strip()
        if second_input.lower() == "q":
            break

        try:
            num1 = float(first_input)
            num2 = float(second_input)
        except ValueError:
            errors += 1
            err = "Помилка: обидва значення мають бути числами"
            print(err)
            logging.error(err, exc_info=True)
            continue

        opr = input("Введіть оператор (+, -, *, /, //, %): ").strip()
        if opr.lower() == "q":
            break

        try:
            match opr:
                case "+":
                    result = num1 + num2
                case "-":
                    result = num1 - num2
                case "*":
                    result = num1 * num2
                case "/":
                    result = num1 / num2
                case "//":
                    result = num1 // num2
                case "%":
                    result = num1 % num2
                case _:
                    raise ValueError(f"Невідомий оператор: '{opr}'")
        except ValueError as error:
            errors += 1
            err = f"Помилка: {error}"
            print(err)
            logging.error(err, exc_info=True)
        except ZeroDivisionError:
            errors += 1
            err = "Помилка: дільник не може дорівнювати нулю для /, // та %"
            print(err)
            logging.error(err, exc_info=True)
        else:
            successful += 1
            print("Результат:", result)

    print("\nКількість успішних обчислень:", successful)
    print("Кількість помилок:", errors)


safe_calculator()