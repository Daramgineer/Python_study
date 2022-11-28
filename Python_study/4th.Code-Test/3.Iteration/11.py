a = 1
b = 1
i = 0
j = 0
x = []
while True:
    try:
        a, b = map(int, input().split())
        x.append(a+b)
        i += 1
    except:
        break

while j < i:
    print("{0}".format(x[j]))
    j += 1