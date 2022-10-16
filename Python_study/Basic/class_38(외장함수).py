#glob : 경로 내의 폴터 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob('*.py')) #확장자가 py인 모든 파일 출력

#os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) #현재 디렉토리 표시

folder = 'sample_dir'
if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(folder) #폴더삭제
    print('폴더를 삭제했습니다.')

else:
    os.makedirs(folder) #폴더생성
    print(folder, '폴더를 생성하였습니다.')

print(os.listdir())
력
#time : 시간관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print('오늘 날짜는 ', datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.todat()
dday = datetime.timedelta(days=100) #100일 뒤 날짜 저장
print('우리가 만난지 100일되는 날은 ', today + dday) #오늘부터 100일 후 출력