n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_partition():
    la, lb = len(a), len(b)
    # 만약 b 의 크기가 더 크면 더 볼 필요도 없이 False 임.
    if la < lb :
        return False
    for i in range(la):
        #만약 b의 첫번쨰 원소와 같다면
        if a[i] == b[0]:
            for j in range(lb):
                if a[i+j] != b[j]:
                    return False
            return True
        return False



if is_partition():
    print("Yes")
else:
    print("No")