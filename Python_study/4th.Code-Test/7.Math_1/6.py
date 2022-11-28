num = int(input())
for _ in range(num):
    a = int(input())
    b = int(input())

    f = [x for x in range(1, b+1)]
   
    for k in range(a):
        for i in range(1, b):
            f[i] += f[i-1]
    print(f[-1])