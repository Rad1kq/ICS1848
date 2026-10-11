import random

arr=[random.randint(1,20) for i in range(7)]

print("Початковий масив:", arr)

n= int(input("Введіть число: "))

middle_index = len(arr) // 2

new_numbers = [random.randint(31, 40) for _ in range(n)]

result = arr[:middle_index + 1] + new_numbers + arr[middle_index + 1:]
print("Масив після вставки нових чисел:", result)
