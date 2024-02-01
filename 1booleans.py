# BOOLEANS
# EX1
print(10>9)
True
# ex2
print(10 == 9)
False
# ex3
print(10<9)
False
# EX4
print(bool("abc"))
True
# ex5
print(bool(0))
False
 
#  EXAMPLES
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

def myfunction() :
  return True
print(myfunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 200
print(isinstance(x, int))


