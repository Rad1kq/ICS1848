import math

x = float(input("Введіть x(обов'язково x>0): "))
# оператор if за для усунення помилки при введенні х<0
if x <= 0:
	print("Помилка: x повинен бути більшим за 0.")
else:
	чисельник = math.log(x) - math.log10(x) + math.log(4 * x, 2)
	знаменник = math.fabs(math.cos(x)) + 0.4
	result = чисельник / знаменник + 0.12 * math.pow(3 * x + 3, 1 / 5)

	print(f"f({x}) = {result}")


