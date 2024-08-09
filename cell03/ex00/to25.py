#!/usr/bin/env python3

number = int(input("Digite um número menor que 25: "))

if number < 25:

    while number <= 25:
        print(number)
        number += 1
else:
    print("Error")


