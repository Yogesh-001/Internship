# cook your dish here
T=int(input())
for _ in range(T):
    a,b,c,d,k=map(int,input().split())
    A=abs(c-a)+abs(d-b)
    if A>k:
        print("NO")
    elif A==k:
        print("YES")
    elif((k-A)%2==0):
        print("YES")
    else:
        print("NO")
