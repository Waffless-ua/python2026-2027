import re


def analyze_contacts() -> None:
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print('Файл "contacts.txt" не знайдено')
        return
    except PermissionError:
        print('Немає прав на читання "contacts.txt"')
        return
    except UnicodeDecodeError:
        print('Файл "contacts.txt" має неправильне кодування')
        return

    email_pattern = (
        r"[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    )

    phone_pattern = (
        r"(?<!\w)"
        r"(?:\+38[ \t-]*)?"
        r"(?:\(0\d{2}\)|0\d{2})"
        r"[ \t-]*\d{3}[ \t-]*\d{2}[ \t-]*\d{2}"
        r"(?!\w)"
    )

    date_pattern = (
        r"\b(0[1-9]|[12][0-9]|3[01])"
        r"\.(0[1-9]|1[0-2])"
        r"\.([0-9]{4})\b"
    )

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    dates = [
        re.sub(date_pattern, r"\3-\2-\1", match.group())
        for match in re.finditer(date_pattern, text)
    ]

    sections = {
        "EMAIL-АДРЕСИ": emails,
        "ТЕЛЕФОНИ": phones,
        "ДАТИ (ISO)": dates,
    }

    try:
        with open("results.txt", "w", encoding="utf-8") as file:
            for title, values in sections.items():
                file.write(f"{title}\n")

                if values:
                    file.write("\n".join(values) + "\n")
                else:
                    file.write("Не знайдено\n")

                file.write("\n")
    except PermissionError:
        print('Немає прав на запис "results.txt"')
    else:
        print('Результати записано у "results.txt"')
        print("Email-адрес:", len(emails))
        print("Телефонів:", len(phones))
        print("Дат:", len(dates))


analyze_contacts()