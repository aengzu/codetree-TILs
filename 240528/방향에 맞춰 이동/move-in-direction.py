n = int(input())
x, y = 0,0

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    if c_dir == 'E':
        # 동쪽이면 0 번
        move_dir = 0
    elif c_dir == 'W':
        # 서쪽이면 1번
        move_dir = 1
    elif c_dir == 'N':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)