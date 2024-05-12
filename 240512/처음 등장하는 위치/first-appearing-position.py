from sortedcontainers import SortedDict

n= int(input())

nums = list(map(int, input().split()))

num_tm = SortedDict()

for i, elem in enumerate(nums):
    if elem in num_tm:
        continue
    else:
        num_tm[elem] = i+1 

for k, v in num_tm.items():
    print(k, v)