a = int(input())

for _ in range(a):
    x = input()
    score = 0
    b = 0
    for i in range(len(x)):
        if x[i] == "O":
            b += 1
            score += b
        elif x[i] == "X":
            b = 0
    print(score)