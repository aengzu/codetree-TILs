import sys

INT_MIN = -sys.maxsize
ans = INT_MIN

n = int(input())

arr = list(map(int, input().split()))

arr_sum = arr[0]

for i in range(1, n):
    if sum_of_nums < 0:
        sum_of_nums = arr[i]
    
    else:
        sum_of_nums += arr[i]
    
    ans = max(ans, sum_of_nums)

print(ans)