class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

n = int(input())

students = []
for _ in range(n):
    a, b = tuple(map(int, input().split()))
    students.append(Student(a, b, _+1))

students.sort(key=lambda x: (x.h, -x.w))

for elem in students:
    print(elem.h,elem.w, elem.num)