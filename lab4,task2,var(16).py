import math

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))

if z == 0 or abs(z) == 1:
	print("Помилка: z не повинен бути рівним 0, 1 або -1.")
else:
	преше = abs(math.sin(x) ** 2 - y * math.exp(2 * z))
	друге = math.sqrt(abs(z)) + 2
	чисельник = (x + y)
	знаменник = math.log(abs(z), 8)
	result = преше + друге - чисельник/знаменник

	print(f"M = {result}")
    