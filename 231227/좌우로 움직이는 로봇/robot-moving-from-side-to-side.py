n, m = tuple(map(int, input().split()))

MAX_S = 10000000
a_dst = [0] * (MAX_S+1)
b_dst = [0] * (MAX_S+1)

a_idx = 1
for _ in range(n):
    t, d = tuple(input().split())
    for i in range(int(t)):
        a_dst[a_idx] = a_dst[a_idx - 1] + (1 if d=='R' else -1)
        a_idx += 1

b_idx = 1
for _ in range(m):
    t, d = tuple(input().split())
    for i in range(int(t)):
        b_dst[b_idx] = b_dst[b_idx - 1] + (1 if d=='R' else -1)
        b_idx += 1


if a_idx < b_idx:
    for i in range(a_idx, b_idx):
        a_dst[i] = a_dst[i-1]
elif a_idx > b_idx:
    for i in range(b_idx, a_idx):
        b_dst[i] = b_dst[i-1]

cnt = 0
t_max = max(a_idx, b_idx)
for i in range(1, t_max):
    if a_dst[i] == b_dst[i] and a_dst[i-1] != b_dst[i-1]:
        cnt += 1

print(cnt)