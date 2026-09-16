import math
x=float(input("введіть значення х: "))

if x>=3:
    y=x-math.log(x)+math.log10(2*x)+math.pow(math.e,x)
    print("y=",y)
elif 0.2 < x < 3:
    y= 6.53*(1-x/math.pow(math.e,0.1*x)) + 0.11*x
    print("y=",y)
else:
    y= 5.3 + x*math.e**x
    print("y=",y)
