n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

cnt = 1
ans = 1
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt, ans)

print(ans)