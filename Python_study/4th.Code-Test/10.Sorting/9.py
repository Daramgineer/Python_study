import sys
input=sys.stdin.readline
'''
N=int(input())
arr=[]
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])'''

a = int(input())
n = []
for i in range(a):
    x, y = map(int, input().split())
    n.append([x,y])

n.sort(key=lambda x : (x[1], x[0]))

for i in range(a):
    print(n[i][0], n[i][1])