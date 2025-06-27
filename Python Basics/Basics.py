# python_basics_syntax_reference.py

# A concise reference for fundamental Python syntax and features.

# --- 1. Basics & Output ---
print("Hello, Python!") # Print statement


# --- 2. Variables & Data Types ---
# Dynamic typing: type inferred.
x = 5         # int: Whole numbers
y = 3.14      # float: Decimal numbers
name = "Ritik" # str: Text
is_student = True # bool: True/False (Capitalized)
none_val = None # NoneType: Represents absence of a value

print(f"Int: {x}, Float: {y}, String: {name}, Bool: {is_student}, None: {none_val}")


# --- 3. Operators ---
# Arithmetic
print(f"Add: {x + y}, Subtract: {x - y}, Multiply: {x * y}, Divide: {x / y}")
print(f"Floor Div (//): {x // y}, Modulus (%): {x % y}, Exponent (**): {x ** 2}")

# Comparison
print(f"x > y: {x > y}, x == 5: {x == 5}") # == for equality, = for assignment

# Logical (and, or, not)
print(f"True and False: {True and False}, True or False: {True or False}, not True: {not True}")

# Assignment
a = 10
a += 5 # a = a + 5
print(f"a after a += 5: {a}")


# --- 4. Data Structures ---

# Lists: Ordered, mutable, allows duplicates. [item1, item2]
my_list = [1, "apple", 3.0, True, 1]
print(f"List: {my_list}")
print(f"List element at index 0: {my_list[0]}") # Access by index
my_list.append("orange") # Add to end
my_list[1] = "banana" # Modify element
print(f"Modified List: {my_list}")
print(f"List slice [1:3]: {my_list[1:3]}") # Slicing (start:end-1)

# Tuples: Ordered, IMMUTABLE, allows duplicates. (item1, item2)
my_tuple = (1, "apple", 3.0, True, 1)
print(f"Tuple: {my_tuple}")
print(f"Tuple element at index 1: {my_tuple[1]}")
# my_tuple.append("orange") # This would cause an error (immutable)

# Sets: Unordered, mutable, NO DUPLICATES. {item1, item2}
my_set = {1, 2, 3, 2, 1} # Duplicates are automatically removed
print(f"Set: {my_set}")
my_set.add(4) # Add element
my_set.remove(2) # Remove element
print(f"Modified Set: {my_set}")

# Dictionaries: Unordered, mutable, key-value pairs, keys unique. {key: value}
my_dict = {"name": "Alice", "age": 20, "city": "Dallas"}
print(f"Dict: {my_dict}")
print(f"Dict value for 'name': {my_dict['name']}") # Access by key
my_dict["grade"] = "A" # Add/Update key
print(f"Modified Dict: {my_dict}")


# --- 5. Conditional Statements (if/elif/else) ---
temp = 25
if temp > 30:
    print("It's hot.")
elif temp > 20: # If first condition is False, try this.
    print("It's warm.")
else: # If all above are False.
    print("It's cool.")


# --- 6. Loops ---
# For Loop: Iterate over sequence.
for item in ["a", "b", "c"]:
    print(f"For loop item: {item}")
    
# Range: Generates a sequence of numbers.
for i in range(5): # 0 to 4
    print(f"Range loop i: {i}")
    
# Nested Loop: Loop inside another loop.
for i in range(2):
    for j in range(3):
        print(f"Nested loop i: {i}, j: {j}")
# For Loop with index: Use enumerate to get index and value.
for index, value in enumerate(["x", "y", "z"]):
    print(f"Enumerate loop index: {index}, value: {value}")
# For Loop with condition: Filter items.
for i in range(5):
    if i % 2 == 0: # Only even numbers
        print(f"Even number: {i}")
        
# For Loop with else: Executes after loop completes without break.
for i in range(3):
    print(f"For loop with else i: {i}")
    
else:
    print("For loop completed without break.")



# While Loop: Repeat as long as condition is true.
count = 0
while count < 2:
    print(f"While loop count: {count}")
    count += 1 # IMPORTANT: Must change condition or infinite loop!

# Loop control: break, continue
for i in range(5):
    if i == 2:
        continue # Skip current iteration, go to next
    if i == 4:
        break # Exit loop entirely
    print(f"Loop control i: {i}")


# --- 7. Functions ---
# Define with 'def'. 'return' sends value back.
def greet(person_name):
    return f"Hello, {person_name}!"

greeting = greet("Bob")
print(f"Function call: {greeting}")

# Parameters (positional, keyword, default)
def power(base, exp=2): # exp has a default value
    return base ** exp
print(f"Power (default): {power(3)}")
print(f"Power (custom exp): {power(3, 3)}")
print(f"Power (keyword args): {power(exp=4, base=2)}")

