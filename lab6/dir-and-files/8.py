import os

def file(file_path):    
    os.remove(file_path)
    print(f"File '{file_path}' deleted ")

file_path = '3.txt'
file(file_path)
