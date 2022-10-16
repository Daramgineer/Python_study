absent = [2, 5] #결석
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student == 7:
        print('{0}번, 교무실로 따라오세요'.format(student))
        break
    print('{0}번, 읽어보세요'.format(student))