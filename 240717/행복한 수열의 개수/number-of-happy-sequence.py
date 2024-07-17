n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]



# 열을 체크 
def check_in_cols(arr, m):
    result = 0
    # 열
    for j in range(n):
        for i in range(n-m+1):
            first_num = arr[i][j]
            is_happy = True
            for k in range(i+1, i+m):
                if arr[k][j] != first_num:
                    is_happy = False
                    break
            if is_happy:
                result += 1
                break

    return result

            
                
# 행을 체크 
def check_in_rows(arr, m):
    result = 0
    # 행
    for i in range(n):
        for j in range(n-m+1):
            first_num = arr[i][j]
            is_happy = True
            for k in range(j+1, j+m):
                if arr[i][k] != first_num:
                    is_happy = False
                    break
            if is_happy:
                result += 1
                break
    return result

def check_happy_cnt(arr, m):
    result = 0
    result += check_in_cols(arr, m)
    result += check_in_rows(arr, m)
    return result

print(check_happy_cnt(arr, m))