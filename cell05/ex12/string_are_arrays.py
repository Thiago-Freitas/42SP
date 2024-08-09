#!/usr/bin/env python3
import sys

def main():
    
    if len(sys.argv) != 2:
        print("none")
        return

    input_string = sys.argv[1]

    count_z = input_string.count('z')

    if count_z > 0:
        print('z' * count_z)
    else:
        print("none")

if __name__ == "__main__":
    main()