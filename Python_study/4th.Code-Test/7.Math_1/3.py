a = int(input())
b = 0
c = 1
x = 0
w = 1
while b < a:
    b += c
    c += 1
    x += 1

y = x - (b - a)
z = x - (y - 1)

if (x%2 != 0):
    print(str(z) + '/' + str(y))
else:
    print(str(y) + '/' + str(z))