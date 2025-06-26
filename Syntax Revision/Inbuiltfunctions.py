# inbuilt_functions_learning.py

# This file demonstrates common inbuilt functions for core Python data types.
# Each section shows a data type, its common inbuilt methods, and the resulting state.

# --- 1. Strings ---
print("--- Strings ---")
my_string = "Hello, Ritik Yadav! You are learning Python."
print(f"Original String: '{my_string}'")

# len(): Returns the length of the string.
length = len(my_string)
print(f"  Length (len()): {length}")

# .upper(): Returns a new string with all characters in uppercase.
upper_string = my_string.upper()
print(f"  Uppercase (.upper()): '{upper_string}'")

# .lower(): Returns a new string with all characters in lowercase.
lower_string = my_string.lower()
print(f"  Lowercase (.lower()): '{lower_string}'")

# .capitalize(): Returns a new string with the first character capitalized and the rest lowercase.
capitalized_string = my_string.capitalize()
print(f"  Capitalized (.capitalize()): '{capitalized_string}'")

# .title(): Returns a new string where the first letter of each word is capitalized.
title_string = my_string.title()
print(f"  Title Case (.title()): '{title_string}'")

# .strip(): Returns a new string with leading/trailing whitespace removed.
whitespace_string = "   Hello World   "
stripped_string = whitespace_string.strip()
print(f"  Stripped ('{whitespace_string}' -> .strip()): '{stripped_string}'")

# .replace(old, new): Returns a new string with all occurrences of 'old' replaced by 'new'.
replaced_string = my_string.replace("Python", "programming")
print(f"  Replaced ('Python' with 'programming'): '{replaced_string}'")

# .split(delimiter): Splits the string by the given delimiter and returns a list of substrings.
split_list = my_string.split(" ") # Split by space
print(f"  Split by space (.split(' ')): {split_list}")
split_comma = "apple,banana,orange".split(",")
print(f"  Split by comma ('apple,banana,orange'.split(',')): {split_comma}")

# .join(iterable): Concatenates elements of an iterable (like a list of strings) using the string as a separator.
joined_string = "-".join(["learn", "python", "fast"])
print(f"  Joined ('.'.join(['learn', 'python', 'fast'])): '{joined_string}'")

# .startswith(prefix): Checks if the string starts with the specified prefix.
starts_with_hello = my_string.startswith("Hello")
print(f"  Starts with 'Hello' (.startswith('Hello')): {starts_with_hello}")

# .endswith(suffix): Checks if the string ends with the specified suffix.
ends_with_python = my_string.endswith("Python.")
print(f"  Ends with 'Python.' (.endswith('Python.')): {ends_with_python}")

# .find(substring): Returns the lowest index of the substring if found, -1 otherwise.
find_ritik = my_string.find("Ritik")
print(f"  Find 'Ritik' (.find('Ritik')): {find_ritik}")
find_nonexistent = my_string.find("Java")
print(f"  Find 'Java' (.find('Java')): {find_nonexistent}")

# .count(substring): Returns the number of non-overlapping occurrences of substring.
count_l = my_string.count("l")
print(f"  Count 'l' (.count('l')): {count_l}")

