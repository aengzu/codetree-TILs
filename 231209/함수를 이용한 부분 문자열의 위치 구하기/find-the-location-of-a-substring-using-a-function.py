text = input()
pattern = input()
idx = []

def is_substr():
    n, m = len(text), len(pattern)
    # text < pattern 이라면 부분 문자열 성립불가
    if n < m:
        return False
    
    for i in range(n):
        # 만약 패턴의 첫 시작 부분과 일치하는 문자가 등장한다면
        flag = True
        if pattern[0] == text[i]:
            #패턴의 길이만큼 살펴봐야함
            for j in range(m):
                if i+j > n-1:
                    break
                if pattern[j] != text[i+j]:
                    flag = False
                    break
            
            # 만약 flag true 라면 text 내에 부분 문자열 pattern 존재함을 의미한
            if flag:
                idx.append(i)
                return True
    
    return False
                

if is_substr()==True:
    print(idx[0])
else:
    print(-1)