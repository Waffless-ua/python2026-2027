numbers = list(range(-10, 11))
multiples_of_three = list(filter(lambda number: number % 3 == 0, numbers))

print("Числа, кратні 3:", multiples_of_three)

celsius = [0, 20, 37, 100]
kelvin = list(map(lambda temperature: temperature + 273.15, celsius))

print("Температури в Кельвінах:", kelvin)

words = ["кіт", "село", "весна", "дуб", "море"]
sorted_words = sorted(words, key=lambda word: word[-1])

print("Слова за останньою літерою:", sorted_words)

people = [
    {"name": "Іван", "age": 22},
    {"name": "Марія", "age": 19},
    {"name": "Андрій", "age": 25},
    {"name": "Олена", "age": 21},
    {"name": "Богдан", "age": 18},
]

filtered_people = sorted(
    filter(lambda person: person["age"] >= 21, people),
    key=lambda person: person["name"],
)

print("Люди віком від 21 року за іменем:", filtered_people)