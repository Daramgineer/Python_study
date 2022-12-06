import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr))) #중복값 없애고 정렬 진행
dic = {arr2[i] : i for i in range(len(arr2))} #정렬한 arr을 기준으로 dict구성
for i in arr:
    print(dic[i], end = ' ')