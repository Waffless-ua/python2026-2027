text = str(input('Введіть будь-який текст:'))

words = text.split()

print(f"Кількість слів: {len(words)}")
print(f"Найдовше слово: {max(words, key=len)}")
print(f"Найкоротше слово: {min(words, key=len)}")

sorted_words = sorted(words)

sorted_words_string = ', '.join(sorted_words)
print(f"Відсортовані слова: {sorted_words_string}")

reversed_words = words[::-1]
print(f"Відсортовані слова у зворотньому порядку: {reversed_words}")

for word in words:
    if word.lower() == word[::-1].lower():
        print(f"Паліндром: {word}")
