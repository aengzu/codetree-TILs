n = int(input())
arr = [0] * 101

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    for i in range(x1, x2+1):
        arr[i] += 1
    
    
all_insect = False

for i in range(len(arr)):
    if arr[i] == n:
        all_insect = True
        break

if(all_insect):
    print("Yes")
else:
    print("No")