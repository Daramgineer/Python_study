a, b = map(int, input().split())
c = int(input())
m = c%60
h = c//60
if (((m+b) < 60) and ((a+h) < 24)):
    print("{0} {1}".format(a+h, m+b))
elif (((m+b) < 60) and ((a+h) >= 24)):
    print("{0} {1}".format((a+h-24), m+b))
elif (((m+b) >= 60) and ((a+h) < 23)):
    print("{0} {1}".format(a+h+1, (m+b-60)))
elif (((m+b) >= 60) and ((a+h) == 23)):
    print("{0} {1}".format(0, (m+b-60)))
elif (((m+b) >= 60) and ((a+h) >= 24)):
    print("{0} {1}".format((a+h-23), (m+b-60)))