class StrReverse:
    
    def __init__(self):
        self.__string = ""
        
    def takeInput(self):
        self.__string = input("Enter a string: ")
    
    def reverseString(self):
        return self.__string[::-1]
    
obj1 = StrReverse()
obj1.takeInput()

print(f"The reversed word is : {obj1.reverseString()}")