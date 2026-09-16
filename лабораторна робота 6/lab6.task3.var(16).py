import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

values = []
x = a

# 1. Заповнюємо список усім значеннями
while x <= b:
    y = (x**3 + math.exp(x)) / (abs(math.sin(x)) + 0.12)
    values.append(y)
    x += h

print("Список усіх значень:", values)

# 2. Знаходимо номер (індекс) найменшого елемента
min_index = values.index(min(values))

# 3. Відрізаємо частину списку від початку до найменшого включно
result = values[:min_index + 1]

print("Елементи від початку до найменшого:", result)