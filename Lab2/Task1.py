text = input('Введіть будь-який текст:')

print("Довжина тексту:", len(text))
print("Перший символ:", text[0])
print("Останній символ:", text[-1])

print("В нижньому регістрі:", text.lower())
print("В верхньому регістрі:", text.upper())
print("Слова з великої літери:", text.title())
print("У зворотньому порядку:", text[::-1])

letter = input('Введіть літеру для пошуку: ')

print("Кількість", letter, "в", text, ":", text.count(letter))

str1 = input('Введіть рядок для перевірки, чи починаються та/або закінчується текст на нього: ')

if text.startswith(str1):
    print(text ,"починається з", str1)
else:
    print(text ,"не починається з", str1)

if text.endswith(str1):
    print(text, "закінчується на", str1)
else:
    print(text, "не закінчується на", str1)

print("Пробіли замінені на \'_\':", text.replace(' ', '_'))