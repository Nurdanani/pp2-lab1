import os

def files():
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = f"{letter}.txt"
        with open(filename, 'w') as f:
            pass
        print(f" {filename}")

files()