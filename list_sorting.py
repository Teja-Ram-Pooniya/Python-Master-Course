# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:01:41 2023

@author: Teja Ram Pooniya
@Program: List in Python and Sorting That List to Sequencilly 
"""
# Generate a list of numbers
numbers = [5, 2, 8, 1, 9, 3, 6, 4, 7]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print(sorted_numbers)
names = ["Carlos", "Ray", "Teja", "Aditya"]
print(names)

# Sorted by Alphabets
print(sorted(names))

# Sorted with length Use key=len
print(sorted(names, key=len))
