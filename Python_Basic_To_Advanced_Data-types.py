# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 07:50:09 2023

@author: Teja Ram Pooniya
@Programming-Topic: Python Basic and Advanced Data-types
"""

"""
Python has several built-in data types that are fundamental for programming. Here are some of the most common ones:

1. Integers (int): Represents whole numbers. For example: 42, -7, 0.

2. Floating-Point Numbers (float): Represents decimal numbers. For example: 3.14, -0.5, 1.0.

3. Strings (str): Represents sequences of characters. Enclosed in single (') or double (") quotes. For example: 'hello', "Python".

4. Booleans (bool): Represents the truth values True or False. Often used for logical operations. For example: True, False.

5. Lists (list): Ordered collections of items, which can be of different data types. Defined using square brackets []. For example: [1, 2, 3], ['apple', 'banana', 'cherry'].

6. Tuples (tuple): Similar to lists, but immutable (cannot be changed after creation). Defined using parentheses (). For example: (1, 2, 3), ('red', 'green', 'blue').

7. Sets (set): Unordered collections of unique items. Defined using curly braces {}. For example: {1, 2, 3}, {'apple', 'banana', 'cherry'}.

8. Dictionaries (dict): Unordered collections of key-value pairs. Defined using curly braces {} with colons separating keys and values. For example: {'name': 'John', 'age': 30}.

9. NoneType (None): Represents the absence of a value or a null value. Often used as a default value or to indicate the absence of a return value from a function.

10. Bytes (bytes) and Byte Arrays (bytearray): Used to represent sequences of bytes (integers from 0 to 255). Bytes are immutable, while byte arrays are mutable.

11. Ranges (range): Represents an immutable sequence of numbers. Used in loops and iterations.

12. Complex Numbers (complex): Represents numbers with both real and imaginary parts. For example: 3 + 2j, -1 - 4j.

These are some of the most commonly used built-in data types in Python. Each data type has its own properties, methods, and use cases. Understanding and effectively using these data types is essential for effective programming in Python.
"""

# Built-in Data-Types
# 1. Integer(int)
x = 42
y = -7
z = 0
print(x)
print(y)
print(z)
print("\n")

# 2. Floating-Point Numbers (float):
pi = 3.14
temperature = -0.5
percentage = 1.0
print("Pi ki value in float: ", pi)
print("Temperature ki value also float: ", temperature)
print("percentage ki value also float: ", percentage)
print("\n")

# 3. Strings (str):
greeting = 'hello'
language = "Python"
print(greeting + " " + language)
print("\n")

# 4. Booleans (bool):
is_valid = True
has_permission = False
print(is_valid)
print(has_permission)
print("\n")

# 5. Lists (list):
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']
print("numbers list: ", numbers)
print("fruits list: ", fruits)
print("\n")

# 6. Tuples (tuple):
point = (3, 5)
colors = ('red', 'green', 'blue')
print("Tuple Points: ", point)
print("Tuple Colors: ", colors)
print("\n")

# 7. Sets (set):
unique_numbers = {1, 2, 3, 4, 5}
unique_fruits = {'apple', 'banana', 'cherry'}
print("Sets Unique Numbers: ", unique_numbers)
print("Sets Unique Fruits: ", unique_fruits)
print("\n")

# 8. Dictionaries (dict):
person = {'name': 'John', 'age': 30, 'country': 'USA'}
print("Dictionaries (dict): Person: \n", person)
print("\n")

# 9. NoneType (None):
result = None
print(result)
print("\n")

# 10. Bytes (bytes) and Byte Arrays (bytearray):
binary_data = b'\x48\x65\x6c\x6c\x6f'
byte_array = bytearray(b'Python')
print(binary_data)
print(byte_array)
print("\n")

# 11. Ranges (range):
numbers_range = range(1, 6)  # Represents [1, 2, 3, 4, 5]
print(numbers_range)
print("\n")

# 12. Complex Numbers (complex):
complex_num = 3 + 2j
another_complex = -1 - 4j
print(complex_num)
print(another_complex)
print("\n")


# 13. Bytes and Byte Literals (bytes, b prefix): Used to represent sequences of bytes, often used for binary data or working with files.
binary_data = b'\x48\x65\x6c\x6c\x6f'  # Represents the bytes 'Hello'
print(binary_data)




# 14. Byte Arrays (bytearray): Mutable version of the bytes type, allowing modification of individual elements.
byte_array = bytearray(b'Python')
byte_array[0] = ord('J')  # Change 'P' to 'J'
print(byte_array)




# 15. Enumerations (enum.Enum): A way to define named constant values. Useful for improving code readability and maintainability.
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3



# 16. Frozen Sets (frozenset): An immutable version of the set data type. Useful for keys in dictionaries or elements in other sets.
frozen_colors = frozenset(['red', 'green', 'blue'])
print(frozen_colors)




# 17. Memory Views (memoryview): Allows access to the internal buffer of an object (like a bytes object) without copying the data.
# Memory Views
data = b'Hello'
mem_view = memoryview(data)
print(mem_view)




# 18. Type Conversion (int(), float(), str(), etc.): Functions to convert between different data types.
# convert string to integer
num_str = "42"
num_int = int(num_str)  # Convert string to integer
print("Integer Value: ", num_int)





# 19. Type Checking (isinstance(), type()): Functions to check the type of an object.
value = 42
if isinstance(value, int):
    print("It's an integer!")
    
    
    

# 20. Type Annotations (typing module): Allows adding hints about the expected data types for function arguments and return values.
from typing import List

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)




# 21. slice Ellipsis
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("My List: ", my_list)
slice_ellipsis = my_list[::3]  # Select every second element
print("Slice Ellipsis Select Every second element: ", slice_ellipsis)

# Bonus for Advanced Concepts in Real-Life Security Software Industry Used for Specific Purpose.
"""

Question:
Security Product based company: used basic data types for what purpose

Answer:
Security product-based companies use basic data types in Python (and other programming languages) for various purposes within their software and systems. Here's how they might use these data types:

1. Integers (int): Integers are used for various purposes in security software, such as:

2. Indexing and counting operations in data structures.
   > Representing IDs, timestamps, version numbers, and other numeric identifiers.
   > Encryption and decryption algorithms that work with integer-based mathematical operations.
   > Floating-Point Numbers (float): Floating-point numbers can be used for:

3. Calculations involving real-world values like measurements and sensor data.
   > Implementing algorithms that require precise decimal representation.
   > Certain cryptographic and mathematical operations.
   > Strings (str): Strings are essential for:

4. Storing and manipulating textual data, including configuration settings.
   > Logging, error messages, and user interaction.
   > Encoding and decoding data in various formats.
   > Booleans (bool): Booleans are used for:

5. Implementing decision-making logic in security protocols and algorithms.
   > Enabling or disabling certain features or security mechanisms.
   > Expressing conditions in access control rules and permission checks.
   > Lists (list), Tuples (tuple), Sets (set): These data types are used for:

6. Storing collections of data such as IP addresses, URLs, or file paths.
   > Maintaining lists of rules, configurations, or patterns.
   > Iterating over items during data analysis or processing.
   > Dictionaries (dict): Dictionaries are employed for:

7. Storing key-value pairs of configuration settings and metadata.
   > Building data structures for fast lookups in security databases.
   > Representing headers and attributes in various network protocols.
   > NoneType (None): None can be used for:

8. Indicating the absence of a value, such as when a resource isn't found.
   > Initializing variables that need to be set later within the code.
   > As a placeholder for a return value from a function that doesn't explicitly return anything.
   > Bytes (bytes) and Byte Arrays (bytearray): These data types are used for:

9. Handling binary data in encryption and decryption processes.
   > Reading and writing data to and from files and network streams.
   > Working with raw data that needs to be manipulated bit by bit.
   > Ranges (range): Ranges may be used for:

10 Generating sequences of numbers used in loops and iterations.
   > Defining numeric boundaries for specific security checks or evaluations.
   > Complex Numbers (complex): While less common in security applications, complex numbers could be used for:

Certain mathematical operations that involve both real and imaginary components.
In the context of security software, these basic data types play a crucial role in representing, processing, and securing various types of information and interactions.
"""
