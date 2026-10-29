class DIGIT:
    def __init__(self, value):
        if value < 1:
            raise ValueError("Число має бути натуральним.")

        self.value = value
        self.is_even = value % 2 == 0

    def divisors(self):
        return [
            divisor
            for divisor in range(1, self.value + 1)
            if self.value % divisor == 0
        ]

    def is_prime(self):
        return len(self.divisors()) == 2


number = int(input("Введіть натуральне число: "))
digit = DIGIT(number)

print("Значення:", digit.value)
print("Число парне:", digit.is_even)
print("Дільники:", digit.divisors())

if digit.is_prime():
    print("Число є простим.")
else:
    print("Число не є простим.")
