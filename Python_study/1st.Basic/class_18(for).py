print('대기번호 : 1')
print('대기번호 : 2')
print('대기번호 : 3')

for waiting_num in [1,2,3,4]:
    print('대기번호 : {0}'.format(waiting_num)) #List안에 있는 정보를 순차적으로 가져와서 출력 1,2,3,4,

for waiting_num in range(5):
    print('대기번호 : {0}'.format(waiting_num)) #0,1,2,3,4 출력

for waiting_num in range(1,10):
    print('대기번호 : {0}'.format(waiting_num)) #1,2,3,4,5,6,7,8,9


starbucks = ['A', 'B', 'C', 'D']
for customer in starbucks:
    print('{0}, 커피나왔습니다'.format(customer))