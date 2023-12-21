class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

OFFSET = 1000
MAX_R = 2000

arr = [
    [0] * (MAX_R+1)
    for _ in range(MAX_R+1)
]

x1, y1, x2, y2 = list(map(int, input().split()))
x1, x2 = x1 + OFFSET, x2+OFFSET
y1, y2 = y1 + OFFSET, y2+OFFSET
for i in range(x1,x2):
    for j in range(y1, y2):
        arr[i][j] += 1
x1, y1, x2, y2 = list(map(int, input().split()))
x1, x2 = x1 + OFFSET, x2+OFFSET
y1, y2 = y1 + OFFSET, y2+OFFSET
for i in range(x1,x2):
    for j in range(y1, y2):
        arr[i][j] += 1
x1, y1, x2, y2 = list(map(int, input().split()))
x1, x2 = x1 + OFFSET, x2+OFFSET
y1, y2 = y1 + OFFSET, y2+OFFSET

for i in range(x1,x2):
    for j in range(y1, y2):
        arr[i][j] -= 2

cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j]==1:
            cnt += 1

print(cnt)