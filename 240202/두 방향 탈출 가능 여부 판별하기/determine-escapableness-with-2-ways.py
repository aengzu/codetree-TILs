n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# n행 m 열
visited = [([0] * m )for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y<m


def can_go(x, y):
    if not in_range(x, y):
        return False
    # 방문 하지 않았거나(길이 없거나) 뱀이 있다면 갈 수 없으므로 return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

# [0] 오른쪽 , [1] 아래쪽
dx, dy = [0,1], [1,0]
def dfs(x, y):
    for i, j in zip(dx, dy):
        new_x, new_y = x + i, y + j

        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)
    
visited[0][0] = 1
dfs(0,0)


print(visited[n-1][m-1])