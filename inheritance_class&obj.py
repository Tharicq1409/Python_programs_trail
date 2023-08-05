#Inheritance
'''
In Python, inheritance is a fundamental concept in object-oriented programming that allows you to create new classes based on existing classes. 
There are three main types of inheritance: single inheritance, multiple inheritance, and multilevel inheritance. 
Single Inheritance:
    Single inheritance involves creating a new class (derived or subclass) that inherits attributes and behaviors from a single parent class (base or superclass).

Multiple Inheritance:
    Multiple inheritance involves creating a new class that inherits attributes and behaviors from more than one parent class. 
    This allows the new class to combine features from multiple sources.

Multilevel Inheritance:
    Multilevel inheritance involves creating a chain of classes, where a derived class inherits from a parent class, and then another class inherits from the derived class. 
    This creates a hierarchical structure.
'''

'''
class dad():
    def phone(self):
        print("Dad's Phone")
class mom():
    def sweet(self):
        print("Mom prepared a Sweets")
class son(dad,mom):     # Multiple Inheritance
    def laptop(self,son):
        self.son = son
        print(self.son+" is a son and He has a laptop")

ram=son()
ram.laptop("Ram")
ram.phone()
ram.sweet()


#Multilevel Inheritance
class Mom():
    def sweet(self):
        print("Sweets Prepared By Mom")

class dad(Mom):
    def phone(self):
        print("Dad's Phone")

class son(dad,Mom):     # Multiple Inheritance
    def laptop(self,son):
        self.son = son
        print(self.son+" is a son and He has a laptop")
        print(self.son+" eats",end=" ")
        Mom.sweet(self)


ram=son()
ram.laptop("Ram")
ram.phone()
ram.sweet()


#hierarchial Inheritance - when parent class is used by more than 2 classes
class dad():
    def money(self):
        print("Dad's Money")

class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass 

son3=son3()
son3.money()


#vaiable usage in single inheritance
class Parent:
    def method1(self):
        self.var1 = "Hello from method1"
    
    def method2(self):
        print(self.var1)

class Child(Parent):
    def method3(self):
        self.var2 = "Hi from method3"
    
    def method4(self):
        print(self.var1)        #using variable of parent class

child_instance = Child()
child_instance.method1()
child_instance.method3()

child_instance.method2()  # This will print: "Hello from method1"
child_instance.method4()  # This will print: "Hi from method3"


#vaiable usage in multiple inheritance
class Parent1:
    def method1(self):
        self.var1 = "Hello from method1 of Parent1"

class Parent2:
    def method2(self):
        self.var2 = "Hi from method2 of Parent2"

class Child(Parent1, Parent2):
    def method3(self):
        self.method1()  # Call method1 from Parent1
        self.method2()  # Call method2 from Parent2
        print(self.var1)  # Access var1 from Parent1
        print(self.var2)  # Access var2 from Parent2

child_instance = Child()
child_instance.method3()
'''
#vaiable usage in multi level inheritance

class Grandparent:
    def method1(self):
        self.var1 = "Hello from method1 of Grandparent"

class Parent(Grandparent):
    def method2(self):
        self.method1()  # Call method1 from Grandparent
        print(self.var1)  # Access var1 from Grandparent

class Child(Parent):
    def method3(self):
        self.method2()  # Call method2 from Parent

child_instance = Child()
child_instance.method3()
