from collections import deque

n ,m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [0,0,-1,1],[1,-1,0,0]

def in_range(r,c):
    return 0<=r<n and 0<=c<m

# 깊이를 담기 위한 배열
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 방문 여부를 위한 배열
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque()

def push(r, c, s):
    step[r][c] = s
    visited[r][c]= 1
    q.append((r,c))

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            new_r, new_c = r + dr, c+ dc
            if in_range(new_r, new_c) and visited[new_r][new_c]== 0 and arr[new_r][new_c]==1:
                push(new_r, new_c, step[r][c] + 1)
            
push(0, 0, 0)
bfs()

if visited[n-1][m-1] = 1:
    print(step[n-1][m-1])
else:
    print(-1)