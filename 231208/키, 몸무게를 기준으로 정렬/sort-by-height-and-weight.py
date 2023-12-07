n = int(input())

class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    
students = []

for _ in range(n):
    name, height, weight = list(input().split())
    height, weight = int(height), int(weight)
    students.append(Student(name, height, weight))

students.sort(key =lambda x: (x.height, -x.weight))

for student in students:
    print(student.name, student.height, student.weight)