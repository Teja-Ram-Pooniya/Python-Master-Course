# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:06:46 2023

@author: Teja Ram Pooniya
@Program: Topic: List in Python How to Program
"""

# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Accessing list items
print(fruits[0])  # Output: 'apple'

# Modifying list items
fruits[1] = 'grape'

# Adding items to a list
fruits.append('orange')
fruits.insert(1, 'kiwi')  # Inserts 'kiwi' at index 1

# Removing items from a list
fruits.remove('cherry')
popped_item = fruits.pop()  # Removes and returns the last item

# Checking item existence
if 'apple' in fruits:
    print("Apple is in the list.")

# Looping through a list
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
