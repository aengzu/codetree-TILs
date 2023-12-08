st = input()

def is_other_alpha_morethantwo(st):
    for i in range(len(st)):
        # 돌아가면서 첫번째 원소와 같지 않다면 True 를 리턴
        # 만약 다 돌았는데 if 문에 들어가지 않는다는 것은
        # 모든 원소들이 첫번째 원소와 같다 즉, 모든 원소가 같다는 뜻이므로 False
        if st[i] != st[0]:
            return True
    
    return False


        
if is_other_alpha_morethantwo(st):
    print("Yes")
else:
    print("No")