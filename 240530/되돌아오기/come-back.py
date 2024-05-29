n = int(input())

x, y = 0, 0

# 동 서 남 북
dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

ans = -1

time = 0

# dir 방향으로 dist 만큼 이동
def move(move_dir, dist):
    global x, y
    global ans, time

    for _ in range(dist):
        x, y = x + dxs[move_dir], y + dys[move_dir]

        time += 1

        if x==0 and y==0:
            ans = time
            return True
    return False

for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    if c_idr == 'E':
        move_dir =0
    elif c_dir =='W':
        move_dir = 1
    elif c_dir =='S':
        move_dir = 2
    else:
        move_dir = 3
    
    done = move(move_dir, dist)

    if done:
        break


print(ans)