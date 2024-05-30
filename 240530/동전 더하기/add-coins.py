n, k = tuple(map(int, input().split()))


count = 0

coin_types = [
    int(input())
    for _ in range(n)
]

for coin in reversed(coin_types):
    count += k // coin
    k %= coin

print(count)