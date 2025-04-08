class MyClass:
    
    __privetVar = 27
    
    def __init__(self, name):
        self.name = name
        
    def __privetMeth(self):
        print("I'm inside class MyClass")
        
    def hello(self):
        print(f"Privet Variable value: {MyClass.__privetVar}")
        
xyz = MyClass("Nahian")

print(xyz.name)
# print(xyz.__privetVar)
#xyz.__privetMeth()

xyz.hello()