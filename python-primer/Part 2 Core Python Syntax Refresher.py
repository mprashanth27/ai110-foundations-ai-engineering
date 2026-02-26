'''#Problem 1: Type Reassignment
x = 10
x = "ten"
x = 10.5
print(type(x))  # Output: <class 'float'>

#Problem 2: Function Behavior with Different Types
def add_value(a, b):
    print(a + b)

add_value(3, 4) # Output: 7
add_value("3", "4") # Output: 34
add_value(3, "4") # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Problem 3: Type Checking at Runtime
def check_type(value):
    if value.isdigit():
        value = int(value)
    else:
        value = float(value)

    print(type(value))

check_type("10") # Output: <class 'int'>
check_type("10.5") # Output: <class 'float'>'''

# Write a snippet that catches a divide-by-zero error.
def divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
divide(10, 2) # Output: 5.0
divide(10, 0) # Output: Error: Cannot divide by zero.

from random import random
print(random.randint(1, 50))