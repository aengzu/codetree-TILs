st = input()

def is_other_alpha_morethantwo(st):
    for i in range(len(st)):
        if st[i] != st[0]:
            return True
    
    return False


        
if is_other_alpha_morethantwo(st):
    print("Yes")
else:
    print("No")