#!/usr/bin/env python3

while True:
    age = input("Please tell me your age: ")
    
    try:
        age_int = int(age)
        print(f"O número digitado é {age_int}")
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

print(f"You are currently {age} years old.")
print(f"In 10 years, you'll be {age_int + 10} years old.")
print(f"In 20 years, you'll be {age_int + 20} years old.")
print(f"In 30 years, you'll be {age_int + 30} years old.")

print()