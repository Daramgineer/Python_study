i = 0
x = [0 for i in range(9)]
while i < 9:
    x[i] = int(input())
    i += 1
print(max(x), x.index(max(x))+1)