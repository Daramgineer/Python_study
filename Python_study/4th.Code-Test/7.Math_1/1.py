a, b, c = map(int, input().split())

if b >= c:
    i = -1

else:
    i = a/(c-b) + 1

print(int(i))