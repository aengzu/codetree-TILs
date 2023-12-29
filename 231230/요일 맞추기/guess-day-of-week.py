m1, d1, m2, d2 = list(map(int, input().split()))

def calculate_date(m1, d1):
    sum = 0
    # 1월 기준 날짜 계산 
    for i in range(1, m1):
        if i==4 or i==6 or i==9 or i==11:
            sum += 30
        elif i==2:
            sum += 28
        else:
            sum += 31
        
    sum += d1
    return sum
    
sum_1 = calculate_date(m1,d1)
sum_2 = calculate_date(m2, d2)

x = sum_2 - sum_1
x = x%7

if x==0:
    print("Mon")
elif x==1:
    print("Tue")
elif x==2:
    print("Wed")
elif x==3:
    print("Thu")
elif x==4:
    print("Fri")
elif x==5:
    print("Sat")
else:
    print("Sun")