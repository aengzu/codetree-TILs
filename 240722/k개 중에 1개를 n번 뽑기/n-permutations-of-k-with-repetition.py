k, n = tuple(map(int, input().split()))
arr = []


def make_p(cnt):
    if cnt > n:
        if len(arr)==n:
            for elem in arr:
                print(elem, end=' ')
            print()
        return
    
    for i in range(1, k+1):
        arr.append(i)
        make_p(cnt+1)
        arr.pop()
        make_p(cnt+1)
    

make_p(1)