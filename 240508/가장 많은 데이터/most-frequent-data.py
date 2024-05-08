# 문자열 데이터 n 개가 주어졌을 때 문자열 K 가 몇 번째로 주어졌는지 판단하려면 최대 n 번 순회해야한다. 
# => 시간복잡도 O(N)
# 문자열이 만약 배열의 index 처럼 쓰인다면 dict 를 이용하여 O(1) 만에 찾을 수 있다.

# 변수 선언 및 입력:
n = int(input())
words = [input() for _ in range(n)]

freq = dict()
ans = 0

# 각 문자열이 몇 번씩 나왔는지를
# hashmap에 기록해줍니다.
for word in words:
    # 처음 나온 문자열이라면 1을 직접 적어줘야 합니다.
    if word not in freq:
        freq[word] = 1
    # 이미 나와있던 문자열이라면 1을 더해줍니다.
    else:
        freq[word] += 1

    # 가장 많이 나온 횟수를
    # 갱신해줍니다.
    ans = max(ans, freq[word])

print(ans)