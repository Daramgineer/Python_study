from cgi import print_form


print('a' + 'b') #ab
print('a', 'b') #a b

print('나는 28살 입니다.')
print('나는 %d살 입니다' %28) #정수
print('나는 %s를 좋아해요.' %'파이썬') #문자
print('apple 은 %c로 시작해요.' %'a') #단어

print('나는 %s살 입니다' %28) #정수
print('나는 %s색과 %s색을 좋아해요.' %('파란', '빨간'))

print('나는 {}살입니다.'.format(28))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))

print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 28, color ='빨간'))

age = 28
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')