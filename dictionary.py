# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:08:51 2023

@author: Teja Ram Pooniya
@Program: Topic: Dictionary in Python How to Program
"""
"""
Discription: 
    Dictionaries:
A dictionary is an unordered collection of key-value pairs. Each key must be unique, 
and keys are used to access corresponding values. 
Dictionaries are defined using curly braces {}.
"""

# Creating a dictionary
person = {
    'name': 'Teja',
    'age': 34,
    'city': 'Jodhpur'
}

# Accessing dictionary values
print(person['name'])  # Output: 'John'

# Modifying dictionary values
person['age'] = 31

# Adding new key-value pairs
person['occupation'] = 'developer'

# Removing key-value pairs
del person['city']

# Checking key existence
if 'name' in person:
    print("Name exists in the dictionary.")

# Looping through dictionary keys
for key in person:
    print(key, person[key])

# Looping through dictionary items (key-value pairs)
for key, value in person.items():
    print(key, value)
