def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

string = input()
if is_palindrome(string):
    print("yes")
else:
    print("no")
