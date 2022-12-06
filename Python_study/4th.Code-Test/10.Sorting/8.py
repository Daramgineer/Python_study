import sys
input=sys.stdin.readline

'''a = int(input())
n = []
for i in range(a):
    x, y = map(int, input().split())
    n.append([x,y])

n.sort(key=lambda x : (x[0], x[1]))

for i in range(a):
    print(n[i][0], n[i][0])'''


'''
a = int(input())
x, y = [], []
for i in range(a):
    p, q = map(int, input().split())
    x.append(p)
    y.append(q)

x.sort()
y.sort()

for i in range(a):
    print(x[i],y[i])
'''

N=int(input())
arr=[]
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])  #??? 위는 틀리고 아래는 맞는 이유는 도대체:????????