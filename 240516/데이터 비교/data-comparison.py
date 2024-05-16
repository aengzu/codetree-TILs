n = int(input())

s1 = list(map(int, input().split()))

m = int(input())
s2 = list(map(int, input().split()))

for elem in s2:
    if elem in s1:
        print('1', end=' ')
    else:
        print('0', end=' ')