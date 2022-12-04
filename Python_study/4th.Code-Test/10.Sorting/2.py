'''import numpy
x = []
for _ in range(5):
    x.append(int(input()))

print(round(numpy.mean(x)))
print(round(numpy.median(x)))''' #numpy 인식 오류? 런타임에러 발생해서 아래로 바꿈

x = []
for i in range(5):
    x.append(int(input()))
x.sort()
print(int(sum(x)/5))
print(x[2])