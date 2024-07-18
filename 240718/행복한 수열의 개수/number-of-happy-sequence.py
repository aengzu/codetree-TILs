n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]



# 배열을 체크
def check_in_arr(arr, m):
    for i in range(0, n-m+1):
        is_happy = True
        first_num = arr[i]
        for k in range(i, i+m):
            if first_num != arr[k]:
                is_happy = False
                break
    return is_happy


result = 0
for i in range(n):
    if check_in_arr(arr[i], m):
        result += 1


for j in range(n):
    col = [arr[i][j] for i in range(n)]
    if check_in_arr(col, m):
        result += 1

print(result)