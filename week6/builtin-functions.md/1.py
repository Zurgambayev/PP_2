from functools import reduce

def f(lst):
    return reduce(lambda x, y: x * y, number)
number = [1,2,3,4,5]

Lambdaa = f(number)

print(Lambdaa)