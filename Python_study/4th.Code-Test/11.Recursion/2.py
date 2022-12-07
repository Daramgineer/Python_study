n = int(input())
a, b = 0, 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while n > 1:
        c = a + b
        a = b
        b = c
        n -= 1
    print(c)
