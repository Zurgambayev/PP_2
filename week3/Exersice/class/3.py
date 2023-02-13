class Shape():
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__ (self,leight,width):
        Shape.__init__(self)
        self.leight = leight
        self.width = width
    def area (self):
        return self.leight * self.width
p1 = Rectangle(int(input()),int(input()))
print(p1.area())