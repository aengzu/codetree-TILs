n,m,k = list(map(int, input().split()))

# 학생의 번호 배열
students = [0] * (n+1)

for i in range(m):
    red = int(input())
    students[red] += 1
    if students[red] >= k:
        print(red)
        break