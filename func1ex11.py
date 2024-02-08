def palindrome(word):
    word = word.lower() 
    if word[::-1] == word:
        print("Yes")
    else:
        print("No")

palindrome("anna")