# 숫자가 동일한 연속 부분 수열
# 배열의 직전의 수와 현재 수가 다를 경우에만 개수를 증가시킨다.

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

cnt = 1
c = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        c += 1
    else:
        c = 1
    cnt = max(cnt,c)
print(cnt)