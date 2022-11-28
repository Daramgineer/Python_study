a = int(input())

for i in range(a):
    x, y = input().split()
    for j in y:
        print(j*int(x), end='')
    print()