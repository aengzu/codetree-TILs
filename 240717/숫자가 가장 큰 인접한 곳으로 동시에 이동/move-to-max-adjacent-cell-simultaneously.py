n, m , t = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

marbles = [tuple(map(int, input().split())) for _ in range(m)]

#상하좌우
dxs = [0,0,-1,1]
dys = [1,-1,0,0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    max_value = -1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            if (max_value < arr[ny][nx]):
                max_value = arr[ny][nx]
    return x, y


for now_t in range(t):
    new_marbles = set()
    for marble in marbles:
        x, y = marble[0], marble[1]
        new_position = can_go(x - 1, y - 1)
        new_marbles.add((new_position[0]-1, new_position[1]-1))
    marbles = list(new_marbles)


print(len(new_marbles))