n, t = map(int, input().split())
left_side = list(map(int, input().split()))
right_side = list(map(int, input().split()))
bottom_side = list(map(int, input().split()))

belt = left_side + right_side + bottom_side


belt_length = 3 * n


t = t % belt_length

belt = belt[-t:] + belt[:-t] 


left_side = belt[:n]
right_side = belt[n:2*n]
bottom_side = belt[2*n:]

print(' '.join(map(str, left_side)))
print(' '.join(map(str, right_side)))
print(' '.join(map(str, bottom_side)))