a = int(input())
b = list(map(int, str(a)))
b.sort(reverse=True)
c = ''.join(str(x) for x in b)
print(c)