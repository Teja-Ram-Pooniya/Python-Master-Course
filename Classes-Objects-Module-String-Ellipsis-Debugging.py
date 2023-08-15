# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:12:36 2023

@author: Teja Ram Pooniya
@Programming-Topic: Python Learn classes, modules, Str(String), Ellipsis Object, Numm Object, Ellipsis Debug
"""

"""
Overview of these concepts in Python:

Sure, I can provide you with an overview of these concepts in Python:

1. Classes and Objects:
   - **Classes:** A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects of the class will have.
   - **Objects:** Objects are instances of a class. They can hold data and perform actions defined by the class's methods.

2. Modules:
   - A module is a Python file containing functions, classes, and variables. It's a way to organize code into reusable components.
   - Modules can be imported into other Python scripts to use the code defined in them.

3. Strings (`str`):
   - Strings are sequences of characters enclosed in single (`'`) or double (`"`) quotes.
   - They are used to represent and manipulate textual data.
   - String methods allow you to perform various operations on strings.

4. Ellipsis (`...`) Object:
   - The ellipsis object is a placeholder in Python. It doesn't do anything on its own.
   - It can be used in slices or function signatures to indicate that something is missing or truncated.

5. `None` Object:
   - `None` is a special object in Python used to represent the absence of a value.
   - It is often used as a default return value for functions that don't explicitly return anything.
   - It's similar to `null` or `nil` in other programming languages.

6. Debugging with Ellipsis (`...`):
   - In some debuggers and development environments, `...` can be used as a placeholder to indicate breakpoints or to allow code execution to stop at a certain point.
   - It's often used as a marker to indicate where debugging should pause.

If you'd like more detailed explanations or code examples for any of these concepts, feel free to ask!


"""

# Absolutely, let's dive into more detailed explanations and examples for each of the topics:

### Classes and Objects:

# **Example: Creating a Class and Objects**

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

print(car1.make, car1.model)  # Output: Toyota Camry
print(car2.make, car2.model)  # Output: Ford Mustang
print("\n")


### Modules:

# Example: Creating and Importing a Module
# 1. Create a file named `my_module.py`:

def greet(name):
    return f"Hello, {name}!"

# 2. In another Python file, import and use the module:

import my_module

message = my_module.greet("Alice")
print(message)  # Output: Hello, Alice!


# Strings (`str`):

# Example: String Manipulation

text = "Python Programming"
print(text.upper())    # Output: PYTHON PROGRAMMING
print(text.lower())    # Output: python programming
print(text.startswith("Py"))  # Output: True
print(text.replace("Programming", "Language"))  # Output: Python Language


### Ellipsis (`...`) Object:

# Example: Using Ellipsis in Slices

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
partial_list = numbers[::2]  # Get every second element
print(partial_list)  # Output: [1, 3, 5, 7, 9]


### `None` Object:

# Example: Using `None` as Default Return Value

def find_element(elements, target):
    for element in elements:
        if element == target:
            return element
    return None

result = find_element([10, 20, 30, 40], 25)
if result is None:
    print("Element not found.")
else:
    print("Element found:", result)


### Debugging with Ellipsis (`...`):

# Example: Debugging with a Breakpoint Marker

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    breakpoint()  # Debugger stops here
    average = total / count
    return average

data = [10, 20, 30, 40]
average_result = calculate_average(data)
print("Average:", average_result)


# These examples should provide you with a clearer understanding of each concept and how they can be used in Python programming.
