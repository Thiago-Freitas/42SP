#!/usr/bin/env python3

while True:
    try:
        number_float = float(input("Give me a number: "))

        if number_float.is_integer():
            print(f"This number is an integer: {int(number_float)}")
        else:
            print(f"This number is a decimal: {number_float}")

        break

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
