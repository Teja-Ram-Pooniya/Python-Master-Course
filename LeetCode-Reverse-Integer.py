# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 05:05:35 2023

@author: Teja Ram Pooniya
@Program: Leetcode - Practice Most Common Problems
@Topic: Reverse Integer

"""
# Python script to reverse an integer:

def reverse_integer(num):
    # Check if the number is negative
    negative = False
    if num < 0:
        negative = True
        num *= -1

    # Convert the number to a string and reverse it
    reversed_num = str(num)[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num)

    # Apply the negative sign if necessary
    if negative:
        reversed_num *= -1

    return reversed_num

# Test the function
num = 1234567891
reversed_num = reverse_integer(num)
print(f"The reverse of {num} is: {reversed_num}")

#In this script, we define a function called reverse_integer that takes an integer as input. The function first checks if the number is negative and stores this information. Then, it converts the number to a string and uses slicing ([::-1]) to reverse the string representation of the number. Finally, it converts the reversed string back to an integer and applies the negative sign if necessary. The reversed integer is then returned.

# You can test this script by providing different values for num.
