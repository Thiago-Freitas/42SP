#!/usr/bin/env python3

print()

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", numbers)

print()

new_numbers = [x + 2 for x in numbers]
filtered_numbers = [num for num in new_numbers if num > 5]

print("New array:", filtered_numbers)

print()