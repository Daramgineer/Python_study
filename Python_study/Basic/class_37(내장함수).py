#input : 사용자의 입력을 받는 함수
#dir : 어떤 객체를 넘겨줬을 떄, 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #외장함수
print(dir())
import pickle
print(dir())
print(dir(random))

lst = [1,2,3]
print(dir(lst))