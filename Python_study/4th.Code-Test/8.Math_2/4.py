def check(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

a, b = map(int, input().split())
for i in range(a, b+1):
    if check(i):
        print(i)