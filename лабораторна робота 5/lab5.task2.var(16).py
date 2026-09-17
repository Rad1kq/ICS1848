число=int(input("введіть трицифрове число: "))

x1= число // 100
x2=(число // 10) % 10
x3= число % 10

if x1 >= x2 and x1 >= x3:
    max_digit=x1
elif x2 >= x1 and x2 >= x3:
    max_digit=x2
else:
    max_digit=x3

if x1 <= x2 and x1 <= x3:
    min_digit=x1
elif x2 <= x1 and x2 <= x3:
    min_digit=x2
else:
    min_digit=x3

result= max_digit + min_digit
print("сума найбільшой та найменшої цифр", result)