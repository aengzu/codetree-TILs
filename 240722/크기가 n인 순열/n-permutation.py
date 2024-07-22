n = int(input())

arr = []
def make_p(cnt):
    if cnt > n:
        for elem in arr:
            print(elem, end=' ')
        print()
        return
    
    for i in range(1, n+1):
        if arr.count(i) >= 1:
            continue
        arr.append(i)
        make_p(cnt+1)
        arr.pop()
    
make_p(1)