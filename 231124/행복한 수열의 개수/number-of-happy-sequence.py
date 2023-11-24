n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0
cnt = [
    0
    for _ in range(n)
]

for i in range(n):
    cnt = [1] * n
    #행
    for j in range(n-1):
        
        #열
        if arr[i][j] == arr[i][j+1]:
            cnt[j] += 1
    for k in range(n):
        if cnt[k]>=m:
            ans += 1
            break

for j in range(n):
    cnt = [1,1,1]
    #행
    for i in range(n-1):
        
        #열
        if arr[i][j] == arr[i+1][j]:
            cnt[j] += 1
   
    for k in range(n):
        if cnt[k]>=m:
            ans += 1
            break

print(ans)