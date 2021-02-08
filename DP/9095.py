import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n = int(input())
    anslist=[0,1,2,4]+[0]*(n-3)
    for i in range(4,n+1):
        anslist[i]=anslist[i-1]+anslist[i-2]+anslist[i-3]
    print(anslist[n])