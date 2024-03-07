import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# Sample input
number = float(input())
milliseconds = int(input())
calculate_square_root(number, milliseconds)
