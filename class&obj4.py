'''
Class Methods : In Python, class methods are a type of method that are bound to the class itself rather than to instances of the class.
                They are defined using the @classmethod decorator and take the class itself as their first parameter, usually named cls. 
                Class methods can be useful for creating alternative constructors, performing operations on class-level attributes, or encapsulating logic that involves the class itself rather than its instances.
                
Static Methods : In Python, static methods are a type of method within a class that do not depend on the instance or class itself. 
                 They are defined using the @staticmethod decorator. 
                 Unlike regular methods and class methods, static methods don't receive any implicit first parameter (like self or cls).
                 Instead, they behave like regular functions that are contained within a class's namespace.
                 
Instance Methods : In Python, instance methods are the most common type of methods associated with a class. 
                   They are defined within a class and operate on the attributes and behavior of individual instances (objects) of that class.
                   Instance methods always have the instance itself (conventionally named self) as their first parameter, which allows them to access and manipulate the instance's attributes and methods.
'''


class laptop():
    Charger_type  = ""
    def __init__(self):             #Class Variable
        self.brand = ""
        self.price = 50000

    #Instance Method
    def setprice(self,price): 
        self.price = price           #Instance Variable
        print("Laptop Price : ",self.price)


    @classmethod    #Decorators need to be used while using Class Method
    def setChargerType(cls):
        cls.Charger_type = "C Type"     #Class Method
        print("Charger Type Changed to",cls.Charger_type)
    
    
    @staticmethod   #Decorators need to be used while using Static method
    def info():   
        print("Information is Empty :( ") 

lap1=laptop()           #object Created
lap1.setprice("49,999") #Method Call
lap1.setChargerType()
lap1.info()