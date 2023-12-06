class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number


n = int(input())


students = []

for i in range(1, n+1):
    height, weight= list(map(int, input().split()))
    students.append(Student(height, weight, i))

# Students 를 키가 큰 순으로(내림차순) -> 키 동일하면 몸무게 순으로(내림차순) -> 동일하면 번호가 (오름차순)
students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in (students):
    print(student.height, student.weight, student.number)