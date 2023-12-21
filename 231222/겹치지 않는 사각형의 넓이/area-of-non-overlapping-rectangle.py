OFFSET = 1000
MAX_R = 2000

arr = [
    [0] * (MAX_R+1)
    for _ in range(MAX_R+1)
]

# 변수 선언 및 입력
n = 3
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    # OFFSET을 더해줍니다.
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    # 직사각형에 주어진 순으로 1, 2, 3 번호를 붙여줍니다.
    # 격자 단위로 진행하는 문제이므로
    # x2, y2에 등호가 들어가지 않음에 유의합니다.
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = i


cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j]==1 or arr[i][j]==2:
            cnt += 1

print(cnt)