n, k = tuple(map(int, input().split()))


nums = {}

arr = list(map(int, input().split()))
ans = 0

for elem in arr:
    dff = k - elem
    if diff in nums:
        asn += nums[diff]
    if elem in nums:
        nums[elem] += 1
    else:
        nums[elem] = 1

print(ans)