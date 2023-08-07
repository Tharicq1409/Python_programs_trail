#Polymorphism
'''
Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as if they are objects of a common superclass. It enables you to write more flexible and reusable code by providing a consistent interface for different types of objects.

In Python, polymorphism is achieved through method overriding and method overloading.

    Method Overriding: Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. This allows you to customize the behavior of a method for each subclass.'''

class Animal():
    def sound(self):
        print("Animal Makes sound.")

class Dog(Animal):
    def sound(self):    #Method Overriding
        print("Dog Barks")

class Bird(Animal):
    def sound(self):    #Method Overriding
        print("Bird Sings")

fly = Bird()
fly.sound()