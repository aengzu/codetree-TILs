# 입력으로 두 개의 정수 n과 k를 받습니다.
n, k = tuple(map(int, input().split()))

# 입력으로 n개의 정수를 배열 형태로 받습니다.
arr = list(map(int, input().split()))

# 각 숫자가 배열에 몇 번 등장하는지 저장하는 딕셔너리입니다.
nums = dict()

# 최종적으로 찾은 쌍의 수를 저장할 변수입니다.
ans = 0

# 배열을 순회하면서 각 숫자의 등장 횟수를 세어 nums에 저장합니다.
for i in range(len(arr)):
    # 현재 숫자 arr[i]가 nums에 없다면, 1로 초기화합니다.
    if arr[i] not in nums:
        nums[arr[i]] = 1
    # 이미 nums에 있다면, 등장 횟수를 1 증가시킵니다.
    else:
        nums[arr[i]] += 1

# 배열 arr의 각 요소를 앞에서부터 순회하면서 가능한 쌍을 찾습니다.
for i in range(n):
    # nums에서 현재 숫자 arr[i]의 등장 횟수를 1 감소시켜 중복 계산을 방지합니다.
    nums[arr[i]] -= 1

    # 현재 위치 i보다 앞에 있는 모든 요소 j에 대해 반복합니다.
    for j in range(i):
        # 필요한 쌍을 만들기 위해 k에서 arr[i]와 arr[j]를 뺀 값 diff를 계산합니다.
        diff = k - arr[i] - arr[j]

        # 만약 diff가 nums에 있으면 해당 diff 값을 가진 요소의 개수만큼 정답을 증가시킵니다.
        if diff in nums:
            ans += nums[diff]

# 계산된 쌍의 수를 출력합니다.
print(ans)