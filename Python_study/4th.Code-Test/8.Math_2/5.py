import math
def c(a,b):
    count = 0
    check = [True] * (b+1) 
    for i in range(2,int(math.sqrt(b)+1)):
        if check[i] == True:
            for j in range(i*2, b+1, i):
                check[j] = False
    
    for i in range(a+1,b+1): 
        if check[i] == True:
            count += 1
    return count

result = []
while True:
    a = int(input())
    if a == 0:
        break
    result.append(c(a,2*a))
    
for i in result:
    print(i)
    