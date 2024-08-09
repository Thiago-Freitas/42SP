#!/usr/bin/env python3
import sys

def main():
    """Função principal que processa os argumentos e interage com o usuário."""
    # Verifica se o número de argumentos é exatamente 2 (nome do script + 1 argumento)
    if len(sys.argv) != 2:
        print("none")
        return

    # Obtém o parâmetro passado
    expected_word = sys.argv[1]

    # Solicita ao usuário que digite uma palavra
    user_input = input("Enter a word: ")

    # Compara a palavra digitada com o parâmetro passado
    if user_input == expected_word:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()