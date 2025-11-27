class MyClass():
    
    name="Naman"
    def __init__(self,name):
        self.name = name
        print(self.name)
        
    @classmethod
    def view(cls):
        return cls.name
    
    

print(MyClass.view())
obj1 = MyClass(MyClass.name)