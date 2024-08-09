#!/usr/bin/env python3

number = int(input("Digite um número: "))
number2 = int(input("Digite outro número: "))
result = number * number2

print(number, "x", number2, "=", result)

if result < 0:
    print("The result is negative.")

elif result > 0:
    print("The result is positive.")

else:
    print("The result is positive and negative.")