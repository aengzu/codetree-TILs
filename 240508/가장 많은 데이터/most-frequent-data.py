# 문자열 데이터 n 개가 주어졌을 때 문자열 K 가 몇 번째로 주어졌는지 판단하려면 최대 n 번 순회해야한다. 
# => 시간복잡도 O(N)
# 문자열이 만약 배열의 index 처럼 쓰인다면 dict 를 이용하여 O(1) 만에 찾을 수 있다.

n = int(input())

colors = {}
max_cnt = 0

for _ in range(n):
    word = input()
    if word not in colors:
        colors[word] = 1
    else:
        colors[word] += 1
        max_cnt = max(max_cnt, colors[word])


print(max_cnt)