import sys
input = sys.stdin.readline

T = int(input())
i = 0
x = '*'
while i < T:
    print(" "*(T-1) + x)
    T -= 1
    x += "*"