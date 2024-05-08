# 주어지는 숫자의 범위가 작다면 배열로 해결 가능
# But 범위가 크다면? 배열 사용시 메모리 낭비 심할 수 있으므로 dict 사용하기
# dict 는 숫자 범위와 무관하게 n 개의 숫자에 대한 메모리만 사용한다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))

nums = dict()

for elem in arr:
    if elem not in nums:
        nums[elem] = 1
    else:
        nums[elem] += 1

query = list(map(int, input().split()))

for elem in query:
    if elem not in nums:
        # 만약 없다면 처리
        print(0, end=" ")
    else:
        print(nums[elem], end=" ")