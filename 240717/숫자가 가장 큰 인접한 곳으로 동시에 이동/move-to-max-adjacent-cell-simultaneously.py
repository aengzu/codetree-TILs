n, m, t = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

marbles = [tuple(map(int, input().split())) for _ in range(m)]

# 상하좌우 
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    max_value = -1
    max_position = (x, y)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > max_value:
            max_value = arr[nx][ny]
            max_position = (nx, ny)
    return max_position

for now_t in range(t):
    new_marbles = []
    for marble in marbles:
        x, y = marble
        new_position = can_go(x - 1, y - 1) 
        new_marbles.append((new_position[0] + 1, new_position[1] + 1)) 
    
    # 중복된 구슬 제거
    position_count = {}
    for pos in new_marbles:
        if pos in position_count:
            position_count[pos] += 1
        else:
            position_count[pos] = 1
    
    marbles = [pos for pos in new_marbles if position_count[pos] == 1]

print(len(marbles))