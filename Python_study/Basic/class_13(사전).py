cabinet = {3:'A', 100:'B'} #key:value
print(cabinet[3]) #A
print(cabinet[100]) #B
print(cabinet.get(3)) #A
#print(cabinet[5]) #오류로 강제종료
print(cabinet.get(5)) #none
print(cabinet.get(5, '사용가능')) #사용가능, 5번이 비어있음
print(3 in cabinet) #True, 3번이 사용중
print(5 in cabinet) #False, 5번이 미사용중

cabinet = {'A-1':'A', 'B-7':'B'}
cabinet['C-2'] = 'C' #C-2를 만들고 C저장. 이미 존재한다면 바꿔치기
cabinet['A-1'] = 'AA'
print(cabinet)

del cabinet['B-7'] #B-7 삭제
print(cabinet.keys()) #key들만 출력
print(cabinet.values()) #value들만 출력
print(cabinet.items()) #key value 짝지어서 출력

cabinet.clear() #내용 삭제
