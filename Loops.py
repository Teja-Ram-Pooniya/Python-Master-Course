# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:24:10 2023

@author: Teja Ram Pooniya
@program: Topic - Loops(if-else) in Python
@Description: 
    Loops and conditional statements (if-else) are fundamental constructs in programming. 
    
    For Loop:
        A for loop is used to iterate over a sequence (like a list, tuple, or range) 
        and execute a block of code for each element.
        ========================================================================
"""

# Example of a for loop
fruits = ['Apple', 'Banana', 'Cherry']
for fruit in fruits:
    print(fruit, "\n")
    
"""
================================================================================
    While Loop:
        A while loop repeatedly executes a block of code as long as a certain condition is true.
"""
count = 0
while count <= 11:
    print(count)
    count += 1
    
"""
================================================================================
If-Else Statement:
    An if statement is used to execute a block of code only if a certain condition is true. 
    An else statement can be added to specify what should happen if the condition is false.
"""

# Example of if-else statement
age = 18
if age >= 18:
    print("You are an adult.\n")
else:
    print("You are a minor.\n")

"""
================================================================================
Nested If-Else:
    You can also use nested if-else statements to create more complex conditions.
"""
# Example of nested if-else
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number.\n")
    else:
        print("Positive odd number.\n")
else:
    print("Non-positive number.\n")

"""
================================================================================
Loop Control Statements:
    Python also provides loop control statements like break and continue. 
    break is used to exit a loop prematurely, and continue is used to skip 
    the current iteration and move to the next one.
"""
# Example of loop control statements
for i in range(10):
    if i == 5:
        break  # Exit the loop when i reaches 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

"""
These constructs allow you to control the flow of your program based on conditions and to perform repetitive tasks efficiently using loops.
"""
