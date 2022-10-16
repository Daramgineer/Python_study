#List[] : 순서를 가지는 객체의 집합

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) #[10, 20, 30]

subway = ['A', 'B', 'C']
print(subway) #['A', 'B', 'C']

print(subway.index('B')) #B의 위치 출력 : 1

subway.append('D') #List 맨뒤에 D추가
print(subway) #['A', 'B', 'C', 'D']

subway.insert(1, 'A-1') #중간에 삽입. 
print(subway) #['A', 'A-1', 'B', 'C', 'D']

print(subway.pop()) #List 맨뒤부터 삭제, 삭제정보 출력
print(subway)

subway.append('A')
print(subway)
print(subway.count('A')) #List 안에 'A'가 몇개 있는지 출력

num_list = [3,6,8,2,1]
num_list.sort() #List 정보 순서대로 정렬(오름차순)
print(num_list)

num_list.reverse() #List 정보 역순으로 출력
print(num_list) 

num_list.clear() #List내 모든 정보 삭제
print(num_list)

mix_list = ('A', 18, True) #List 자료형은 상관없음
print(mix_list)

num_list = [5,4,3,2,1]
mix_list = ['A', 'B']
num_list.extend(mix_list) #numList 뒤에 mixList 붙임
print(num_list)