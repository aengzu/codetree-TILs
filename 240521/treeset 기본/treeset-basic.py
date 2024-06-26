from sortedcontainers import SortedSet

n = int(input())


s = SortedSet()

for i in range(n):
    cmds = list(input().split())
    if cmds[0] == 'add':
        s.add(int(cmds[1]))
    elif cmds[0] == 'largest':
        if s:
            print(s[-1])
        else:
            print("None")
    elif cmds[0] == 'smallest':
        if s:
            print(s[0])
        else:
            print("None")
    elif cmds[0] == 'remove':
        s.remove(int(cmds[1]))
    elif cmds[0] == 'lower_bound':
        idx = s.bisect_left(int(cmds[1]))
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
    elif cmds[0] == 'upper_bound':
        idx = (s.bisect_right(int(cmds[1])))
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
    else:
        if int(cmds[1]) in s:
            print("true")
        else:
            print("false")