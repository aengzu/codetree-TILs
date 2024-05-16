n = int(input())

s1 = list(map(int, input().split()))

m = int(input())
s2 = list(map(int, input().split()))

set1 = set(s1)

for elem in s2:
    if elem in set1:
        print('1', end=' ')
    else:
        print('0', end=' ')