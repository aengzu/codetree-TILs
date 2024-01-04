n, m = tuple(map(int, input().split()))

arr = [[0]*m
        for _ in range(n)]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

# R: 열 +1 / D: 행 +1 / L : 열 -1 / U: 행 -1
dr, dc = [0,1,0,-1], [1,0,-1,0]

r, c = 0,0
d = 0


arr[r][c] = 1

for i in range(2, n*m+1):
    nr, nc = r + dr[d], c + dc[d]
    if not in_range(nr, nc) or arr[nr][nc] != 0:
        d = (d+1)%4
    
    r, c = r + dr[d], c + dc[d]
    arr[r][c] = i
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()