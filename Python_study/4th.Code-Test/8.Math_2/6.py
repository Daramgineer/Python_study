def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

# 소수 집합 만들기
nums = {x for x in range(2, 10_001) if x == 2 or x % 2 == 1}
# nums = 2와 홀수로 이루어진 집합
for odd in range(3, 101, 2): # 101 == int(math.sqrt(10_000)) + 1
    nums -= {i for i in range(2 * odd, 10_001, odd) if i in nums}
    # 홀수의 배수로 이루어진 집합을 빼줌

# 골드바흐 수를 출력
t = int(input())
for _ in range(t):
    even = int(input())
    half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
    for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
        if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
            print(x, even-x)  # 작은수부터 출력
            break
