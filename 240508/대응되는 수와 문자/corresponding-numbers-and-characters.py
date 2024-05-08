# 대응되는 수와 문자
n, m = tuple(map(int, input().split()))
arr = [
    input()
    for _ in range(n)
]

string_to_num = dict()

for i,elem in enumerate(arr):
    string_to_num[elem] = i+1

for _ in range(m):
    word = input()
    #  ord(문자) : 정수 반환

    if ord(word[0]) >= ord('0') and ord(word[0]) <= ord('9'):
        print(arr[int(word)-1])
    else:
        print(string_to_num[word])