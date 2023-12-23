n, t = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

ans = 1
cnt = 1
for i in range(1, len(arr)):
    if arr[i] > arr[i-1] and arr[i-1] > t:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

if cnt==1:
    print(0)
else:
    print(ans)