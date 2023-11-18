n = int(input())

arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    #홀수일때
    if i%2==0:
        idx = int(i/2)
        arr2 = arr[:i+1]
        arr2.sort()
        print(arr2[idx], end=" ")