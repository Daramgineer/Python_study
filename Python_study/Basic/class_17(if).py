weather = input('오늘날씨는 어때요? ') #str 형태로 입력받아서 저장

if weather == '비' or '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물이 없어요')


temp = int(input('기온은 어때요?')) #int 형태로 입력받아서 저장

if 30 <= temp:
    print('너무더워요')
elif 10<=temp and  temp <30:
    print('쾌적해요')
elif 0<=temp<10:
    print('쌀쌀해요')
else : 
    print('추워요')