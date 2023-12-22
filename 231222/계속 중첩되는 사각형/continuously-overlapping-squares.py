n = int(input())

rect = [
    list(map(int, input().split()))
    for _ in range(n)
]

MAX_R = 200
OFFSET = 100

area = [
    [0]*(MAX_R+1)
    for _ in range(MAX_R+1)
]

# 홀수번째는 빨, 짝수번째는 파
#          1          2


for i, (x1,y1,x2,y2) in enumerate(rect, start=1):
    x1, y1 = x1+OFFSET, y1+OFFSET
    x2, y2 = x2+OFFSET, y2+OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            if i%2==0:
                c = 2
            else:
                c=1
            area[x][y] = c


cnt = 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if area[i][j] == 2:
            cnt += 1


print(cnt)