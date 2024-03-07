a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))

# 겹치지 않으면 b-a + d-c
# 겹치면 끝점 - 첫점


def is_intersecting(a,b,c,d):
    if b < c or d < a:
        return False
    return True


if(is_intersecting(a,b,c,d)):
    print(max(b,d)-min(a,c))
else:
    print(b-a+d-c)