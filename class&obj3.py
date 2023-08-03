class phone:
    android_version = 13            #Class Variable  --> when variables are common for all class use class variable
    def __init__(self,name,model):  
        self.name = name            #Instance variable --> when variables are specific to some class use Instance Variable
        self.model = model
    def display(self):
        print(" Brand Name : ",self.name)       
        print(" Model Name : ",self.model)
        print("Android Version ",self.android_version)
        print('\n')


redmi = phone("Redmi","Note 12 Pro Max") #object created
redmi.display()

realme = phone("Realme","10 Pro 5G")
realme.display()
