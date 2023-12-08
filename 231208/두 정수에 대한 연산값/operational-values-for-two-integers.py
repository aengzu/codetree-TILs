a, b = tuple(map(int, input().split()))

def modify_num(a, b):
    if a < b:
        b = b + 25
        a = a*2
        return a, b
    else:
        a = a + 25
        b = b*2
        return a, b

print(modify_num(a, b)[0], modify_num(a,b)[1])