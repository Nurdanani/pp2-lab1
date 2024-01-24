# EXERCISE:
# syntax
# ex1
print("Hello World")
# ex2
if 5 > 2:
    print("YES")
# COMMENTS
# ex1
#This is a comment
# ex2
"""
This is a comment
written in 
more than just one line
"""
# variables
# ex1
carname="Volvo"
# ex2
x = 50
# ex3
x = 5
y = 10
print(x + y)
# ex4
x = 5
y = 10
z = x + y
print(z)
# ex5
x,y,z = "Orange", "Banana", "Cherry"
# ex6
x = y = z ="Orange"
# ex7
def myfunc():  
 global x
 x = "fantastic"
#  Datatypes
# ex1
x = 5
print(type(x))

int
# ex2
x = "Hello World"
print(type(x))

str
# ex3
x = 20.5
print(type(x))

float
# ex4
x = ["apple", "banana", "cherry"]
print(type(x))

list
# ex5
x = ("apple", "banana", "cherry")
print(type(x))

tuple
# ex6
x = {"name" : "John", "age" : 36}
print(type(x))

dict
# ex7
x = True
print(type(x))

bool
# Numbers
# ex1
x = 5
x = float(x)
# ex2
x = 5.5
x = int(x)
# ex3
x = 5
x = complex(x)
# Strings
# ex1
x = "Hello World"
print(len(x))
# ex2
txt = "Hello World"
x = txt[0]
# ex3
txt = "Hello World"
x = txt[2:5]
# ex4
txt = " Hello World "
x = txt.strip()
# ex5
txt = "Hello World"
txt = txt.upper()
# ex6
txt = "Hello World"
txt = txt.lower()
# ex7
txt = "Hello World"
txt = txt.replace("H","J")
# ex8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# EXAMPLES:
if 5>2:
    print("fife is greater than two!")
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
        
x = 5
y = "Hello, World!"

# comments
#This is a comment.
print("Hello, World!")

print("Hello, World!")#This is a comment.

# print("hello, world!")
print("cheers, mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("hello, world!")

# Variables
x = 5
y = "John"
print(x)
print(y)

x=4 #x is of type int
x="sally" # x is now of type str
print(x)

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
#is the same as
x = 'John'

a = 4
A= "Sally"
#A will not overwrite a

myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"

x, y, z = "orange","banana","cherry"
print(x)
print(y)
print(z)

x=y=z="orange"
print(x)
print(y)
print(z)

fruits=["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x="Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Py"
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Numbers
x = 1 # int
y = 2.8 # float
z = 1j # complex
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35792371892782918
z = -3252682
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -78.89
print(type(x))
print(type(y))
print(type(z))

x = 1    
y = 2.8  
z = 1j  
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))

# STRINGS
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)
  
a = "Hello"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes")
  
txt = "The best things in life are free!"
print("expensive" not in txt)





    







