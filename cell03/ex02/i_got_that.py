#!/usr/bin/env python3

while True:
        user_input = input("Digite algo (ou 'STOP' para parar): ")
        
        if user_input.upper() == "STOP":
            print("Parando o loop.")
            break
        
        print(f"Você digitou: {user_input}")