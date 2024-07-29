n = int(input())

# 2, 3 , 2+3, 3+3, 2+3+3, 2+2+2, 3+2
# f(2) = 1 
# f(3) = 1
# f(4) = f(2) + 2 = 1
# f(5) = f(2) + 3 / f(3) + 2 = 2
# f(6) = f(3) + 3 / f(4) + 2 = 2
# f(7) = f(4) + 3 / f(5) + 2 = 1 + 2 = 3
# f(8) = f(5) + 3 / f(6) + 2 = 2 + 2 = 4




MAX_N = 1000

memo = [0] * (MAX_N + 1)
memo[2], memo[3], memo[4] = 1, 1, 1

for i in range(5, n+1):
    memo[i] = memo[i-2] + memo[i-3]
    print(memo[i])


print(memo[n])