# A, B 각각의 사람이 매 초마다 어느 위치에 있었는지를 기록하여 두 사람의 시간과 위치가 전부 일치하는 시점을 찾는다.
# d*t = 1000000 이다. 따라서 최대 위치는 100000이 된다.

MAX_T = 1000000

n, m = tuple(map(int, input().split()))

A, B = [0] * (MAX_T+1), [0] *(MAX_T+1)


# a 의 타임 체크
a_idx = 1

for i in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        # 문법 주목 ! A 의 현재 위치는 A 의 바로 이전 위치 + (R 이면 1 을 아니면 -1) 을 해준다.
        A[a_idx] = A[a_idx-1] + (1 if d == 'R' else -1)
        # 한 타임 흘렀다는 의미이므로 +1 을 한다.
        a_idx += 1

# b 의 타임 체크
b_idx = 1

for i in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        # 문법 주목 ! B 의 현재 위치는 B 의 바로 이전 위치 + (R 이면 1 을 아니면 -1) 을 해준다.
        B[b_idx] = B[b_idx-1] + (1 if d == 'R' else -1)
        # 한 타임 흘렀다는 의미이므로 +1 을 한다.
        b_idx += 1

# 둘이 만나는 시간을 구한다
ans = 0
for i in range(1, a_idx):
    if A[i] == B[i]:
        ans = i
        break
print(ans)