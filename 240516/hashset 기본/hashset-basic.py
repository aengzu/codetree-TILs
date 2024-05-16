# Pyhon 에는 set 이라는 클래스 존재
# set 은 HashSet 자료구조로 되어있고, HashSet 의 해싱을 기반으로 데이터를 관리한다.
# 따라서 삽입, 삭제, 탐색은 O(1), HashSet 은 빠르지만 순서를 나타내지는 못한다.
n = int(input())

s = set()

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'find':
        if cmd[1] in s:
            print("true")
        else:
            print("false")
    elif cmd[0] == 'add':
        s.add(cmd[1])
    elif cmd[0] == 'remove':
        s.remove(cmd[1])
    else:
        print('error')