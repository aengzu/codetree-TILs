# 입력 받기
a, b = map(int, input().split())
n = input()

# a진수 -> 10진수 변환
def atoten(n, a):
    num = 0
    for i, digit in enumerate(n[::-1]):
        num += int(digit) * (a ** i)
    return num

# 10진수 -> b진수 변환
def tentob(n, b):
    if n == 0:
        return '0'
    bdigit = []
    while n > 0:
        bdigit.append(str(n % b))
        n //= b
    return ''.join(bdigit[::-1])

# 변환 과정
n_10 = atoten(n, a)  # a진수에서 10진수로
n_b = tentob(n_10, b)  # 10진수에서 b진수로

# 결과 출력
print(n_b)