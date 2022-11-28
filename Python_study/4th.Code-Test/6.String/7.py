a, b = map(int, input().split())
x = list(str(a))
y = list(str(b))

x.reverse()
y.reverse()

p = ''.join(x)
q = ''.join(y)
print(max(p,q))