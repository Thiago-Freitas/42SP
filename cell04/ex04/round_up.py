#!/usr/bin/env python3

import math

while True:
    try:
        number = float(input("Give me a number: "))
        
        rounded_up = math.ceil(number)
        
        print(f"The number rounded up is: {rounded_up}")
        
        break

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
