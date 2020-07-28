# Chapter01 -1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생1
student_name_1 = "Kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender' : 'Mail'},
    {'score1' : 95},
    {'score2' : 88}
]

# 학생2
student_name_2 = "Lee"
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender' : 'Female'},
    {'score1' : 77},
    {'score2' : 92}
]

# 학생3
student_name_3 = "Park"
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender' : 'Male'},
    {'score1' : 99},
    {'score2' : 100}
]

# 리스트 구조
# 관리하기 불편
# 데이터의 정확한 위치(인덱스) 매핑 해서 사용
student_names_list = ['Kim', 'Lee', 'Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender' : 'Male', 'score1' : 95, 'score2' : 88},
    {'gender' : 'Female', 'score1' : 77, 'score2' : 92},
    {'gender' : 'Male', 'score1' : 99, 'score2' : 100}
]

# 학생 삭제
del student_names_list[1] # 'Lee'삭제
del student_numbers_list[1] # 2 삭제
del student_grades_list[1] # 2 삭제
del student_details_list[1] # 1번째 dict 삭제

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
# 클래스는 속성과 메소드를 가진다. 메소드가 없어도(pass)된다.
class Student():
    def __init__(self, name, number, grade, details): # 속성
        self._name = name
        self._number = number
        self._grade = grade
        self._detils = details

    def __str__(self): # 객체를 집어넣으면 그안에 내용을 보여주는 기능이다.
        return 'str : {} - {}'.format(self._name, self._number)

    def __repr__(self): # 
        return 'repr : {} - {}'.format(self._name, self._number)

student1 = Student('Kim', 1, 1, {'gender' : 'Male', 'score1' : 95, 'score2' : 88})
student2 = Student('Lee', 2, 2, {'gender' : 'Female', 'score1' : 77, 'score2' : 92})
student3 = Student('Park', 3, 4, {'gender' : 'Male', 'score1' : 99, 'score2' : 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)

print()
print()

# 반복(__str__) = 객체를 집어넣으면 그안에 내용을 보여주는 기능이다.
for x in students_list:
    print(repr(x))
    print(x)
# 두 가지 메서드를 만든다면 __str__ 메서드가 호출한다.
