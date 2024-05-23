import heapq
n,m = tuple(map(int, input().split()))

pq = []

arr = list(map(int, input().split()))

for elem in arr:
    heapq.heappush(pq, -elem)

for i in range(m):
    k = -heapq.heappop(pq) - 1
    heapq.heappush(pq, -k)

print(-pq[0])