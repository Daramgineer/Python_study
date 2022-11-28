import math
a, b, c = map(int, input().split())
day = math.ceil((c-a)/(a-b)) + 1
print(day)