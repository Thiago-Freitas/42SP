#!/usr/bin/env python3
import sys
import re

def main():
    """Função principal que processa os argumentos e exibe o resultado."""
    # Verifica se o número de argumentos é exatamente 3 (nome do script + 2 argumentos)
    if len(sys.argv) != 3:
        print("none")
        return

    # Obtém os parâmetros
    keyword = sys.argv[1]
    text = sys.argv[2]

    # Cria uma expressão regular para encontrar todas as ocorrências da palavra-chave
    pattern = re.escape(keyword)
    matches = re.findall(pattern, text)
    
    # Conta o número de ocorrências
    count = len(matches)
    
    # Verifica se a palavra-chave apareceu pelo menos uma vez
    if count > 0:
        print(count)
    else:
        print("none")

if __name__ == "__main__":
    main()
