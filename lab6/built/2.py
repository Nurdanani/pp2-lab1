def count(string):
    u = 0
    l = 0
    for char in string:
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
    
    print("upper letter:", u)
    print("lower letter:", l)

string = input()
count(string)
