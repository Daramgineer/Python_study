def recursion(s, l, r):
    global counter
    counter += 1
    if l >= r: return 1 #탐색위치가 같아지거나 역전되는 경우 1리턴
    elif s[l] != s[r]: return 0 #양쪽 끝이 다르면 0리턴 
    else: return recursion(s, l+1, r-1) #양쪽끝이 같으면 하나씩 안쪽 재탐색.

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

a = int(input())
for _ in range(a):
    counter = 0
    a = isPalindrome(str(input()))
    print(a, counter)