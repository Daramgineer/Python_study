a = int(input())

x = []
for i in range(a):
    x.append(int(input()))
    
x.sort()

for i in range(a):
    print(x[i])