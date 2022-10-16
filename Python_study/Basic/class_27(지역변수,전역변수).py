gun = 10

def check(soldiers):
    #gun = 20 #지역변수
    global gun #전역변수
    gun = gun - soldiers
    print('[함수 내] 남은총 : {0}'.format(gun))

def check_ret(gun, soldiers):
    gun = gun - soldiers
    print('함수내 남은총 : {0}'.format(gun))
    return gun #전역변수에 저장

print('전체 총 : {0}'.format(gun))
gun = check_ret(gun,2)
print('남은 총 : {0}'.format(gun))