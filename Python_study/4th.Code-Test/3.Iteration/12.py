a = int(input()) #26
i = 1
e = 0
b = a//10 #2
c = a%10 #6
d = (b+c) #8
e = c*10 + d%10 #68
while a != e:
    b = e//10 #2
    c = e%10 #6
    d = (b+c) #8
    e = c*10 + d%10 #68
    i += 1

print("{0}".format(i))