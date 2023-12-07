n = int(input())
arr = list(map(int, input().split()))

def print_arr(arr):
    for  elem in arr:
        if elem%2==0:
            print(int(elem/2), end=' ')
        else:
            print(elem, end=' ')

print_arr(arr)