s = input("Введіть рядок слів: ")

words = s.split()

unique_words = set()

for word in words:
    unique_words.add(word)

print("Унікальні слова:", unique_words)
