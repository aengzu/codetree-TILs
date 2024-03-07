x1, x2, x3, x4 = list(map(int, input().split()))

def is_intersecting(x1, x2, x3, x4):
    if x1<x3 and x3<=x2:
        return True
    elif x3<x1 and x1<=x4:
        return True
    else:
        return False

if(is_intersecting(x1,x2,x3,x4)):
    print("intersecting")
else:
    print("nonintersecting")