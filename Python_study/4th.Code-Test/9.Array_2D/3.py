a = int(input())
paper = [[0]*101 for i in range(101)] # 0,0 을 포함하고 있어서 101개임.(행렬특징)

for _ in range(a):
    left,bottom = map(int, input().split())
    for i in range(10): #색칠 가로크기 10
        for j in range(10): #색칠 세로크기 10
            paper[left+i][bottom+j] = 1 #좌측부터 10, 하단부터 10 까지 해당열의 성분을 1로 바꿈

check = 0
for i in paper: #i가 paper의 모든 row와 col에 대해 연산 진행
    check += sum(i) #paper안에 있는 모든 1을 합함. (격자당 색칠된 크기는 1)
print(check)