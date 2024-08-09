#!/usr/bin/env python3
import sys

def main():
    
    args = sys.argv[1:]

    # Verifica se há argumentos
    if not args:
        print("none")
    else:
        # Exibe o número de parâmetros
        print(f"parameters: {len(args)}")

        # Exibe cada parâmetro e seu comprimento
        for arg in args:
            print(f"{arg} {len(arg)}")

if __name__ == "__main__":
    main()
