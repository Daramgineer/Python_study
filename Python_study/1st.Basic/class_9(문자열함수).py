python = 'Python is amazing'

print(python.lower()) #모든 글자 소문자 출력
print(python.upper()) #모든 글자 대문자 출력
print(python[0].isupper()) #해당 글자가 대문자인지 True/False
print(len(python)) #글자수 출력
print(python.replace('Python', 'Java')) #Python 글자를 Java로 변경후 출력

index = python.index('n') #첫번째 n 찾기
print(index) #n이 몇번째에 있는지 출력
index = python.index('n', index+1) #두번째 n 찾기
print(index) #n이 몇번째에 있는지 출력

print(python.find('n'))
print(python.find('Java')) #Java는 없으므로 -1 출력

print(python.count('n')) #n이 몇개있는지 count