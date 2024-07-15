n = int(input())

positions = [list(map(int, input().split())) for _ in range(n)]


max_coins = 0

for i in range(n-2):
    for j in range(n-2):
        now_coins = 0
        for k in range(j, j+3):
            now_coins += positions[i][k] 
            now_coins += positions[i+1][k]
            now_coins += positions[i+2][k]
            max_coins = max(now_coins, max_coins)
    
        
print(max_coins)