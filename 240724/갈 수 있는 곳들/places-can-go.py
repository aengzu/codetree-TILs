from collections import deque
n, k = tuple(map(int, input().split()))
# 1: 이동 불가, 0: 이동가능
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
start_pts = []
bfs_q = deque()

for i in range(k):
    r, c = tuple(map(int, input().split()))
    start_pts.append((r,c))


def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y):
    # 범위 내에 있고, 방문 경험 없고, 0인 곳들만 갈 수 있다.
    return in_range(x,y) and not visited[x][y] and not grid[x][y]

cnt = 0
def bfs():
    global bfs_q
    global cnt
    # 오, 아, 왼,위
    dxs, dys = [0,1,0,-1],[1,0,-1,0]
    # 큐가 비어있지않다면 계속하기
    # 데큐는 size() 가 아니라 len() 으로 해야함.
    while bfs_q:
        x,y = bfs_q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                bfs_q.append((new_x,new_y))
                visited[new_x][new_y] = True
                cnt += 1
    
    return cnt


for _ in range(k):
    x, y = start_pts[_]
    bfs_q.append((x-1,y-1))
    visited[x-1][y-1]  = True
    

bfs()



ans = sum([
    1
    for i in range(n)
    for j in range(n)
    if visited[i][j]
])
  
    

print(ans)