# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:16:32 2023

@author: Teja Ram Pooniya
@Program: Topic: String in Python How to Program
"""
"""
Description:
    
Certainly! Strings are a fundamental data type in Python that allow you to 
work with text data. They are used to represent sequences of characters and
 are defined using either single quotes ' ', double quotes " ", or
 triple quotes ''' ''' or """ """.
"""

# Creating strings
single_quoted = 'Hello, world!'
double_quoted = "Python programming"
triple_quoted = '''This is a multi-line
string using triple quotes.'''
escaped_chars = "Escaping characters like \"quotes\" and \\backslashes\\"

# String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

# String methods
text = "    Python is fun!    "
print(text.strip())  # Removes leading and trailing spaces
print(text.lower())  # Converts to lowercase
print(text.upper())  # Converts to uppercase
print(text.replace("fun", "awesome"))  # Replaces substring
print(text.startswith("Python"))  # Checks if string starts with given substring
print(text.endswith("awesome!"))  # Checks if string ends with given substring

# String formatting
age = 25
name = "Bob"
formatted_string = "My name is {} and I am {} years old.".format(name, age)
f_string = f"My name is {name} and I am {age} years old."

# String slicing
word = "Python"
print(word[0])      # Output: 'P'
print(word[1:4])    # Output: 'yth'
print(word[:2])     # Output: 'Py'
print(word[2:])     # Output: 'thon'
print(word[-1])     # Output: 'n'


