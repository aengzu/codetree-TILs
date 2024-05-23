# 파이썬에서 우선순위 큐 사용하고자 한다면 heqpq 를 사용해 우선순위 큐를 대신하여 이용한다.
# 단, heapq는 min-heap이므로 이를 max-heap처럼 사용하기 위해서는 
# 넣는 값에 -를 붙여 관리하여 마치 최댓값이 골라지는 것과 같은 효과를 만들어내야함.
import heapq

n = int(input())

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        if self.items is []:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        return -heapq.heappop(self.items)
    
    def top(self):
        return -self.items[0]


q = PriorityQueue()

for i in range(n):
    cmds = list(input().split())
    c = cmds[0]
    if c == 'push':
        option = int(cmds[1])
        q.push(option)
    elif c=='size':
        print(q.size())
    elif c == "empty":
        print(q.empty())
    elif c=='pop':
        print(q.pop())
    else:
        print(q.top())