n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

people_num = 0
people_nums = list()

# 격자를 벗어나는 지 확인
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n


# 주어진 위치로 갈 수 있는지 확인
def can_go(x, y):
    if not in_range(x,y):
        return False
    # 방문했거나 벽이 있으면 못감
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global people_num
    # 0: 오른쪽(열y+1), 1: 아래쪽(행x+1),  2: 왼쪽(열y-1) 3: 위쪽(행x-1)
    dxs, dys = [0,1,0,-1], [1,0,-1,0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True

            people_num += 1
            dfs(new_x, new_y)

# 격자의 각 위치에서 탐색을 시작할 수 있는 경우 
# 한 마을에 대한 dfs 탐색 시작

for i in range(n):
    for j in range(n):
        if can_go(i,j):
            visited[i][j] = True
            people_num = 1

            dfs(i,j)

            # 한 마을 탐색 끝나면 사람 수 넣어두기
            people_nums.append(people_num)


people_nums.sort()

print(len(people_nums))

for i in range(len(people_nums)):
    print(people_nums[i])