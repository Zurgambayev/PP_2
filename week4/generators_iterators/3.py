def delt(n):
    a = 0
    while a < n:
        if a % 3 == 0 and a % 4 == 0:
            yield a
        a += 3
four_three = delt(int(input()))
for i in four_three:
    print(i, end = ',')