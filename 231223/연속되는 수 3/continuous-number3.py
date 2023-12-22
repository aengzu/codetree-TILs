n = int(input())

# 동일 숫자로만 이루어진 연속 부분 수열

arr = [ int(input()) 
        for _ in range(n)]

cnt = 1
ans = 1
for i in range(1, len(arr)):
    # 부호 같을 때
    if arr[i] * arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)
    
print(ans)