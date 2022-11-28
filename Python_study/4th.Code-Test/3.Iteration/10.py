a = 1
b = 1
i = 0
j = 0
x = []
while (a != 0) & (b != 0):
    a, b = map(int, input().split())
    x.append(a+b)
    i += 1

while j < i-1:
    print("{0}".format(x[j]))
    j += 1