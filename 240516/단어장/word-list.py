from sortedcontainers import SortedDict
sd = SortedDict()

n = int(input())

words = [
    input()
    for _ in range(n)
]

for elem in words:
    if elem in sd:
        sd[elem] += 1
    else:
        sd[elem]= 1

for (k,v) in sd.items():
    print(k, v)