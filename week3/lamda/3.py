def myfunc(n):
  return lambda a : a * n

m2 = myfunc(2)
m3 = myfunc(3)
print(m2(11))
print(m2(11))
print(myfunc(5)(11))