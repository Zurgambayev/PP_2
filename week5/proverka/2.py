from functools import reduce

numbers = []
numbers = [1, 2, 3, 4, 5]

def product(x, y):
    return x * y

result = reduce(product, numbers)



result = reduce(product, numbers)


result = reduce(product,) 


result


print(result)
