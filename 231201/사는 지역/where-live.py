class DB:
    def __init__(self, name, add, reg):
        self.name = name
        self.add = add
        self.reg = reg


n = int(input())
arr = []
for i in range(n):
    name, add, reg = list(input().split())
    arr.append(DB(name, add, reg))

target_idx = 0
# for - in enumerate(배열) 꼴 기억해두기
for i, person in enumerate(arr):
    if person.name > arr[target_idx].name:
        target_idx = i

print(f"name {arr[target_idx].name}")
print(f"addr {arr[target_idx].add}")
print(f"city {arr[target_idx].reg}")