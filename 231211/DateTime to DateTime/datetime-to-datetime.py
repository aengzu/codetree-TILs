a, b, c = list(map(int, input().split()))


def howmuchtime(a, b, c):
    if a==11 and (b<11 or (b==11 and c<11)):
        return -1
    
    sum_min = c+b*60+a*24*60
    eleven_min = 11+11*60+11*60*24

    return sum_min-eleven_min

print(howmuchtime(a,b,c))