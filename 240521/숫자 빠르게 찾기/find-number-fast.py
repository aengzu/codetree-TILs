n,m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for _ in range(m):
    idx = -1
    target = int(input())
    left, right = 0, n-1
    
    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            idx = mid+1
            break
        if arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    print(idx)