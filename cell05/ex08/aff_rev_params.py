#!/usr/bin/env python3
import sys

if len(sys.argv) > 2:

    parameters = sys.argv[1:]
    
    reversed_parameters = parameters[::-1]
    
    for param in reversed_parameters:
        print(param)
else:
    # Imprime "none" se houver menos de dois parâmetros
    print("none")