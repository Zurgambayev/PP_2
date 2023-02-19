def voz(n):
    for i in range(n,0 - 1, -1):
        yield i
a = voz(int(input()))
for x in a:
    print(x, end = ', ')