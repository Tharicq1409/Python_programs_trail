class a:
    def __init__(self):
        print("This is from class A")

class b(a):
    def __init__(self):
        super().__init__()
        print("This is from Class B")

obj1 = b()