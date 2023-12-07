_str = input()


def is_pelindrome(_str):
    for i in range(len(str)):
        if str[i] != str[len(s)-i-1]:
            return False

    return True
    
if is_pelindrome(_str):
    print('Yes')
else:
    print('No')