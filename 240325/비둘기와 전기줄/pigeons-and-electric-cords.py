# 최소라면 같은 번호의 비둘기에 대해 위치가 0 -> 1 혹은 1 -> 0으로 바뀐다면 도로를 건너간 것이다.
# 이를 위해 이전 위치를 저장하는 배열과 이동 횟수를 저장하는 배열이 필요하다.

n = int(input())

pigean = [0] * 101
now_p = [-1] * 101

for i in range(n):
    p, x = tuple(map(int, input().split()))
    if now_p[p] + x == 1:
        pigean[p] += 1
        now_p[p] = x
    elif now_p[p] == x:
        continue
    else:
        now_p[p] = x

sum = 0
for i in range(1, 101):
    if pigean[i] == -1:
        continue
    sum += pigean[i]

print(sum)