n = int(input())

x, y = 0, 0

# W, S, E, N
dx, dy = [-1, 0, 1, 0],[0, -1, 0, 1]

# 0: W, 1: S, 2:E, 3:N

time = 0
c_flg = False

def check(x,y):
    return x==0 and y==0
    
for _ in range(n):
    dir, c = tuple(input().split())
    c = int(c)
    if dir=='N':
        for i in range(c):
            time += 1
            x, y = x+dx[3], y+dy[3]
            if check(x,y):
                c_flg = True
                print(time)
    elif dir=='S':
        for i in range(c):
            time += 1
            x, y = x+dx[1], y+dy[1]
            if check(x,y):
                c_flg = True
                print(time)
    elif dir=='E':
        for i in range(c):
            time += 1
            x, y = x+dx[2], y+dy[2]
            if check(x,y):
                c_flg = True
                print(time)
    else:
        for i in range(c):
            time += 1
            x, y = x+dx[0], y+dy[0]
            if check(x,y):
                c_flg = True
                print(time)


if(c_flg==False):
    print(-1)