T = int(input())
i = 0
j = 0
x = [0 for i in range(T)]
while i < T:
    a,b  = map(int, input().split())
    x[i] = a+b
    i += 1
while j < T:
    print("{0}".format(x[j]))
    j += 1