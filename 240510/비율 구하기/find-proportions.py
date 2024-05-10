# 알파벳 대, 소문자만으로 이루어진 문자열들 주어졌을 때, 그 문자열이 전체 중 어느정도 비율 차지하는 지 구하기
from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

# 주어진 문자열 사전순으로 출력
arr = list(
    input()
    for _ in range(n)
)

for elem in arr:
    if elem in sd:
        sd[elem] += 1
    else:
        sd[elem] = 1

size = len(arr)


# 차지하는 비율을 백분율로 소수점 4번째까지 반올림하여 공백두고 출력
for k, v in sd.items():
    ratio = v / size * 100
    print(f"{k} {ratio:.4f}")