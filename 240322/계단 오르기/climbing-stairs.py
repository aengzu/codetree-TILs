n = int(input())
MOD = 10007
# 0층일 때는 0가지, 1층일 때 0가지
# 2층일 때 1가지, 3층일 때 1가지, 
# 3층일 때 1가지
# 4층일 때 2+2, 1가지 
# 5층일 때 2+3, 1가지, (3층일때 까지 방법수 + 1) + (2층일때까지 방법수 +1)
# 6층일 때 3+3, 2+2+2, 2가지
# 7층일 때 3+2+2, 1가지



# dp[0] = 0 , dp[1] = 0
# dp[2] = 1, dp[3] = 1
# dp[i] = dp[i-2] + dp[i-3] + 2

dp = [0] * 1001
dp[0], dp[1] = 0,0
dp[2], dp[3] = 1,1

for i in range(4, n+1):
    dp[i] = (dp[i-2] + dp[i-3])  % MOD

print(dp[n])