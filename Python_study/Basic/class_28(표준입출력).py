print('python' , 'java')
print('python' , 'java', sep=",") #sep : 띄어쓰기 부분을 ,로 치환
print('python' , 'java', 'c++', sep=' vs ')
print('python', 'java', sep=',', end='?') #end : 성분 끝에 ?붙임
print('무엇이 더 재밌을까요?')

import sys
print('python', 'java', file=sys.stdout) #표준출력
print('python', 'java', file=sys.stderr) #표준에러

scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':') #왼쪽으로 정렬하는데 8칸을 확보한 후. 오른쪽으로 정렬하는데 4칸 확보한 후.

for number in range(1, 21):
    print('대기번호 : ' + str(number).zfill(3)) #3칸 확보 후, 값이없는건 0으로 채움 001, 002,

answer = int(input('아무거나 입력하세요 : '))
print(answer)