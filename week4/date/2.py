from random import random

class Ran:
    def __init__(self, quantity):
        self.qty = quantity
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.cur += random()
            self.qty -= 1
            return round(self.cur, 2)
        else:
            raise StopIteration

it = Ran(50)
for i in it:
    print(i)