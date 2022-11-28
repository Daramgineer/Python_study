jumin = '990120-1234567' #0부터 indexing

print("성별 : " + jumin[7]) #8번째 출력
print('출생연도 : ' + jumin[0:2]) #0부터 2직전까지 출력
print('생일 : ' + jumin[2:6]) #2부터 6직전까지 출력
print('주민번호 앞자리 : ' + jumin[:6]) #0부터 6직전까지
print('주민번호 뒷자리 : ' + jumin[7:]) #7부터 끝까지

print('주민번호 뒷자리 : ' + jumin[-7:]) #맨뒤에부터 count (-1부터 indexing)