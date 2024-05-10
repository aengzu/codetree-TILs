# python 에는 treemap 자료구조로 만들어져있는 내장함수가 없기 때문에 외부라이브러리 활용
from sortedcontainers import SortedDict

# SortedDict 는 TreeMap 자료구조로 되어있으며, TreeMap 은 균형잡힌 이진트리 구조로 데이터를 관리해준다. 
# 각 노드에 (key, value) 의 페어로 데이터가 들어있고, key 를 기준으로 노드의 위치가 결정된다.
# TreeMap 에서의 삽입, 삭제, 탐색 등 모든 함수의 시간복잡도는 전부 O(log N)이다.

sd = SortedDict()
# TreeMap 은 SortedDict()로 선언하는 것을 제외하고는 각 함수의 사용이 Python에서의 Dict 사용과 완벽히 동일하다.
n = int(input())

for _ in range(n):
    command = input()

    if command.startswith("add"):
        _, k, v = tuple(command.split())
        k, v = int(k), int(v)
        sd[k] = v

    elif command.startswith("find"):
        k = int(command.split()[1])
        if k not in sd:
            print("None")
        else:
            print(sd[k])
    elif command.startswith("remove"):
        k = int(command.split()[1])
        sd.pop(k)
    else:
        if not sd:
            print("None")
        else: #TreeMap 에선 이미 key 오름차순 정렬되어서 들어감
            for value in sd.values():
                print(value, end=' ')
            print()