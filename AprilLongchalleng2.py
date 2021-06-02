# cook your dish here
t=int(input())
for _ in range(t):
    k1,k2,k3,v=map(float,input().split())
    a=k1*k2*k3*v
    b=9.58
    #print(a)
    if round(100/a,2)<b:
        print("YES")
    else:
        print("NO")
