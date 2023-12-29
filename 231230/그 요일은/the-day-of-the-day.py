m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()

days_of_weak = ["Mon", "Tue","Wed", "Thu", "Fri", "Sat", "Sun"]
days_in_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def calculate_days(m1, d1):
    sum = 0
    for i in range(1, m1):
        sum += days_in_month[m1]
    sum += d1
    return sum
    
diff = calculate_days(m2, d2) - calculate_days(m1, d1)

rem = diff%7
cals = diff//7 -1

x = days_of_weak.index(A)

if rem < int(x):
    cals += 1

print(cals)