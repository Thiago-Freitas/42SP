#!/usr/bin/env python3

print()

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"{numbers}")

print()

new_numbers = [x + 2 for x in numbers]
new_numbers = {num + 2 for num in numbers if num > 5}

print(new_numbers)

print()