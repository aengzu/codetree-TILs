n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split()) for _ in range(n))]

# n 행 m 열
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 뱀이 없으면 1, 뱀이 있으면 0 

def in_map(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_map(x, y):
        return False
    # 이미 방문했거나 뱀이 있다면 못감
    if visited[x][y] or arr[x][y] ==0:
        return False
    
    return True

def dfs(x, y):
    # 오른쪽(열+1) 혹은 아래(행+1)로만 갈 수 있음
    dxs, dys = [0,1], [1,0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)


visited[0][0] = 1
dfs(0,0)

print(visited[n-1][m-1])