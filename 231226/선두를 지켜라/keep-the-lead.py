n, m = tuple(map(int, input().split()))

MAX_T = 1000000

A = [0] * (MAX_T+1)
B = [0] * (MAX_T+1)

# A 의 위치 
a_t = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for i in range(t):
        A[a_t] = A[a_t-1] + v
        a_t += 1
    


# B 의 위치
b_t = 1
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for i in range(t):
        B[b_t] = B[b_t-1] + v
        b_t += 1


# 추월 개수 세기
cnt = 0
leader = 0
for i in range(1, a_t):
    if A[i] > B[i]:
        # 기존 리더가 B 였다면
        if leader == 2:
            cnt += 1
        leader = 1
    elif A[i] < B[i]:
        if leader == 1:
            cnt += 1
        leader = 2

print(cnt)