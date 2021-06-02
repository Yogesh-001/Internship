# cook your dish here
T=int(input())
for _ in range(T):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m']
    bets=['N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k=input()
    a=k.split()
    c=int(a[0])
    original=0
    a.remove(a[0])
    if c==len(a):
        for i in a:
            b=list(i)
            count=0
            count1=0
            for j in b:
                if j in alpha:
                    count+=1
                elif j in bets:
                    count1+=1
                if count==len(b) or count1==len(b):
                    original+=1
    if original==c:
        print("YES")
    else:
        print("NO")
