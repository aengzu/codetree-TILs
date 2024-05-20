n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr2 = set(arr2)
set1 = set(arr1)

for  elem2 in arr2:
    if elem2 not in set1:
        print(0)
    else:
        print(1)