# Arbitrary Arguments (*args, **kwargs)
def func_args(*args): # Collects positional args into a tuple
    print(f"Args: {args}")
func_args(1, 2, 3)
#output: Args: (1, 2, 3)

def func_kwargs(**kwargs): # Collects keyword args into a dictionary
    print(f"Kwargs: {kwargs}")
func_kwargs(name="John", age=30)
#output: Kwargs: {'name': 'John', 'age': 30}


# --- 8. Classes & Objects (OOP) ---
# Blueprint for creating objects.
class Car:
    def __init__(self, make, model): # Constructor: initializes object state
        self.make = make # Instance variables
        self.model = model
    
    def display_info(self): # Method: function bound to an object
        return f"Car: {self.make} {self.model}"

my_car = Car("Toyota", "Camry") # Create object (instance)
print(f"Object method call: {my_car.display_info()}")


# --- 9. Exception Handling (try/except/finally) ---
# Gracefully handle errors.
try:
    result = 10 / 0 # Error
except ZeroDivisionError as e: # Catch specific error
    print(f"Caught Error: {e}")
except Exception as e: # Catch any other error
    print(f"Generic Error: {e}")
finally:
    print("Always runs (cleanup).")


# --- 10. File I/O ---
# Reading/writing files. 'with' ensures file is closed.
filename = "temp_notes.txt"
with open(filename, "w") as f: # 'w' for write (creates/overwrites)
    f.write("My first line.\n")
    f.write("My second line.")

with open(filename, "r") as f: # 'r' for read
    content = f.read()
print(f"File Content: '{content}'")




# --- 11. List Comprehensions ---
# Concise way to create lists. [expression for item in iterable if condition]
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
print(f"List Comprehension (squares): {squares}")


# --- 12. Lambda Functions ---
# Small, anonymous functions. Single expression.
add_nums = lambda a, b: a + b
print(f"Lambda add(7, 3): {add_nums(7, 3)}")


# --- 13. Decorators ---
# Modify or enhance functions/methods. @decorator_name
def logger(func):
    def wrapper(*args, **kwargs): # Wrapper function to log calls and arguments 
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
output = logger # Assign the decorator to a variable

@logger # Applies the 'logger' decorator to 'my_func'
def my_func(a, b):
    return a + b

print(f"Decorated function result: {my_func(5, 3)}")


# --- 14. Generators (yield) ---
# Functions that return an iterator, yielding values one by one (memory efficient).
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i # Pause execution, return value, resume later

gen_obj = even_numbers(6)
print(f"Generated evens: {list(gen_obj)}") # Convert to list to see all values


# --- 15. Modules & Packages ---
# Organizing code. 'import' brings modules into scope.
import math # Standard library module
print(f"math.pi: {math.pi}, math.sqrt(25): {math.sqrt(25)}")

from datetime import date # Import specific part
today = date.today()
print(f"Today's date: {today}")

# --- 16. Regular Expressions (re) ---
# Pattern matching in strings.
import re
text_data = "Phone: 123-456-7890, Email: test@example.com"
phone_pattern = r'\d{3}-\d{3}-\d{4}' # Regex for phone number
match = re.search(phone_pattern, text_data)
if match:
    print(f"Regex found phone: {match.group()}")


# --- 17. Context Managers (with statement) ---
# Resource management (e.g., files, locks). Ensures setup/teardown.
# Already demonstrated in File I/O with 'with open(...)'.


# --- 18. Type Hinting ---
# Optional annotations for types. Improves readability & tooling.
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result."""
    """Subtracts b from a and returns the result."""    
    return a - b

print(f"Type hinted subtract(10.5, 3.2): {subtract(10.5, 3.2)}")


# --- 19. Asynchronous Programming (async/await, asyncio) ---
# # Asynchronous programming allows concurrent execution of tasks.
# # Concurrency without threads. For I/O-bound tasks.

# Concurrency without threads. For I/O-bound tasks.
import asyncio

async def fetch_data(delay): # 'async def' defines a coroutine
    await asyncio.sleep(delay) # 'await' pauses execution, waits for result
    return f"Data after {delay} seconds"

async def main_async():
    print("Starting async operations...")
    data1 = await fetch_data(1) # Wait for 1 second
    data2 = await fetch_data(0.5) # Wait for 0.5 seconds
    print(f"Async Data: {data1}, {data2}")
    #output: Async Data: Data after 1 seconds, Data after 0.5 seconds

# asyncio.run(main_async()) # Run the top-level async function
# NOTE: Cannot run asyncio.run() directly in some environments (like interactive shells)
# You need to save this and run as a script.

print("Async section placeholder: Run this in a .py file: asyncio.run(main_async())")