'''
class laptop:  #class name
    price = 0
    processor =  ''             #variables used
    ram = 0

HP = laptop()
dell = laptop()             #object created
Lenovo = laptop()

HP.price = 95000
HP.processor = "i7 12th Gen"     #variable declaration
HP.ram = "16GB"

print(HP.price)
print(HP.processor)     #print statement
print(HP.ram)

dell.price = 112000
dell.processor = "i7 13th Gen"
dell.ram = "16GB"

print(dell.price)
print(dell.processor)
print(dell.ram)

Lenovo.price = 97000
Lenovo.processor =  "i7 12th Gen"
Lenovo.ram = "16GB"

print(Lenovo.price)
print(Lenovo.processor)
print(Lenovo.ram)
'''


class Kodaikanal:   #class created
    name = ''
    distance = ''               #variables

    def firecamp(self):
        print("FireCamp at Evening time.")          #function definition

    def resort(self):
        print("Booked a Resort at Kodaikanal")

passenger1 = Kodaikanal()
passenger1.name = "Kumar"

print(passenger1.name + " enjoys" , end=' ')
passenger1.firecamp()

passenger2 = Kodaikanal()
passenger2.name = "Muthu"

print(passenger2.name  , end=' ')
passenger2.resort()





