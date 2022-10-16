def profile_1(name, age, lang1, lang2, lang3):
    print('이름 : {0}\t나이: {1}\t'.format(name,age), end=" ") #줄바꿈없이 이어서 출력
    print(lang1, lang2, lang3)

def profile(name, age, *language):
    print('이름 : {0}\t나이: {1}\t'.format(name,age), end=" ") #줄바꿈없이 이어서 출력
    for lang in language: #있는 성분만 출력
        print(lang, end=" ")
    print()

profile('A', 28, 'python', 'c', 'c++')
profile('B', 17, 'java', 'swift')