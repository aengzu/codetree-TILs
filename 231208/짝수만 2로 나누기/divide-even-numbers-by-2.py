n = int(input())

arr = [int(input()) for _ in range(n)]

def print_arr(arr):
    for  elem in arr:
        if elem % 2==0:
            print(elem, end=' ')
        else:
            print(elem, end=' ')