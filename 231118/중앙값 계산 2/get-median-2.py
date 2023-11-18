n = int(input())

arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    #홀수일때
    if i%2==0:
        idx = int(i/2)
        print(arr[idx], end=" ")