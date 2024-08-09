#!/usr/bin/env python3

number = int(input("Digite um número para ver a tabuada "))

print("Tabuada_do", number)
for i in range(11):
    result = number * i
    print(f"{number} x {i} = {result}")