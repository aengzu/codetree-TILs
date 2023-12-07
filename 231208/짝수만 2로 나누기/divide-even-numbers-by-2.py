n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

def print_arr(arr):
    for  elem in arr:
        if elem % 2==0:
            print(elem, end=' ')
        else:
            print(elem, end=' ')

print_arr(arr)