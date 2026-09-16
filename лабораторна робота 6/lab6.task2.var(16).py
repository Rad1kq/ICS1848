import math

a=float(input("введіть а: "))
b=float(input("введіть b: "))
h=float(input("введіть крок h: "))

x= a
while x <= b:
    y= math.pow(x,3) + math.exp(x) / math.fabs(math.sin(x) + 0.12)
    print("x=", x, "f(x)=",y)
    x+=h