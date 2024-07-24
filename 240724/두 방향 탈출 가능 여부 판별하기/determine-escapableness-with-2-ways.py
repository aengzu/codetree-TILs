n,m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
drs, dcs = [0,1,0,-1], [1, 0,-1,0]


def in_range(r,c):
    return 0<=r<n and 0<=c<n

def dfs(r, c):
    if visited[r][c]==1:
        return
    visited[r][c] = 1
    for i in range(4):
        new_r, new_c = r + drs[i], c + dcs[i]
        if in_range(new_r,new_c) and arr[new_r][new_c] == 0:
            dfs(new_r, new_c)

dfs(0,0)

if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)