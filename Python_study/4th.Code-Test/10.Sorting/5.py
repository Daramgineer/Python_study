#https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html

import sys
input=sys.stdin.readline

a = int(input())
x = [0]*10000

for i in range(a):
    b = int(input())
    x[b-1] += 1 #x 에 입력된 각 숫자의 횟수를 저장함. 5가 3번 입력되면 5번째에 3을 저장.
    
for i in range(10000):
    if x[i] != 0:
        for j in range(x[i]): #x에 저장된 수만큼 index+1 의 숫자를 출력(0부터 시작하는 리스트 특성)
            print(i+1)