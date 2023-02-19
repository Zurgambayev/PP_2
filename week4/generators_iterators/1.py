def gener(a):
    b = 1
    while b**2 < a:
        yield b**2
        b+=1
power = gener(int(input()))
for i in power:
    print(i)