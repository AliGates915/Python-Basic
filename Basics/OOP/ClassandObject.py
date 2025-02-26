# OOP in Python - Covers All Topics

from abc import ABC, abstractmethod  # For Abstraction

# 1. Class and Object
class Animal:
    def __init__(self, name, species):
        self.name = name  # Public Attribute
        self._species = species  # Protected Attribute
        self.__secret = "Hidden Info"  # Private Attribute
    
    def make_sound(self):
        return "Some generic sound"
    
    def get_secret(self):
        return self.__secret  # Accessing private attribute

# 2. Inheritance (Single, Multiple, Multilevel)
class Dog(Animal):  # Single Inheritance
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):  # Method Overriding
        return "Bark! Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

class Hybrid(Dog, Cat):  # Multiple Inheritance
    def __init__(self, name, breed):
        super().__init__(name, breed)

# 3. Abstraction (Using Abstract Class)
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started!"

# 4. Polymorphism (Same function, different behavior)
def animal_sound(animal):
    return animal.make_sound()

# 5. Encapsulation (Using Getters & Setters)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Variable
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited: ${amount}"
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"Withdrew: ${amount}"
    
    def get_balance(self):
        return self.__balance

# 6. Class Method and Static Method
class MathOperations:
    pi = 3.1415
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * (radius ** 2)
    
    @staticmethod
    def add(a, b):
        return a + b

# 7. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Testing the functionality
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers")
    hybrid = Hybrid("Mysterious Hybrid", "Unknown Breed")
    
    print(dog.make_sound())  # Bark! Bark!
    print(cat.make_sound())  # Meow! Meow!
    print(animal_sound(dog))  # Bark! Bark!
    print(animal_sound(cat))  # Meow! Meow!
    
    # Bank Account
    acc = BankAccount(1000)
    print(acc.deposit(500))  # Deposited: $500
    print(acc.withdraw(300))  # Withdrew: $300
    print(f"Balance: ${acc.get_balance()}")  # Balance: $1200
    
    # Math Operations
    print(MathOperations.circle_area(5))  # 78.5375
    print(MathOperations.add(10, 20))  # 30
    
    # Vector Addition
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    print(v3)  # Vector(6, 8)
