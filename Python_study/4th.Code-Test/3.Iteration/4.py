T = int(input())
n = int(input())

i = 0
y = 0
while i < n:
    a,b  = map(int, input().split())
    x = a*b
    y += x
    i += 1

if T == y:
    print("Yes")
else:
    print("No")