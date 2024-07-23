n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
max_v = 0

def make_p(cnt, selected_cols, current_sum):
    global max_v
    
    if cnt == n:
        max_v = max(max_v, current_sum)
        return 
    
    for j in range(n):
        if j not in selected_cols:
            make_p(cnt + 1, selected_cols + [j], current_sum + arr[cnt][j])

make_p(0, [], 0)
print(max_v)