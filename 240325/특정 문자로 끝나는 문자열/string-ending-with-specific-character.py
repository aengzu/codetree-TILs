strs = [
    input()
    for _ in range(10)
]

c = input()
passed = False

for i in range(len(strs)):
    if strs[i][-1] == c:
        passed = True
        print(strs[i])

if not passed:
    print("None")