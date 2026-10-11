n = int(input("Скільки рядків будемо вводити? "))

best_string = ""
best_sum = -1

for i in range(n):
    s = input(f"Введіть рядок {i + 1}: ")

    current_sum = 0
    for ch in s:
        if ch.isdigit():
            current_sum += int(ch)

    if current_sum > best_sum:
        best_sum = current_sum
        best_string = s

print("Рядок з максимальною сумою цифр:", best_string)
print("Сума цифр:", best_sum)
