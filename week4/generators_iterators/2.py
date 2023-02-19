def gen(n):
    a = 0
    while a < n:
        if a % 2 == 0:
            yield a
        a+=1
even = gen(int(input()))
for i in even:
    print(i,end = ',')