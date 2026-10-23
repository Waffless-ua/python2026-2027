text = """
Студенти вивчають Python та створюють цікаві програми.
Python допомагає аналізувати текст, обробляти дані та знаходити помилки.
На заняттях студенти використовують списки, кортежі, множини та словники.
Словники зберігають дані, а множини допомагають знаходити унікальні елементи.
Студенти пишуть програми щодня, перевіряють результати та вдосконалюють
свої навички. Python робить навчання цікавим, а практичні завдання
допомагають краще розуміти алгоритми та структури даних.
"""

normalized_text = text.lower()

for punctuation in ".,!?;:()[]{}«»\"":
    normalized_text = normalized_text.replace(punctuation, " ")

words = normalized_text.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Кількість входжень слів:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

top_words = sorted(
    word_counts.items(),
    key=lambda item: item[1],
    reverse=True,
)[:3]

print("\nТри найуживаніші слова:")
for word, count in top_words:
    print(f"{word}: {count}")

letter_counts = {}

for character in text.lower():
    if character.isalpha():
        letter_counts[character] = letter_counts.get(character, 0) + 1

print("\nКількість входжень букв:")
for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}")

inverted_index = {}

for index, word in enumerate(words):
    if word not in inverted_index:
        inverted_index[word] = []
    inverted_index[word].append(index)

print("\nЗворотний індекс (позиції слів, починаючи з 0):")
for word, positions in inverted_index.items():
    print(f"{word}: {positions}")

unique_count = len(word_counts)
unique_percentage = unique_count / len(words) * 100 if words else 0

print("\nЗагальна кількість слів:", len(words))
print("Кількість унікальних слів:", unique_count)
print(f"Відсоток унікальних слів: {unique_percentage:.2f}%")