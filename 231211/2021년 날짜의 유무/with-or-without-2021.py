M, D = tuple(map(int, input().split()))

def exist_data(M, D):
    if M < 1 or M > 12 or D < 1 or D>31:
        return False
    elif M==2:
        # 2월 일때 28일까지면 OK
        if D > 28:
            return False
    
    elif  M==4 or M==6 or M==9 or M==11:
        if D > 30:
            return False
    return True

if exist_data(M, D):
    print('Yes')
else:
    print('No')