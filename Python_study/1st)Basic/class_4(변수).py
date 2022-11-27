#애완동물을 소개하기
#print('우리집 강아지 이름은 코코와 구찌에요')
#print('코코는 8살이고, 구찌는 5살이에요')
#print('코코는 어른일까요? True')

animal = '강아지'
name1 = '코코'
name2 = '구찌'
age1 = 8
age2 = 5
is_adult1 = age1 >= 3
is_adlut2 = age2 >= 3

print('우리집' + animal + '이름은' + name1 + '와' + name2 + '에요')
print(name1 + '는' + str(age1) + '살 이고,' + name2 + '는' + str(age2) + '살 이에요') #정수형 출력시 str 붙임
print(name1, '는', str(age1), '살 이고,', name2, '는', str(age2), '살 이에요') #정수형 출력시 str 붙임
print(name1 + '는 어른일까요?' + str(is_adult1)) #boolena형도 str붙임