import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

if z == 0 or abs(z) == 1:
	print("Ошибка: z не должен быть равен 0, 1 или -1.")
else:
	first_part = abs(math.sin(x) ** 2 - y * math.exp(2 * z))
	second_part = math.sqrt(abs(z)) + 2
	third_part = (x + y) / math.log(abs(z), 8)
	result = first_part + second_part - third_part

	print(f"M = {result}")
