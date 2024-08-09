#!/usr/bin/env python3

while True:
    number = input("Give me the first number: ")
    number1 = input("Give me the second number: ")

    try:
        number_int = int(number)
        number1_int = int(number1)
        print(f"The numbers entered are {number_int} and {number1_int}")
        break
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

print()

print("Thank you!")

# Verifica se o segundo número não é zero para evitar divisão por zero
if number1_int != 0:
    print(f"{number_int} + {number1_int} = {number_int + number1_int}")
    print(f"{number_int} - {number1_int} = {number_int - number1_int}")
    print(f"{number_int} / {number1_int} = {number_int / number1_int:.2f}")
    print(f"{number_int} * {number1_int} = {number_int * number1_int}")
else:
    print(f"{number_int} + {number1_int} = {number_int + number1_int}")
    print(f"{number_int} - {number1_int} = {number_int - number1_int}")
    print(f"{number_int} / {number1_int} = Undefined (division by zero)")
    print(f"{number_int} * {number1_int} = {number_int * number1_int}")
    
print()
