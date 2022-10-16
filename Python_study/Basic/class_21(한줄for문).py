#출석번호가 1,2,3,4에서 101,102,103,104로 바뀜
from operator import length_hint


student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

#이름을 길이로 변환
student = ['iron man', 'thor', 'spider man']
student = [len(i) for i in student]
print(student)

student = ['iron man', 'thor', 'spider man']
student = [i.upper() for i in student]
print(student)