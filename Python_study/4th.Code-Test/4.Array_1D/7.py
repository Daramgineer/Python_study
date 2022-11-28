a = int(input())
x = list(map(int, input().split()))
y = max(x)
z = [0 for i in range(a)]
i = 0
b = 0
c = 0
while i < a:
    z[i] = x[i]/y*100
    b += z[i]
    i += 1
c = b/a
print(c)