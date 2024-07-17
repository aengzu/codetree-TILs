# 1*m 의 블록을 한 행씩 내려야한다.
# 1. 다음 행의 m 개의 열이 비어있는 지 확인
# 2.1 m 개의 행이 다 비어있다면 1*m 블록의 위치를 다음 행으로 내린다.
# 2.2 m 개의 행이 다 비어있지 않다면 종료한다. 

n, m, k = list(map(int, input().split()))
k = k-1
grid = [list(map(int, input().split())) for _ in range(n)]

def is_empty(idx, k, m):
    for j in range(k,k+m):
        if grid[idx][j] == 1:
            return False
    return True


now_idx = 0
for i in range(n):
    if is_empty(i, k, m):
        now_idx += 1
    else:
        for j in range(k, k+m):
            grid[i-1][j] = 1
        break


for i in range(n):
    for j in range(n):
        print(grid[i][j], end= ' ' )
    print()