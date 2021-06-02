t=int(input())
for _ in range(t):
    X,A,B=map(int,input().split())
    print((A+(100-X)*B)*10)
