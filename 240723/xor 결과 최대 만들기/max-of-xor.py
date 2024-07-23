n ,m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

ds = []
max_v = 0
def find_max(cnt):
    global max_v

    if cnt > m:
        for elem in ds:
            elem = bin(elem)
        result = ds[0]
        for i in range(1, len(ds)):
            result = result ^ i 
        max_v = max(max_v, result)
        return 
    for i in range(len(arr)):
        ds.append(arr[i])
        find_max(cnt+1)
        ds.pop()
    
find_max(1)
print(max_v)