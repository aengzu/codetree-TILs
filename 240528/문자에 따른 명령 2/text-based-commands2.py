x, y = 0,0
         # 서 0 , 북 1, 동 2, 남 3
dx, dy = [-1, 0, 1, 0],[0, 1, 0, -1]

cmd = input()
#처음 디폴트는 북쪽
dir_num = 1

for i in range(len(cmd)):
    #왼쪽으로 90도 회전
    if cmd[i]=='L':
        dir_num -= 1
        dir_num %= 4
        

    #오른쪽으로 90도 회전
    elif cmd[i]=='R':
        dir_num += 1
        dir_num %= 4

    else :
        #한칸이동
        x, y = x+dx[dir_num], y+dy[dir_num]


print(x, y)