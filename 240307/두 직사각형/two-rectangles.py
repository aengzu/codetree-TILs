x1, y1, x2, y2 = list(map(int, input().split()))
a1, b1, a2, b2 = list(map(int, input().split()))

def is_overlapping(x2, y2, a1, b1, x1,y1,a2,b2):
    if x2 < a1 or y2 < b1 or b2 < y1 or a2 < x1:
        return False
    else:
        return True

if(is_overlapping(x2,y2,a1,b1,x1,y1,a2,b2)):
    print("overlapping")
else:
    print("nonoverlapping")