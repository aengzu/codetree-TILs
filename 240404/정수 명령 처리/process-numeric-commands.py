class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if self.size==0:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items[-1]


n = int(input())

st = Stack()
for _ in range(n):
    cmds = list((input().split()))
    if cmds[0]=='push':
        st.push(int(cmds[1]))
    elif cmds[0]=='empty':
        print(st.empty())
    elif cmds[0]=='pop':
        print(st.pop())
    elif cmds[0]=='size':
        print(st.size())
    else:
        print(st.top())