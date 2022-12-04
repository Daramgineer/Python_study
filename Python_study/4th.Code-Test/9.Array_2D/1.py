a, b = map(int, input().split())
x, y = [], []
 
for row in range(a):
    row = list(map(int, input().split())) #map 함수로 인해 row에 index가 생성됨. 자동으로 row가 3줄 만들어질때까지 입력.
    x.append(row)

for row in range(a):
    row = list(map(int, input().split())) #위와 마찬가지
    y.append(row)
    
for row in range(a):
    for col in range(b):
        print(x[row][col] + y[row][col], end=' ') #map 함수가 자동으로 col역할을 맡고있었음. 연산및 출력 바로가능.
    print()