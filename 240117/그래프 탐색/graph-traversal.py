# n: 정점의 개수 / m : 간선의 개수
n, m = tuple(map(int, input().split()))

# index 를 1부터 사용하기 위해 
graph = [[] for _ in range(n+1)]

visited = [false] * (n+1)
vertex_cnt = 0
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global vertex_cnt
    for curr_v in graph[v]:
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)

visited[1] = True
dfs(1)

print(vertex_cnt)