# .isdigit(), .isalpha(), .isalnum(), .isspace(), .islower(), .isupper():
# Check character properties. Return True if all characters in the string satisfy the condition, False otherwise.
print(f"  '123'.isdigit(): {'123'.isdigit()}")
print(f"  'abc'.isalpha(): {'abc'.isalpha()}")
print(f"  'ab12'.isalnum(): {'ab12'.isalnum()}")
print(f"  ' '.isspace(): {' '.isspace()}")
print(f"  'hello'.islower(): {'hello'.islower()}")
print(f"  'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"  'Hello'.islower(): {'Hello'.islower()}") # False


# --- 2. Lists ---
print("\n--- Lists ---")
my_list = [10, 20, 30, 40, 50]
print(f"Original List: {my_list}")

# len(): Returns the number of items in the list.
length_list = len(my_list)
print(f"  Length (len()): {length_list}")

# .append(element): Adds an element to the end of the list. Modifies in place.
my_list.append(60)
print(f"  After .append(60): {my_list}")

# .insert(index, element): Inserts an element at a specific index. Modifies in place.
my_list.insert(2, 25) # Insert 25 at index 2
print(f"  After .insert(2, 25): {my_list}")

# .remove(value): Removes the first occurrence of a specified value. Raises ValueError if not found. Modifies in place.
my_list.remove(40)
print(f"  After .remove(40): {my_list}")

# .pop(index=-1): Removes and returns the item at the given index (default last). Modifies in place.
popped_item = my_list.pop() # Remove last
print(f"  After .pop() (removed: {popped_item}): {my_list}")
popped_item_at_index = my_list.pop(0) # Remove first
print(f"  After .pop(0) (removed: {popped_item_at_index}): {my_list}")

# .extend(iterable): Adds all elements of an iterable (like another list) to the end. Modifies in place.
my_list.extend([70, 80])
print(f"  After .extend([70, 80]): {my_list}")

# .index(value, start=0, end=len()): Returns the index of the first occurrence of a value. Raises ValueError if not found.
index_of_30 = my_list.index(30)
print(f"  Index of 30 (.index(30)): {index_of_30}")

# .count(value): Returns the number of times a specified value occurs in the list.
count_25 = my_list.count(25)
print(f"  Count of 25 (.count(25)): {count_25}")
my_list.append(25)
count_25_new = my_list.count(25)
print(f"  After appending 25, count of 25: {count_25_new}")


# .sort(key=None, reverse=False): Sorts the list in ascending order by default. Modifies in place.
# For numerical lists, sorts numerically. For strings, sorts alphabetically.
unsorted_list = [5, 1, 4, 2, 8]
unsorted_list.sort()
print(f"  Sorted (ascending) [5,1,4,2,8] -> .sort(): {unsorted_list}")

unsorted_list_reverse = [5, 1, 4, 2, 8]
unsorted_list_reverse.sort(reverse=True)
print(f"  Sorted (descending) [5,1,4,2,8] -> .sort(reverse=True): {unsorted_list_reverse}")

# .reverse(): Reverses the order of elements in the list. Modifies in place.
rev_list = [1, 2, 3, 4, 5]
rev_list.reverse()
print(f"  Reversed [1,2,3,4,5] -> .reverse(): {rev_list}")

# .copy(): Returns a shallow copy of the list.
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(f"  Original list after copy and modification of copy: {original}")
print(f"  Copied list after modification: {copied}")

# .clear(): Removes all items from the list. Modifies in place.
cleared_list = [1, 2, 3]
cleared_list.clear()
print(f"  After .clear(): {cleared_list}")


# --- 3. Tuples ---
print("\n--- Tuples ---")
my_tuple = (10, 20, 30, 20, 40)
print(f"Original Tuple: {my_tuple}")

# Tuples are immutable, so they have fewer methods.

# len(): Returns the number of items in the tuple.
length_tuple = len(my_tuple)
print(f"  Length (len()): {length_tuple}")

# .index(value, start=0, end=len()): Returns the index of the first occurrence of a value.
index_of_30_tuple = my_tuple.index(30)
print(f"  Index of 30 (.index(30)): {index_of_30_tuple}")

# .count(value): Returns the number of times a specified value occurs in the tuple.
count_20_tuple = my_tuple.count(20)
print(f"  Count of 20 (.count(20)): {count_20_tuple}")


# --- 4. Sets ---
print("\n--- Sets ---")
my_set = {10, 20, 30, 40}
print(f"Original Set: {my_set}")

# len(): Returns the number of items in the set.
length_set = len(my_set)
print(f"  Length (len()): {length_set}")

# .add(element): Adds an element to the set. Does nothing if the element is already present. Modifies in place.
my_set.add(50)
print(f"  After .add(50): {my_set}")
my_set.add(10) # Adding an existing element
print(f"  After .add(10) (no change): {my_set}")

# .remove(element): Removes an element. Raises KeyError if the element is not found. Modifies in place.
try:
    my_set.remove(20)
    print(f"  After .remove(20): {my_set}")
except KeyError:
    print("  Element not found for .remove()")

# .discard(element): Removes an element if present. Does nothing if the element is not found. Modifies in place.
my_set.discard(30)
print(f"  After .discard(30): {my_set}")
my_set.discard(99) # Discarding a non-existent element
print(f"  After .discard(99) (no change): {my_set}")

# .union(other_set): Returns a new set containing all unique elements from both sets.
set_b = {40, 50, 60}
union_set = my_set.union(set_b)
print(f"  Union with {{40, 50, 60}} (.union()): {union_set}")

# .intersection(other_set): Returns a new set containing elements common to both sets.
intersection_set = my_set.intersection(set_b)
print(f"  Intersection with {{40, 50, 60}} (.intersection()): {intersection_set}")

# .difference(other_set): Returns a new set containing elements in the first set but not in the second.
difference_set = my_set.difference(set_b)
print(f"  Difference with {{40, 50, 60}} (.difference()): {difference_set}")

# .issubset(other_set): Returns True if all elements of the set are in the other set.
is_subset = {10, 50}.issubset(my_set)
print(f"  Is {{10, 50}} a subset of my_set? (.issubset()): {is_subset}")

# .issuperset(other_set): Returns True if all elements of the other set are in the set.
is_superset = my_set.issuperset({10, 50})
print(f"  Is my_set a superset of {{10, 50}}? (.issuperset()): {is_superset}")

# .isdisjoint(other_set): Returns True if the sets have no common elements.
is_disjoint = my_set.isdisjoint({90, 100})
print(f"  Is my_set disjoint with {{90, 100}}? (.isdisjoint()): {is_disjoint}")

# .update(iterable): Adds elements from an iterable to the set. (like |= operator)
my_set.update({70, 80})
print(f"  After .update({{70, 80}}): {my_set}")

# .intersection_update(iterable): Updates the set with the intersection of itself and another iterable. (like &= operator)
my_set_int_update = {1, 2, 3, 4, 5}
my_set_int_update.intersection_update({3, 4, 5, 6, 7})
print(f"  Intersection Update of {{1,2,3,4,5}} with {{3,4,5,6,7}}: {my_set_int_update}")

# .difference_update(iterable): Updates the set by removing elements found in another iterable. (like -= operator)
my_set_diff_update = {1, 2, 3, 4, 5}
my_set_diff_update.difference_update({3, 4, 6})
print(f"  Difference Update of {{1,2,3,4,5}} with {{3,4,6}}: {my_set_diff_update}")

# .symmetric_difference(other_set): Returns a new set with elements in either set but not in both.
sym_diff_set = {1, 2, 3}.symmetric_difference({3, 4, 5})
print(f"  Symmetric Difference of {{1,2,3}} and {{3,4,5}}: {sym_diff_set}")

# .symmetric_difference_update(iterable): Updates the set with the symmetric difference. (like ^= operator)
my_set_sym_diff_update = {1, 2, 3, 4}
my_set_sym_diff_update.symmetric_difference_update({3, 4, 5, 6})
print(f"  Symmetric Difference Update of {{1,2,3,4}} with {{3,4,5,6}}: {my_set_sym_diff_update}")


# .pop(): Removes and returns an arbitrary element from the set. Raises KeyError if set is empty.
try:
    popped_set_item = my_set.pop()
    print(f"  Popped item from set: {popped_set_item}. Remaining set: {my_set}")
except KeyError:
    print("  Set is empty, cannot pop.")

# .clear(): Removes all elements from the set. Modifies in place.
cleared_set = {1, 2, 3}
cleared_set.clear()
print(f"  After .clear(): {cleared_set}")


# --- 5. Dictionaries ---
print("\n--- Dictionaries ---")
my_dict = {"name": "Ritik", "age": 22, "city": "Dallas"}
print(f"Original Dictionary: {my_dict}")

# len(): Returns the number of key-value pairs in the dictionary.
length_dict = len(my_dict)
print(f"  Length (len()): {length_dict}")

# .keys(): Returns a view object that displays a list of all keys.
dict_keys = my_dict.keys()
print(f"  Keys (.keys()): {list(dict_keys)}") # Convert to list for clear printing

# .values(): Returns a view object that displays a list of all values.
dict_values = my_dict.values()
print(f"  Values (.values()): {list(dict_values)}") # Convert to list for clear printing

# .items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
dict_items = my_dict.items()
print(f"  Items (.items()): {list(dict_items)}") # Convert to list for clear printing

# .get(key, default=None): Returns the value for the specified key. If key is not found, returns default (or None).
name = my_dict.get("name")
print(f"  Get 'name' (.get('name')): {name}")
country = my_dict.get("country", "USA") # Using a default value
print(f"  Get 'country' (.get('country', 'USA')): {country}")

# .pop(key, default=NoDefault): Removes the specified key and returns its value. If key not found, raises KeyError or returns default.
popped_value = my_dict.pop("age")
print(f"  After .pop('age') (removed: {popped_value}): {my_dict}")
try:
    my_dict.pop("non_existent_key")
except KeyError:
    print("  Tried to pop non-existent key, caught KeyError.")

# .popitem(): Removes and returns an arbitrary (key, value) pair. Raises KeyError if dict is empty.
popped_item_dict = my_dict.popitem()
print(f"  After .popitem() (removed: {popped_item_dict}): {my_dict}")

# .update(iterable or dictionary): Updates the dictionary with elements from another dictionary or iterable of key-value pairs.
my_dict.update({"profession": "Engineer", "city": "Richardson"}) # Update city, add profession
print(f"  After .update({{profession: 'Engineer', city: 'Richardson'}}): {my_dict}")

# .clear(): Removes all items from the dictionary. Modifies in place.
cleared_dict = {"a": 1, "b": 2}
cleared_dict.clear()
print(f"  After .clear(): {cleared_dict}")

# .copy(): Returns a shallow copy of the dictionary.
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
copied_dict["c"] = 3
print(f"  Original dict after copy and modification of copy: {original_dict}")
print(f"  Copied dict after modification: {copied_dict}")

# .setdefault(key, default=None): Returns the value of the specified key. If the key does not exist, insert the key with the specified default value.
my_dict_set_default = {"a": 1}
value_a = my_dict_set_default.setdefault("a", 100) # Key 'a' exists, value won't change
value_b = my_dict_set_default.setdefault("b", 200) # Key 'b' doesn't exist, will be added
print(f"  .setdefault('a', 100) -> Value: {value_a}, Dict: {my_dict_set_default}")
print(f"  .setdefault('b', 200) -> Value: {value_b}, Dict: {my_dict_set_default}")

# .fromkeys(iterable, value=None): Creates a new dictionary with keys from iterable and values set to 'value'.
new_dict_from_keys = dict.fromkeys(["key1", "key2", "key3"], 0)
print(f"  dict.fromkeys(['key1', 'key2'], 0): {new_dict_from_keys}")


# --- 6. Common Inbuilt Functions (Not tied to a specific object type) ---
print("\n--- Common Inbuilt Functions ---")

# print(): Outputs to the console.
print("  This is output from print().")

# type(): Returns the type of an object.
print(f"  Type of my_list: {type(my_list)}")
print(f"  Type of my_string: {type(my_string)}")

# len(): (Already covered for specific types, but generally applicable to anything with a length).
print(f"  len('abc'): {len('abc')}")

# int(), float(), str(), bool(): Type conversion functions.
int_from_str = int("123")
print(f"  int('123'): {int_from_str}")
float_from_int = float(10)
print(f"  float(10): {float_from_int}")
str_from_int = str(456)
print(f"  str(456): '{str_from_int}'")
bool_from_int = bool(0) # 0 is False, any non-zero is True
print(f"  bool(0): {bool_from_int}")
bool_from_empty_list = bool([]) # Empty collections are False
print(f"  bool([]): {bool_from_empty_list}")

# min(), max(): Returns the smallest/largest item in an iterable.
numbers = [1, 5, 2, 8, 3]
print(f"  min({numbers}): {min(numbers)}")
print(f"  max({numbers}): {max(numbers)}")

# sum(): Sums the items of an iterable.
print(f"  sum({numbers}): {sum(numbers)}")

# sorted(): Returns a new sorted list from the items in an iterable. Does not modify original.
unsorted = [5, 1, 4, 2, 8]
sorted_list = sorted(unsorted)
print(f"  sorted({unsorted}) (original unchanged): {sorted_list}, original: {unsorted}")

# range(start, stop, step): Generates a sequence of numbers.
range_list = list(range(5)) # 0, 1, 2, 3, 4
print(f"  list(range(5)): {range_list}")
range_start_stop = list(range(2, 7)) # 2, 3, 4, 5, 6
print(f"  list(range(2, 7)): {range_start_stop}")
range_step = list(range(0, 10, 2)) # 0, 2, 4, 6, 8
print(f"  list(range(0, 10, 2)): {range_step}")

# enumerate(iterable, start=0): Returns an enumerate object. Iterates with index and value.
for index, value in enumerate(['a', 'b', 'c']):
    print(f"  enumerate example: Index {index}, Value {value}")

# zip(*iterables): Aggregates elements from multiple iterables.
names = ['Alice', 'Bob']
ages = [30, 25]
zipped = list(zip(names, ages))
print(f"  list(zip(['Alice','Bob'], [30,25])): {zipped}")

# abs(): Returns the absolute value of a number.
print(f"  abs(-10): {abs(-10)}")

# round(number, ndigits=None): Rounds a number to a given precision.
print(f"  round(3.14159, 2): {round(3.14159, 2)}")

# input(prompt): Reads a line from input, converts to string.
# user_input = input("  Enter something: ")
# print(f"  You entered: {user_input}")

# open(file, mode): Opens a file and returns a file object. (Basic, more for file I/O)
# try:
#     with open("example.txt", "w") as f:
#         f.write("Hello from Python!\n")
#     print("  'example.txt' created.")
# except Exception as e:
#     print(f"  Error creating file: {e}")