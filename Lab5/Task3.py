import logging

logging.basicConfig(
    filename="errorsTask3.log",
    filemode="w",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def demonstrate_exceptions() -> None:
    try:
        raise ZeroDivisionError("Ділення на нуль")
    except ZeroDivisionError as e:
        logging.error(e, exc_info=True)

    try:
        raise ValueError("Некоректне значення")
    except ValueError as e:
        logging.error(e, exc_info=True)

    try:
        raise IndexError("Індекс поза межами списку")
    except IndexError as e:
        logging.error(e, exc_info=True)

    try:
        raise KeyError("Відсутній ключ")
    except KeyError as e:
        logging.error(e, exc_info=True)

    try:
        raise FileNotFoundError("Файл не знайдено")
    except FileNotFoundError as e:
        logging.error(e, exc_info=True)

    try:
        raise ZeroDivisionError("Ділення на нуль")
    except ArithmeticError as e:
        logging.error(f"Перехоплено через ArithmeticError: {e}", exc_info=True)

    try:
        raise ZeroDivisionError("Ділення на нуль")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)

    try:
        raise ValueError("Некоректне значення")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)

    try:
        raise IndexError("Індекс поза межами списку")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)

    try:
        raise KeyError("Відсутній ключ")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)

    try:
        raise FileNotFoundError("Файл не знайдено")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)

    try:
        raise KeyboardInterrupt("Переривання користувачем")
    except Exception as e:
        logging.error(f"Перехоплено через Exception: {e}", exc_info=True)
    except KeyboardInterrupt as e:
        logging.error(f"Exception не перехопив KeyboardInterrupt: {e}", exc_info=True)


demonstrate_exceptions()

with open("errorsTask3.log", "r", encoding="utf-8") as file:
    print(file.read())