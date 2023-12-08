n = int(input())

arr = list(map(int, input().split()))

def make_abs(arr):
    for elem in arr:
        print(abs(elem), end=' ')

make_abs(arr)