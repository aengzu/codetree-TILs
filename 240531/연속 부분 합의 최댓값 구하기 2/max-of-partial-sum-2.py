import sys

INT_MIN = -sys.maxsize
ans = INT_MIN

n = int(input())

arr = list(map(int, input().split()))

arr_sum = arr[0]

for i in range(1, n):
    if arr_sum < 0:
        arr_sum = arr[i]
    
    else:
        arr_sum += arr[i]
    
    ans = max(ans, arr_sum)

print(ans)