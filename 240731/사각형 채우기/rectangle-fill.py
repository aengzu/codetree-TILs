n = int(input())

MAX_N = 1000

# 2 x 1 사각형은 2x1 ->  1개
# 2 * 2 사각형은 2*1, 2*1 / 1*2, 1*2 -> 2개
# 2 * 3 사각형은 2*1, 2*1, 2*1 / 1*2 1*2 2*1 / 1*2 2*1 2*1 / 3개

table = [0] * MAX_N
table[0] = 1
table[1] = 2
table[2] = 3
for i in range(2, n):
    table[i] = table[i-1] + table[i-2]

print(table[n-1]%10007)