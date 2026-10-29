firm = {}
firm_1 = int(input("Введіть кількість фірм: "))

for _ in range(firm_1):
    name = input("Введіть назву фірми: ")
    workers = int(input("Введіть кількість працівників: "))
    firm[name] = workers

founded_years = {}
for name in firm:
    founded_years[name] = int(input(f"Введіть рік заснування фірми {name}: "))

print("Словник з роками заснування:", founded_years)
