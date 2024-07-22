k, n = tuple(map(int, input().split()))
arr = []

def make_p(cnt):
    if cnt > 3:
        if arr[-1]==arr[-2] and arr[-2]==arr[-3]:
            return 

    if cnt > n:
        for elem in arr:
            print(elem, end=' ')
        print()
        return


    for i in range(1, k+1):
        arr.append(i)
        make_p(cnt+1)
        arr.pop()

make_p(1)