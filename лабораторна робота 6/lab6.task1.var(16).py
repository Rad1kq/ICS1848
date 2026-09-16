import math

a=float(input("введіть а: "))
b=float(input("введіть b: "))
h=float(input("введіть крок h: "))

n= int((b-a)/ h)

for i in range(n):
    x= a + i * h
    y= math.pow(x,3) + math.exp(x) / math.fabs(math.sin(x) + 0.12)
    print("x=", x, "f(x)=",y)