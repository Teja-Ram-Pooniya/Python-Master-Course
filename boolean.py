# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:19:08 2023

@author: Teja Ram Pooniya
@Program: Topic: Boolean in Python How to Program
"""
"""
Description:
    Booleans in Python are a data type that represent the two truth values:
        True and False. Booleans are used to perform logical operations 
        and make decisions in your code.
        
        Booleans are essential for creating conditional logic in your code. 
        They are used in if statements, loops, and functions to 
        control program flow based on certain conditions.
    
"""
# Boolean values
is_true = True
is_false = False

# Comparisons
x = 5
y = 10
result = x < y  # result will be True

# Logical operators
logical_and = True and False  # result will be False
logical_or = True or False    # result will be True
logical_not = not True        # result will be False

# Conditional statements
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")

# Using booleans in loops
while is_true:
    print("This will keep running as long as is_true is True")
    is_true = False  # Change is_true to False to exit the loop

# Using booleans in functions
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # Output: True
print(is_even(7))   # Output: False
