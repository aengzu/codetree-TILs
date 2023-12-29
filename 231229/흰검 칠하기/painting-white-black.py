n = int(input())

# 0 이 시작위치일 때  -100000 ~ +100000 까지 가능
OFFSET = 100000
MAX_T = 200000

map = [0]*(MAX_T+1)
b_cnt = [0]*(MAX_T+1)
w_cnt = [0]*(MAX_T+1)


now_posi = OFFSET
for _ in range(n):
    x, d = tuple(input().split())

    x = int(x)
    if d=='L':
        map[now_posi] = 1
        w_cnt[now_posi] += 1
        for i in range(1, x):
            now_posi = now_posi - 1
            map[now_posi] = 1 #흰색
            w_cnt[now_posi] += 1

            
            
    elif d=='R':
        map[now_posi] = 2
        b_cnt[now_posi] += 1
        for i in range(1, x):
            now_posi = now_posi + 1
            map[now_posi] = 2 #검은색
            b_cnt[now_posi] += 1

            



w, b, g = 0,0,0
for i in range(MAX_T+1):
    if w_cnt[i] >= 2 and b_cnt[i] >= 2:
        g += 1
    elif map[i] == 1:
        w += 1
    elif map[i]==2:
        b += 1
   

print(w,b,g)