#Python Inheritance
class Dad:              #Parent Class 1
    def owns_mobile(self):
        self.mobile = "Dad's Mobile"

class Mom:
    def prepared(self): #Parent Class 2
        self.cook = "Sweets Prepared by his Mom."

class Son(Dad,Mom): 
    def owns_laptop(self,son_name,laptop):
        self.laptop = laptop
        self.son = son_name
        self.owns_mobile()  #Calling Method from Parent Class 1
        self.prepared()     #Calling Method from Parent Class 2
        print(self.son + " is a son and " +self.laptop+ " He doesn't have mobile so he uses his " +self.mobile+ 
        ". Meanwhile " +self.son+ " eats " +self.cook)

raghu=Son()
raghu.owns_laptop("Raghu","he has a laptop.")