n = int(input())  # 마을의 크기 입력

villedges = [list(map(int, input().split())) for _ in range(n)]  # 마을의 지도 입력

# 이동 방향: 오른쪽, 왼쪽, 아래, 위
drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]

# 방문 여부를 기록하는 배열
visited = [[0] * n for _ in range(n)]

def in_range(r, c):
    # 좌표가 범위 내에 있는지 확인하는 함수
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    # DFS를 통해 연결된 사람의 수를 찾는 함수
    visited[r][c] = 1  # 현재 위치를 방문 처리
    count = 1  # 현재 사람 포함하여 카운트

    # 4방향으로 탐색
    for dr, dc in zip(drs, dcs):
        new_r, new_c = r + dr, c + dc
        # 새로운 좌표가 범위 내에 있고, 방문하지 않았으며, 사람이 있는 경우
        if in_range(new_r, new_c) and not visited[new_r][new_c] and villedges[new_r][new_c] == 1:
            count += dfs(new_r, new_c)  # 재귀적으로 연결된 사람 수 누적
    
    return count  # 현재 연결된 사람의 총 수 반환

people_nums = []  # 각 마을의 사람 수를 저장할 리스트
for i in range(n):
    for j in range(n):
        # 방문하지 않았고 사람이 있는 경우 DFS 시작
        if villedges[i][j] == 1 and not visited[i][j]:
            people_num = dfs(i, j)
            people_nums.append(people_num)  # 결과를 리스트에 추가

people_nums.sort()  # 사람 수를 오름차순으로 정렬
print(len(people_nums))  # 총 마을의 수 출력
for num in people_nums:
    print(num)  # 각 마을의 사람 수 출력