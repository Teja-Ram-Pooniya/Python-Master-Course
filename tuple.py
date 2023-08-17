# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:13:02 2023

@author: Teja Ram Pooniya
@Program: Topic: Tuple in Python How to Program
"""
"""
Description:
    Certainly! A tuple is another fundamental data structure in Python.
    Tuples are similar to lists, but unlike lists, they are immutable, 
    meaning their values cannot be changed after creation. 
    Tuples are often used to group related data together and are defined using parentheses ().
"""
# Creating a tuple
coordinates = (3, 5)

# Accessing tuple elements
x = coordinates[0]
y = coordinates[1]
print("x:", x, "y:", y)  # Output: x: 3 y: 5

# Nested tuples
point = ((1, 2), (3, 4))
print(point[0])  # Output: (1, 2)

# Tuple unpacking
x, y = coordinates
print("x:", x, "y:", y)  # Output: x: 3 y: 5

# Using tuples in functions
def get_coordinates():
    return 7, 9

new_x, new_y = get_coordinates()
print("New x:", new_x, "New y:", new_y)  # Output: New x: 7 New y: 9

# Looping through a tuple
for coordinate in coordinates:
    print(coordinate)

