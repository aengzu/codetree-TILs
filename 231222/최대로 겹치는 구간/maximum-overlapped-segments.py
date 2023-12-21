# [x1, x2]에 대해 지점이 겹치는지가 궁금할 때에는 x1부터 x2까지, 
# 구간이 겹치는지가 궁금할 때에는 x1부터 x2 - 1까지 표기를 진행


n = int(input())

line = [0] * 101

for _ in range(n):
    x1 , x2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        line[i] += 1

print(max(line))