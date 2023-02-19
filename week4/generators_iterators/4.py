import math
def Genar(a,b):
    for i in range(a, b + 1):
        if i == math.sqrt(i) * math.sqrt(i):
            yield i

a = int(input())
b = int(input())
Squar = Genar(a,b)
for i in Squar:
    print(i, end = ',')
