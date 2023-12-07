a, b = tuple(map(int, input().split()))

def complete_number(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i%2==0:
            continue
        elif i%10==5:
            continue
        elif i%3==0 and i%9!=0:
            continue
        
        cnt += 1
    return cnt


print(complete_number(a, b))