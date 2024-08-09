#!/usr/bin/env python3
import sys

def main():
    
    args = sys.argv[1:]

    if not args:
        print("none")
        return

    for arg in args:
        # Verifica se o argumento não termina com 'ism'
        if not arg.endswith("ism"):
            print(f"{arg}ism")

if __name__ == "__main__":
    main()
