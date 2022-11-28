class NumRangeError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print('나누기 전용 계산기')
    nums = []
    nums.append(int(input('첫번째 수')))
    nums.append(int(input('두번째 수')))

    if nums[0] >= 10 or nums[1] >= 10:
        raise NumRangeError('입력값 : {0}, {1}'.format(nums[0], nums[1]))
    nums.append(int(nums[0] / nums[1]))
    print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
except ValueError: #오류발생시 출력후 정상종료
    print('입력오류')
except ZeroDivisionError as err: #division by zoro 출력(오류원인)
    print(err)
except NumRangeError as err:
    print('한자리 수만 입력하세요.')
    print(err)
finally:
    print('계산종료')
