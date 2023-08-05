#Inheritance
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
son3.money()'''

