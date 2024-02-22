# ex1
import math
def deg(degree):
    return degree*(math.pi/180)
degree=15
rad=deg(degree)
print(rad)

# ex2
import math
def area(h, a, b):
    return (h*(a+b))/2
h=5
a=5
b=6
area1=area(h,a,b)
print(area1)

# ex3
import math
def area(l,n):
    return (pow(l,2)*n)/(4*math.tan(math.pi/n))
l=25
n=4
area1=area(l,n)
print(area1)

# ex4
import math
def area(h,l):
    return h*l
h=6
l=5
area1=area(h,l)
print(area1)
