a, b = tuple(map(int, input().split()))

# n 이 소수인지 판별
def is_prime(n):
    if n==1:
        return False
    
    for i in range(2, n):
        if n%i==0:
            return False 
    return True

# 자릿수의 합이 짝수인지
def is_digit_suum_even(n):
    digit_sum = (n//100) + ((n//10)%10) + (n%10)
    if digit_sum%2==0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_digit_suum_even(i) and is_prime(i):
        cnt += 1

print(cnt)