# cook your dish here
T=int(input())
for _ in range(T):
    x,m,d=map(int,input().split())
    print(min(x*m,x+d))
