weight = int(input())

if weight%5 == 0:
    print(weight//5)

else:
    x = weight//5
    y = weight//3
    p = (weight-5*x)//3
    q = (weight%5)%3

    if (x == 0) & (q != 0):
        print(-1)

    elif (x == 0) & (q == 0):
        print(y)

    elif (q == 0):
        print(x+p)

    else: 
        while q != 0:
            x = x - 1
            y = (weight-(5*x))//3
            q = (weight-(5*x))%3
            
            if q == 0:
                print(x+y)

            elif (x == 0) & (q != 0):
                print(-1)
                break