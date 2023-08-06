
class a:
    def __init__(self):
        print("This is from class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("This is from Class B")
class c(b):
    def __init__(self):
        super().__init__()
        print("This is from Class C")
obj1 = c()

'''
class Parent:
    def greeting(self):
        print("Hello from Parent")

class Child(Parent):
    def greeting(self):
        super().greeting()  # Call the greeting() method of the Parent class
        print("Hi from Child")

child = Child()
child.greeting()
'''