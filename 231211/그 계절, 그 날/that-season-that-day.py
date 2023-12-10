y, m, d = list(map(int, input().split()))


def yunnyeon(y):
    if y%4==0 and y%100==0 and y%400==0:
        return True
    elif y%4==0 and y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False
        
def exist_date(y, m, d):
    if m<1 or m>12 or d<1 or d>32:
            return '-1'
    elif m==4 or m==6 or m==9 or m==11:
            if d>30:
                return '-1'
   
    if yunnyeon(y):
        if m==2 and d>30:
            return '-1'
    
    if 3 <= m and m <=5:
        return 'Spring'
    elif 6 <= m and m <= 8:
        return 'Summer'
    elif 9 <= m and m <= 11:
        return 'Fall'
    else:
        return 'Winter'
    




print(exist_date(y, m,d))