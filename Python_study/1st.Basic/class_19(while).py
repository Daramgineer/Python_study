customer = 'A'
index = 5
while index >= 1:
    print('{0}, 커피나왔습니다. {1}번 남았어요'.format(customer, index))
    index -=1
    if index == 0:
        print('커피는 폐기처분합니다')


customer = 'B'
person = 'Unknown'
while person != customer :
    print('{0}, 커피나왔습니다.'.format(customer))
    person = input('이름이 뭔가요?')