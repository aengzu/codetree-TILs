n = int(input())

strs = [
    input()
    for _ in range(n)
]

result = ""
for elem in strs:
    result += elem
print(result)