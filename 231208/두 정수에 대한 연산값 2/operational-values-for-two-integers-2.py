a, b = tuple(map(int, input().split())

def modify_num(a, b):
    if a<b:
        a += 10
        b *=2
        return a,b
    else:
        a *=2
        b += 10
        return a,b

print(modify_num(a,b)[0], modify_num(a,b)[1])