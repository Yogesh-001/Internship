t=int(input())
for _ in range(t):
    c,C=0,1
    N,K=map(int,input().split())
    s=input()
    for i in range(N):
        if s[i]=="*":
            c+=1
            if c==K:
                print("YES")
                break
        else:
            c=0
    if c!=K:
        print("NO")
