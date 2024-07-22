k, n = tuple(map(int, input().split()))
arr = []

def make_p(cnt):

    if cnt > n:
        for elem in arr:
            print(elem, end=' ')
        print()
        return


    for i in range(1, k+1):
        if arr.count(i) >= 2:
            continue
        arr.append(i)
        make_p(cnt+1)
        arr.pop()

make_p(1)