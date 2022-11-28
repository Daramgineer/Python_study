#일반 가격
def price(people):
    print('{0}명 가격은 {1}원 입니다.'.format(people, people*10000))

#일반할인 가격
def price_morning(people):
    print('{0}명의 할인가격은 {1}원 입니다.'.format(people, people*8000))

#군인할인 가격
def price_soldier(people):
    print('{0}명의 할인가격은 {1}원 입니다.'.format(people, people*6000))