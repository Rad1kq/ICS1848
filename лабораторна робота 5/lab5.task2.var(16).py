число=int(input("введіть трицифрове число: "))

x1= число // 100
x2=(число // 10) % 10
x3= число % 10

max_digit= max(x1,x2,x3)
min_digit= min(x1,x2,x3)

result= max_digit + min_digit
print("сума найбільшой та найменшої цифр", result)