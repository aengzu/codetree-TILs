MAX_N = 1000000
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

min_arr = [[MAX_N+1]*n for _ in range(n)]
min_arr[0][0] = arr[0][0]

# 테두리값 세팅
for i in range(1, n):
    min_arr[0][i] = min(min_arr[0][i-1], arr[0][i])
    min_arr[i][0] = min(min_arr[i-1][0], arr[i][0])

# 내부값 세팅
for i in range(1, n):
    for j in range(1, n):
        min_arr[i][j] = min(min_arr[i-1][j], min_arr[i][j-1], arr[i][j])


print(max(min_arr[n-2][n-2], min_arr[n-2][n-1], min_arr[n-1][n-2]))