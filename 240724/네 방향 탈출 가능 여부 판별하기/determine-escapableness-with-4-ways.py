from collections import deque
n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [1,-1,0,0], [0,0,1,-1]
queue = deque()

visited = [[0]*m for _ in range(n)]

def in_range(r, c):
    return 0<=r<n and 0<=c<m

def bfs():
    while queue:
        r,c = queue.popleft()
        for dr, dc in zip(drs, dcs):
            new_r, new_c = r+dr, c + dc

            if in_range(new_r, new_c) and arr[new_r][new_c] == 1 and not visited[new_r][new_c]:
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))


queue.append((0,0))
visited[0][0] = 1

bfs()

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)