a = int(input())
x = list(map(int, input().split()))
b = int(input())
c = 0
for i in x:
    if i == b:
        c += 1

print(c)