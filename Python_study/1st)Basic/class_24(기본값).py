def profile(name, age, main_lang):
    print('이름 : {0}\t나이: {1}\t언어 : {2}'.format(name, age, main_lang))

profile('A', 28, 'python')
profile('B', 12, 'java')

#나이가 같고 언어가 같을 때,
def profile(name, age=21, main_lang='python'):
    print('이름 : {0}\t나이: {1}\t언어 : {2}'.format(name, age, main_lang))

profile('A')
profile('B')