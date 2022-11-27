a, b = map(int, input().split())
if (45<=b):
    print("{0} {1}".format(a,b-45))
elif ((0<a<=23) and (b<45)):
    print("{0} {1}".format(a-1,60-(45-b)))
elif ((a==0) and (b<45)):
    print("{0} {1}".format(23,60-(45-b)))