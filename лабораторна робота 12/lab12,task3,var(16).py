from arithmetic_progression import nth_term, sum_terms


first_term = float(input("Введіть перший член прогресії: "))
difference = float(input("Введіть різницю прогресії: "))
n = int(input("Введіть номер члена та кількість членів N: "))

term = nth_term(first_term, difference, n)
total = sum_terms(first_term, difference, n)

print(f"{n}-й член прогресії: {term}")
print(f"Сума перших {n} членів: {total}")
