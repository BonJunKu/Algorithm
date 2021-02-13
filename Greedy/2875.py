import sys
input=sys.stdin.readline
n,m,k=list(map(int,input().split()))
ans=0
while(n+m>=k and n>=0 and m>=0):
    n-=2
    m-=1
    if not (n+m>=k and n>=0 and m>=0):
        break
    ans+=1
print(ans)