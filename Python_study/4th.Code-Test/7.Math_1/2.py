a = int(input())
b = 1
n = 6
count = 1
while b < a:
    count += 1
    b += n
    n += 6

print(count)