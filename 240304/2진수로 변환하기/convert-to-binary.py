n = int(input())

digits = []

while(True):
    if n < 2:
        digits.append(n)
        break
    
    digits.append(n%2)
    n //= 2



# 시작, 종료 미지정이므로 처음부터 끝까지 + -1(역순으로 진행)
for digit in digits[::-1]:
    print(digit, end="")