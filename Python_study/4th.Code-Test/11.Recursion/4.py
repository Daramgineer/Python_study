'''def merge_sort(arr):
    if len(arr) < 2: #리스트 개수가 한개면 정렬불필요.
        return arr

    mid = len(arr)+1 // 2
    low_arr = merge_sort(arr[:mid]) #기준 왼편 분할
    high_arr = merge_sort(arr[mid:]) # 기준 오른편 분할

    merged_arr = []
    l, h, k = 0, 0, 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            hit.append(low_arr[k])
            l += 1
            k += 1
        else:
            merged_arr.append(high_arr[h])
            hit.append(high_arr[k])
            h += 1
            k += 1
            
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

a, num = map(int, input().split())
b = list(map(int, input().split()))
hit = []
merge_sort(b)
if len(hit) < (num-2):
    print(-1)
else:
    print(hit[num-2])''' #메모리 초과....?


import sys
input = sys.stdin.readline
def merge_sort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L)+1)//2
   
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    
    i,j = 0,0
    L2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1
    
    return L2

n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)