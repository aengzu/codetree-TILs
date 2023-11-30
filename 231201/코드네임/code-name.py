class Grade:
    def __init__(self, codename, grade):
        self.codename = codename
        self.grade = grade

users = []

for _ in range(5):
    code, grade = tuple(input().split())
    users.append(Grade(code, int(grade)))

min_idx = 0
for i in range(1, 5):
    if users[min_idx].grade > users[i].grade:
        min_idx = i

print(users[min_idx].codename, users[min_idx].grade)