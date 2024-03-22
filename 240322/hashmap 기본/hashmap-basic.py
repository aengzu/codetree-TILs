# 파이썬의 dict class 는 HashMap 자료구조로 되어있음. HashMap 은 해싱 기반으로 데이터 관리
# (key, value) 쌍

n = int(input())

hm = dict()

while(True):
    if n==0:
        break
    command = list(input().split())
    k = command[1]
    if command[0]=='add':
        v = command[2]
        hm[int(k)] = int(v)
    elif command[0]=='find':
        print(hm.get(int(k)))
    elif command[0]=='remove':
        del hm[int(k)]
    else:
        print('error')
    n -= 1