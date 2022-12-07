import sys
n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(sys.stdin.readline().strip())
    
set_list = set(l)	## set으로 변환해서 중복값을 제거
l = list(set_list)	## 다시 list로 변환
l.sort()	#괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬.
l.sort(key = len) #문자열 길이 순으로 정렬.

for i in l:
    print(i)