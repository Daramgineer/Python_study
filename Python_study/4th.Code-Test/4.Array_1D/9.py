a = int(input())
b = 0
p = 0
count = 0
y = []
for _ in range(a):
    x = list(map(int, input().split()))
    for i in range(len(x)-1):
        b += x[i+1]
        i += 1
    c = b/(len(x)-1)

    for i in range(len(x)-1):
        if c < x[i+1]:
            count += 1
            i += 1

    d = (count / (len(x) - 1))
    y.append(d*100)
    count = 0
    b = 0

while p < a:
    print("%.3f%%"%round(y[p],4))
    p += 1