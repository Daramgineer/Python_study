"""
10000 이하의 소수 찾기
while num <= 10000:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1

        if error == 0:
            x.append(num)
    num += 1

print(x)
"""

a = int(input())
num = 2
while a != 1:
  if a % num == 0: 
    print(num) 
    a = a / num
  else:
    num += 1