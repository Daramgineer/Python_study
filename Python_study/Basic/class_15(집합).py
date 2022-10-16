#중복불가능, 순서없음
my_set = {1,2,3,5,5,5}
print(my_set) #중복된 5는 한번만 출력

java = {'A', 'B', 'C', 'D'}
python = set(['A', 'F'])

#교집합
print(java & python) #'A'
print(java.intersection(python)) #'A'

#합집합
print(java | python) #'F','A','B','C','D' 순서보장X
print(java.union(python)) #'F','A','B','C','D' 순서보장X

#차집합
print(java - python) #'C', 'D', 'B'
print(java.difference(python)) #'C', 'D', 'B'

#성분추가
python.add('B')
print(python) #'A','F','B'

java.remove('C')
print(java) #'D', 'B', 'A'