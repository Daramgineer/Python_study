a = int(input())
b = int(input())
x = list(map(int, str(b)))
x, y, z = [a*x[2], a*x[1], a*x[0]]
print(x)
print(y)
print(z)
print(x + y*10 + z*100)