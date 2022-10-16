from cgi import print_form

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(8/2) #4.0 //나누기는 정수가 아닌 실수형으로 출력

print(2**3) #8
print(5%3) #2 //나머지
print(10%3) #1
print(5//3) #1 //몫
print(10//3) #3 //력

print(10>3) #True
print(4>=1) #True
print(3==3) #True
print(3+4==7) #True
print(3+(4==4)) #4 //True = 1
print(3+(4==8)) #3 //False = 0

print(1 != 3) #True //같지않음
print(not(1 != 3)) #False

print((3>0) and (1<9)) #True
print((3>0) & (1<9)) #True

print((3>0) or (1>9)) #True
print((3>0) | (1>9)) #True

print(5>4>3) #True
print(5>4>7) #False

print(abs(-4)) #4
print(pow(3,9)) #19683
print(max(4,12)) #12
print(min(17,99)) #17
print(round(3.1415)) #3 //반올림
print(round(4.9)) #5 //반올림

from math import *
print(floor(4.99)) #4 //내림
print(ceil(3.14)) #4 //올림
print(sqrt(16)) #4 //제곱근