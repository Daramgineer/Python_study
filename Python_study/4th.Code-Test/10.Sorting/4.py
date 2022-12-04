import sys
input=sys.stdin.readline

a = int(input())
x, y = [], []
for i in range(a):
    x.append(int(input()))
    
y = sorted(x)

for i in range(a):
    print(y[i])