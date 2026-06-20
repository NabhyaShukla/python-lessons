#Eg. of Abstraction, inheritence, and polymorphism

from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):#when you declare a method as abstract @abstractmethod it is unimplemented...you cant write anything
    @abstractmethod
    def behave(self):
        pass

    def display(self):
        print(f"This is normal method, so i have implemented")

class Dog(Animal):
    @override
    def behave(self):
        print("Dog Barks...")

class Cat(Animal):
    @override
    def behave(self):
        print("Cat Meows...")

class Snake(Animal):
    @override
    def behave(self):
        print("Snake Hiss...")

d1 = Dog()
c1 = Cat()
s1 = Snake()

d1.behave()
c1.behave()
s1.behave()