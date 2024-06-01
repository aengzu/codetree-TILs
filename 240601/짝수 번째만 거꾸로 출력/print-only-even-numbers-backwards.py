str = input()

even_str = ""

for i in range(len(str)):
    if i % 2 != 0:
        even_str += str[i]

print(''.join(reversed(even_str)))