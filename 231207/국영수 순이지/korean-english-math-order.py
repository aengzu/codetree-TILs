class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []

for _ in range(n):
    name, kor, eng, math = list(input().split())
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(Student(name,kor, eng, math))


# 첫 번째 우선순위는 국어 점수 내림차순
# 국어 점수가 같다면 두 번째 우선순위는 영어 내림차순, 그 다음은 수학 내림차순
students.sort(key=lambda x: (-x.kor, -x.eng, -x.math)) 

for student in students: # 정렬 이후의 결과 출력
    print(student.name, student.kor, student.eng, student.math)