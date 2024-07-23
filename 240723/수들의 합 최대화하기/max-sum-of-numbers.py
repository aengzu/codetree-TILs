n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0

def backtrack(row, selected_cols, current_sum):
    global max_sum

    # 종료 조건 달성
    if row == n:
        max_sum = max(max_sum, current_sum)
        return
    
    for col in range(n):
        if col in selected_cols:
            continue
        # 현재 행(row)에서 열(col)을 선택하고 다음 행으로 넘어감
        backtrack(row + 1, selected_cols + [col], current_sum + arr[row][col])

# 초기 호출: 첫 번째 행부터 시작, 선택된 열은 없고 합은 0
backtrack(0, [], 0)

print(max_sum)