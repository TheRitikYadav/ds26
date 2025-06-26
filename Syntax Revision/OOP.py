# python_oop_reference_commented.py

# A concise reference for Object-Oriented Programming (OOP) concepts in Python.

# --- 1. Classes and Objects ---
# Class: Blueprint for creating objects.
# Object (Instance): A specific instance of a class.

class Dog:
    # Class Variable: Attribute shared by ALL instances of this class.
    species = "Canis familiaris"

    # __init__ method: The CONSTRUCTOR. Called automatically when a new object is created.
    # 'self': Conventionally, the first parameter; refers to the instance itself.
    def __init__(self, name, age):
        # Instance Variables: Attributes unique to EACH instance.
        self.name = name
        self.age = age
        print(f"Dog {self.name} created.")

    # Instance Method: Function operating on an object's instance data ('self').
    def bark(self):
        return f"{self.name} says Woof!"

    # Instance Method with parameters.
    def get_age_in_dog_years(self, factor=7):
        return self.age * factor

# Creating Objects (Instantiation): Calling the class name like a function.
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(f"My dog's name: {my_dog.name}, age: {my_dog.age}")
print(f"Your dog's species: {your_dog.species}") # Accessing class variable.
print(f"Buddy's bark: {my_dog.bark()}")
print(f"Lucy's age in dog years: {your_dog.get_age_in_dog_years()}")
print(f"Buddy's age in cat years (factor 5): {my_dog.get_age_in_dog_years(5)}")


# --- 2. Encapsulation ---
# Purpose: Bundling data (attributes) and methods that operate on the data within a single unit (class).
# Controls access to internal state to maintain data integrity.

class Account:
    def __init__(self, balance):
        # Private-like attribute: The leading underscore '_' is a convention.
        # It signals that this attribute is internal and should not be accessed directly from outside the class.
        self._balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            
    def get_balance(self):
        # Public method: Provides controlled access to the encapsulated '_balance' data.
        return self._balance

my_account = Account(100)
my_account.deposit(50)
my_account.withdraw(30)
my_account.withdraw(200) # Invalid withdrawal
# print(my_account._balance) # Technically accessible due to Python's nature, but discouraged by convention.
print(f"Current balance via method: {my_account.get_balance()}")


# --- 3. Inheritance ---
# Purpose: Creating new classes (child/derived) from existing ones (parent/base).
# Child classes automatically inherit attributes and methods from their parents, promoting code reuse.

class Animal: # Parent class
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        # Placeholder for method meant to be implemented by subclasses.
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal): # Child class: Cat inherits from Animal.
    def __init__(self, name, breed):
        # super().__init__(name): Calls the constructor of the parent class (Animal).
        # Ensures parent's initialization logic runs.
        super().__init__(name)
        self.breed = breed
    
    def speak(self): # Method Overriding: Child class provides its own implementation of a parent method.
        return f"{self.name} the {self.breed} says Meow!"

class Lion(Cat): # Multi-level inheritance: Lion inherits from Cat.
    def speak(self): # Further Overriding.
        return f"{self.name} the Lion roars!"
        
class Doggo(Animal): # Another child class inheriting from Animal.
    def speak(self):
        return f"{self.name} says Woof!"

my_cat = Cat("Whiskers", "Siamese")
my_lion = Lion("Simba", "African")
my_doggo = Doggo("Fido")

print(my_cat.speak())
print(my_lion.speak())
print(my_doggo.speak())

# isinstance(obj, class): Inbuilt function. Purpose: Checks if an object is an instance of a class (or a subclass thereof).
print(f"Is Whiskers an Animal? {isinstance(my_cat, Animal)}")
# issubclass(child_class, parent_class): Inbuilt function. Purpose: Checks if a class is a subclass of another class.
print(f"Is Cat a subclass of Animal? {issubclass(Cat, Animal)}")


# --- 4. Polymorphism ---
# Purpose: Objects of different classes can be treated uniformly if they share a common interface.
# "Poly" (many) "morph" (forms) - a method takes many forms depending on the object it's called on.

animals = [Cat("mittens", "Domestic"), Doggo("Rex"), Lion("Mufasa", "King")]

for animal in animals:
    # Polymorphic call: The 'speak()' method behaves differently for each object type,
    # despite being called in the same way.
    print(animal.speak())


# --- 5. Abstraction ---
# Purpose: Hiding complex implementation details and showing only essential features.
# Achieved using abstract classes and methods (from 'abc' module).

from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC (Abstract Base Class) to make it abstract.
    @abstractmethod # Decorator: Marks a method as abstract. Subclasses MUST implement this method.
    def area(self):
        pass

    @abstractmethod # Another abstract method.
    def perimeter(self):
        pass
        
    def describe(self): # Concrete method within an abstract class.
        return "This is a geometric shape."

class Circle(Shape): # Concrete class: MUST implement all abstract methods from Shape.
    def __init__(self, radius):
        self.radius = radius
        
    def area(self): # Implementation of abstract 'area'.
        return 3.14159 * self.radius**2
        
    def perimeter(self): # Implementation of abstract 'perimeter'.
        return 2 * 3.14159 * self.radius

# shape = Shape() # ERROR: Cannot instantiate an abstract class directly.
my_circle = Circle(5)
print(f"Circle area: {my_circle.area()}")
print(f"Circle perimeter: {my_circle.perimeter()}")
print(my_circle.describe())


# --- 6. Special/Magic Methods (Dunder Methods) ---
# Purpose: Methods with double underscores (e.g., __init__, __str__).
# Python calls these automatically in specific situations to enable built-in functionalities
# or integrate with Python's core language features (e.g., len(), print(), + operator).

class Book:
    def __init__(self, title, author): # Constructor, as seen before.
        self.title = title
        self.author = author

    def __str__(self): # Dunder method. Purpose: Defines object's "informal" string representation.
        # Called by print(), str(). Aimed at human readability.
        return f"'{self.title}' by {self.author}"

    def __repr__(self): # Dunder method. Purpose: Defines object's "official" string representation.
        # Called by repr(). Aimed at unambiguous representation for developers (e.g., debugging).
        return f"Book(title='{self.title}', author='{self.author}')"
        
    def __len__(self): # Dunder method. Purpose: Enables the use of len() on object.
        # Returns the length of the book's title in this example.
        return len(self.title)
        
    def __add__(self, other): # Dunder method. Purpose: Defines behavior for the '+' operator.
        # Allows custom addition logic between Book objects.
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", "Various Authors")
        return NotImplemented # Important for binary operations; signals that this operation is not supported.

my_book = Book("The Hitchhiker's Guide", "Douglas Adams")
another_book = Book("The Restaurant at the End of the Universe", "Douglas Adams")

print(my_book) # Uses __str__
print(repr(my_book)) # Uses __repr__ explicitly
print(f"Length of title: {len(my_book)}") # Uses __len__
combined_book = my_book + another_book # Uses __add__
print(combined_book)