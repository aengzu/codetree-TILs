n = int(input())
arr = list(map(int, input().split()))

results = ""
for elem in arr:
    results += (str(elem))
print(results)

cnt = len(results) // 5

for i in range(cnt):
	print(results[i], end="")
	if (i + 1) % 5 == 0:
		print()