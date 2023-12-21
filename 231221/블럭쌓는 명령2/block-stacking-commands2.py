n, k = tuple(map(int, input().split()))

blocks = [0]*(n+1)

for _ in range(k):
    start, end = tuple(map(int, input().split()))
    for i in range(start, end+1):
        blocks[i] += 1
    
# max(배열) : 배열의 최댓값
print(max(blocks))