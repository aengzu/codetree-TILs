import sys

rect = [
    list(map(int, input().split()))
    for _ in range(2)
]


MAX_R = 2000
OFFSET = 1000

area = [[0] * (MAX_R+1)
        for _ in range(MAX_R+1)
]

for i, (x1, y1, x2, y2) in enumerate(rect, start=1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            area[x][y] = i

min_x, min_y = MAX_R, MAX_R
max_x, max_y = 0, 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if area[i][j] == 1:
            min_x = min(i, min_x)
            min_y = min(j, min_y)
            max_x = max(i, max_x)
            max_y = max(j, max_y)


if min_x==MAX_R:
    print(0)
else:
    print((max_x-min_x+1)*(max_y-min_y+1))