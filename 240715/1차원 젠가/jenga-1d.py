n = int(input())

genga = [int(input()) for _ in range(n)]
s1,e1 = tuple(map(int, input().split()))
s2,e2 = tuple(map(int, input().split()))
s1,e1 = s1-1, e1-1
s2,e2 = s2-1, e2-1


def do_genga(genga,s,e):
    new_genga = []
    for i in range(len(genga)):
        if i in range(s,e+1):
            continue
        new_genga.append(genga[i])
    return new_genga
    
new_genga = do_genga(genga,s1,e1)
new_genga = do_genga(new_genga,s2,e2)

print(len(new_genga))
for elem in new_genga:
    print(elem)