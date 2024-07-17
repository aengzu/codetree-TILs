n, r, c = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

results = []
# 상 하 좌 우 
dxs = [0, 0, -1, 1]
dys = [-1,1,0, 0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

x, y = c-1, r-1

def simulation(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y+dy
        if in_range(nx, ny):
            if (arr[ny][nx]>arr[y][x]):
                results.append(arr[ny][nx])
                simulation(nx, ny)
                break
    return results

print(arr[y][x], end=' ')
results = simulation(x,y)
for elem in results:
    print(elem, end=' ')