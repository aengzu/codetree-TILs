n = int(input())


strs = [list(input())
        for _ in range(n)
]

sum_len = 0
sum_a  = 0
for elem in strs:
    sum_len += len(elem)
    if elem[0] == 'a':
        sum_a += 1

print(sum_len, sum_a, end=" ")