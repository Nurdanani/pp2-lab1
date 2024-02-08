def print_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            r= s[:i] + s[i+1:]
            print_permutations(r, prefix + s[i])
user_string = "abcd" 
print_permutations(user_string)