n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


arr_sum = [[0] * n  for _ in range(n)]

# 초기값 세팅
arr_sum[0][0] = arr[0][0]

# 가장자리 채우기 
for i in range(1, n):
    arr_sum[i][0] = arr_sum[i-1][0] + arr[i][0]
    arr_sum[0][i] = arr_sum[0][i-1] + arr[0][i]

# 내부 채우기
for i in range(1, n):
    for j in range(1, n):
        arr_sum[i][j] = max(arr_sum[i-1][j], arr_sum[i][j-1]) + arr[i][j]

print(arr_sum[n-1][n-1])