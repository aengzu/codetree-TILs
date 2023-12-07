class DB:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

db = []

for _ in range(5):
    name, h, w = list(input().split())
    h, w = int(h), float(w)
    db.append(DB(name, h, w))

db.sort(key=lambda x: x.name)

print("name")
for student in db:
    print(student.name, student.h, student.w)

db.sort(key=lambda x: -x.h)
print()
print("height")
for student in db:
    print(student.name, student.h, student.w)