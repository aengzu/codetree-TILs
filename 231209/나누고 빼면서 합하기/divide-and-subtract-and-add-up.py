n, m= tuple(map(int, input().split()))

a = list(map(int, input().split()))

def modify(m):
    sum = a[m-1]
    while m!=1:
        if m%2!=0:
            m -= 1
            sum += a[m-1]
        else:
            m = int(m/2)
            sum += a[m-1]
    return sum


print(modify(m))