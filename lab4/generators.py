# ex1
N=int(input())
sq=(i**2 for i in range(N+1))
for i in sq:
    print(i)
    
# ex2
def even(n):
    for i in range(0, n + 1, 2):
        yield i
    
n = int(input())
even1 = even(n)
for num in even1:
    print(num)
    
# ex3
def div(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
g= div(n)
for i in g:
    print(i)

# ex4
a=int (input ( ))
b=int (input ( ))
def s(a,b) :
  for i in range (a, b):
    yield i**2
result = [str (num) for num in s(a, b)]
print (",". join(result))

# ex5
def nums(n):
    while n >= 0:
        yield n
        n -= 1
n=int(input())
generator = nums(n)
for num in generator:
    print(num)