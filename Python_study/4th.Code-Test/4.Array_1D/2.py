a, b = map(int, input().split())
x = list(map(int, input().split()))
for i in x:
    if i < b:
        print(i, end=" ")