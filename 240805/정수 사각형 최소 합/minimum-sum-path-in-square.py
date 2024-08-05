# 출발 (1, N) 도착 (N, 1)
# 왼쪽 혹은 아래로 이동

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

sum_arr = [[0] * n for _ in range(n)]

sum_arr[0][n-1] = arr[0][n-1]

# 테두리 채우기 ((1, n) 부터 왼쪽으로)
for i in range(n-2, -1, -1):
    sum_arr[0][i] = sum_arr[0][i+1] + arr[0][i]

# 테두리 채우기 ((1,n) 에서 아래쪽으로)
for i in range(1, n):
    sum_arr[i][n-1] = sum_arr[i-1][n-1] + arr[i][n-1]

# 가운데 채우기 (위랑 오른쪽에서 최솟값 가져와서 더하기)
for i in range(1, n):
    for j in range(n-2, -1, -1):
        sum_arr[i][j] = min(sum_arr[i-1][j], sum_arr[i][j+1]) + arr[i][j]


print(sum_arr[n-1][0])