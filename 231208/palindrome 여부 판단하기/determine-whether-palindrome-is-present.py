_str = input()

def is_pelindrome(_str):
    for i in range(len(_str)):
        if _str[i] != _str[len(_str)-i-1]:
            return False

    return True
    
if is_pelindrome(_str):
    print('Yes')
else:
    print('No')