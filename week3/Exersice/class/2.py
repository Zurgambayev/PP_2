class Shape():
    def __init__(self):
        pass
class Squar(Shape):
    def __init__(self, leight):
        Shape.__init__(self)
        self.leight = leight
    def area (self):
        return self.leight ** 2
p = Squar(int(input()))
print(p.area())
