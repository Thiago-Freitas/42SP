#!/usr/bin/env python3
import sys

def main():
    
    args = sys.argv[1:]

    if len(args) != 2:
        print("none")
        return

    try:
        # Convert arguments to integers
        start = int(args[0])
        end = int(args[1])
        
        # Create a range and convert it to a list
        result = list(range(start, end + 1))
        
        # Print the list
        print(result)
    except ValueError:
        # Handle the case where conversion to integer fails
        print("none")

if __name__ == "__main__":
    main()