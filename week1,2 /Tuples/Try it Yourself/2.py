x = (1,2,3,4,5)
y = list(x)
y[1] = 101
x = tuple(y)
print(x)