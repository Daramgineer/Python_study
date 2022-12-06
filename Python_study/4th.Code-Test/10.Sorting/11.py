import sys
n = int(sys.stdin.readline())
member = []
for _ in range(n):
    member.append(list(input().split())) #입력 순서대로 분리해서 리스트 작성 [(0,0), (1,1)....]

member.sort(key=lambda a:int(a[0])) #모든 리스트의 0번성분 기준으로 전체 정렬.

for i in range(n):
    print(member[i][0], member[i][1]) #i번째의 0번 성분, 1번성분 출력준