a = 42
i = 0
j = 0
x = [0 for i in range(10)]
y = [0 for i in range(10)]
while i < 10:
    x[i] = int(input())
    y[i] = int(x[i]%a)
    i += 1

y_count = list(set(y))
print(len(y_count))