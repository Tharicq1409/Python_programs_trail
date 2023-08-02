'''
class student:
    def __ini__(self): #constructor
        self.name=""    #creating variables inside constructor
        self.register_no=""
    def display(self):
        print("Register Number :",self.register_no)
        print("Name :",self.name)

s1=student()
s1.name = "Ram"
s1.register_no = "001"
s1.display()


s2=student()
s2.name= "John"
s2.register_no = "002"
s2.display()

class Fruit():
    def __init__(self,color):
        self.color = color

apple = Fruit("Green")
print(apple.color)
'''

class teacher:
    def __init__(self,name,reg_no):
        self.name = name
        self.reg_no = reg_no
    def display(self):
        print("Teacher Name : ",self.name)
        print("Register No : ",self.reg_no)

t1 = teacher("Raghu",1001)
t1.display()
t2 = teacher("Prabhu",1002)
t2.display ()