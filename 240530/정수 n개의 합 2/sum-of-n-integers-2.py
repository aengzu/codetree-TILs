import sys
INT_NUM = -sys.maxsize

n, k = tuple(map(int, input().split()))

arr = [0] = list(map(int, input().split()))
pre_sum = [0] * (n+1)

ans = INT_MIN


def get_sum(s, e):
    return pre_sum[e] - pre_sum[s]


pre_sum[0] = 0
for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + arr[i]

for i in range(1, n-k+2):
    ans = max(ans, get_sum(i, i+k-1))

print(ans)