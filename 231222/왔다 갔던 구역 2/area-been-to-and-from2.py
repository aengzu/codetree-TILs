n = int(input())
area = [0] * 1001
now = 0

for _ in range(n):
    hop, dir = tuple(input().split())
    hop = int(hop)
    if dir == 'L':
        dst = now - hop
        for i in range(dst, now):
            area[i] += 1
        now = dst
    elif dir == 'R':
        dst = now + hop
        for i in range(now, dst):
            area[i] += 1
        now = dst

cnt = 0
for i in area:
    if i >= 2:
        cnt += 1
print(cnt)