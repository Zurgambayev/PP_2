class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def MyFunction(self):
        print("Hello Bratan " + self.name)
p1 = Person("Erasyl",19)
p1.MyFunction()