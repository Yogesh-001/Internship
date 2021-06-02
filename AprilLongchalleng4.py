t=int(input())
for _ in range(t):
    n=int(input())
    a,b,c,d=20,36,51,60
    if n==1:
        print(a)
    elif n==2:
        print(b)
    elif n==3:
        print(c)
    elif n==4:
        print(d)
    else:
        r=n%4
        s=60*(n//4)-4*(n-4)
        if r==1:
            print(s+a)
        elif r==2:
            print(s+b)
        elif r==3:
            print(s+c)
        else:
            print(s)
