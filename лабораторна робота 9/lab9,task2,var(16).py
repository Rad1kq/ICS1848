txt = input("Введіть рядок: ")

counts = {}
for sym in txt:
    counts[sym] = counts.get(sym, 0) + 1

unique_sym = list(counts)
single_sym = [sym for sym, count in counts.items() if count == 1]

print("Кількість повторів символів:", counts)
print("Унікальні символи:", unique_sym)
print("Символи, які зустрічаються лише один раз:", single_sym)
