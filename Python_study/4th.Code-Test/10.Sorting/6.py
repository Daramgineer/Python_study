"""import numpy
import sys
from collections import Counter
input=sys.stdin.readline
x = []
a = int(input())
for _ in range(a):
    x.append(int(input()))
x.sort()

print(round(numpy.mean(x)))
print(print(x[a//2]))
f = Counter(x) # 각 성분마다 개수 카운트 해서 딕셔너리 형태로 저장 
b = f.most_common() # 빈도수가 높은순으로 투플형태로 저장
if len(x) >1: #만약 입력값이 하나면, 그게 최빈값이므로 예외처리
    if b[0][1] == b[1][1]:
        print(b[1][0]) # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번쨰로 작은것을 출력
    else:
        print(b[0][0])
else:
    print(x[0])
print(x[-1] - x[0])""" #출력은 동일한데 런타임에러가 뜸....이유는 모름.


import sys
from collections import Counter
N = int(sys.stdin.readline())

k = []

for i in range(N):
    k.append(int(sys.stdin.readline()))
    
k.sort()
#산술평균
print(int(round(sum(k)/N,0)))

#중앙값
print(k[N//2])

#최빈값
f = Counter(k) # 딕셔너리 형태로 출력 Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1})

b = f.most_common() # 빈도수가 높은순으로 투플형태로 출력 [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]

if len(k) >1: #만약 입력값이 하나면, 그게 최빈값이므로 예외처리
    if b[0][1] == b[1][1]:
        print(b[1][0]) # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번쨰로 작은것을 출력
    else:
        print(b[0][0])
else:
    print(k[0])

#범위
print(k[-1] - k[0])