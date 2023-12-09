n,m = tuple(map(int, input().split()))

a = list(map(int, input().split()))

def sum_of_interval(a1, a2):
    sum = 0
    for i in range(a1-1, a2):
        sum += a[i]
    print(sum)

for _ in range(m):
    a1,a2 = tuple(map(int, input().split()))
    sum_of_interval(a1, a2)