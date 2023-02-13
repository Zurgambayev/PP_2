def myFunction(n):
    return abs(n - 50)
a = [100,23,42,245,4,57,50]
a.sort(key = myFunction)
print(a)