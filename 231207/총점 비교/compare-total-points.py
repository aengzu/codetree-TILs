class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

students = [
]

for _ in range(n):
    name, kor, eng, math = list(input().split())
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(Student(name, kor, eng, math))

# 점수의 총합 기준 오름차순
students.sort(key=lambda x: x.kor + x.eng + x.math) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name, student.kor, student.eng, student.math)