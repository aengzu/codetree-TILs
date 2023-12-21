n = int(input())
## 색종이는 가로세로8이고 넓이 64이다.
# (-100, 100) (-100,100) 범위이므로 오프셋

OFFSET = 100
MAX_R = 200

rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for x1, y1 in rects:
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            arr[i][j] = 1


cnt = 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if arr[i][j] ==1:
            cnt += arr[i][j]
print(cnt)