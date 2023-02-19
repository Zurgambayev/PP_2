def Funcia(m):
    for i in m:
        m[i] *= 28.3495231 


m = {}
a = int(input())
while a:
    b = int(input())
    m[input()] = b
    a -= 1
Funcia(m)
print(m)   
