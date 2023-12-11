n = int(input())

class Number:
    def __init__(self, num, index):
        self.num = num
        self.index = index


num = list(map(int, input().split()))
data = [    Number(number, i)
            for i, number in enumerate(num)]
#data 에는 입력된 숫자가 인덱스로 들어감
data.sort(key=lambda x: (x.num, x.index))
answer = [0] * n
# 데이터가 3 1 6 2 7 30 1
# 정렬되면 1(2) 1(7) 2(4) 3(1) 6(3) 7(6) 30(6) 이됨
# 그렇다면 앞에서부터 해당하는 수의 인덱스의 위치에 찐덱스를 넣어줌
#         4   1     5     3
for i , number in enumerate(data):
    # data에서 i 번쨰 인덱스와 number 를 가져온다. number의 인덱스에 해당하는 위치에 i번째임을 넣어줌
    answer[number.index] = i+1

for i in range(n):
    print(answer[i], end = ' ')