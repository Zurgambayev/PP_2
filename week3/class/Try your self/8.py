class Person:
    def __init__(era, name, age):
        era.name = name
        era.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John" ,19)
del p1.age

print(p1.age)