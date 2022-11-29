a = int(input())
b = int(input())
sum = 0
min = 0
check = 0
while a <= b:
    error = 0
    if a > 1 :
        for i in range(2, a):
            if a % i == 0:
                error += 1

        if error == 0:
            sum += a
            if check < 1:
                min = a
                check += 1
    a += 1

if sum < 1:
    min = -1

if sum > 0:
    print(sum)
    print(min)
elif sum < 1:
    print(min)