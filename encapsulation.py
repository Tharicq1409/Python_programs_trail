'''
class Company():
    def __init__(self):
        self.__company = "Google"  #private variable are accessed with a method inside a same class

    def company_print(self):
        print(self.__company)
company = Company()
company.company_print()'''



class King():
    def __init__(self):
        self._name = "Tharicq" #protected variable are accessible within the same class or child class.

king=King()
print("This code has been Written By "+king._name+" and he is a King !")