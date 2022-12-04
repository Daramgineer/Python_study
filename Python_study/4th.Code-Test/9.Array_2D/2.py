a, b, c, d = 9, 9, 0, 0
x, y = [], []
max_value = None
for row in range(a):
    row = list(map(int, input().split()))
    x.append(row)

for row in range(a):
    for col in range(b):
        if (max_value is None or x[row][col] > max_value):
            max_value = x[row][col]
            c = row+1
            d = col+1

print(max_value)
print(c, d)