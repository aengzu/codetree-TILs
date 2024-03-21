from collections import deque # collections 에서 deque 임포트하기

# bfs 는 시작점 기준 가까운 곳부터 순서대로 탐색함.

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
# 뱀이 없으면 1, 뱀이 있으면 0

# bfs 는 큐가 필요
q = deque()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y<m

def can_go(x,y):
    # 범위내에 있고 뱀이 없고(1) 방문 기록 없으면 True
    return in_range(x,y) and grid[x][y] and not visited[x][y]

def bfs():
    # 큐에 남은 것이 없을 때까지 반복한다.
    while q:
        # 큐에서 가장 먼저 들어온 원소를 내보냄
        x, y = q.popleft()
        # 큐에서 뺀 원소의 위치를 기준으로 4방향을 확인함
        dxs, dys = [0,1,0,-1], [1,0,-1,0] # 오, 아, 왼, 위
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부를 표시해줍니다.
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
            

# bfs 를 이용해 최소 이동 횟수를 구한다. 
q.append((0,0))
visited[0][0] = True

bfs()

# 최종지점 방문 기록 있으면 1, 없으면 0
answer = 1 if visited[n-1][m-1] else 0

print(answer)