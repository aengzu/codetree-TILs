n, m = tuple(map(int, input().split()))

g = [[] for _ in range(n+1)]

for i in range(m):
    x, y = tuple(map(int, input().split()))
    g[x].append(y)
    g[y].append(x)


visited = [0 for _ in range(n+1)]

def dfs(node):
    if visited[node]:
        return
    visited[node] = 1 
    for next_node in g[node]:
        dfs(next_node)

dfs(1)
cnt = 0
for i in visited:
    if i==1:
        cnt += 1
print(cnt-1)