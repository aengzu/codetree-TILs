n, k = tuple(map(int, input().split()))

arr = list(map(int, input().split()))
nums = dict()


for elem in (arr):
    if elem in nums:
        nums[elem] += 1
    else :
        nums[elem] = 1


new_arr = [
    [value, key]
    for key, value in nums.items()
]

new_arr = sorted(new_arr, reverse=True)



for i in range(k):
    print(new_arr[i][1], end=" ")