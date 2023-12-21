n = int(input())

OFFSET = 100
MAX_R = 200
checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            checked[i][j]=1


# 직사각형 넓이의 총 합을 구합니다.
area = 0
for x in range(0, MAX_R + 1):
    for y in range(0, MAX_R + 1):
        if checked[x][y]:
            area += 1

print(area)