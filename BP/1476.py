import sys
input=sys.stdin.readline

e,s,m=list(map(int,input().split()))
while not (e==s and s==m):
    x=min(e,s,m)
    if x==e:
        e+=15
    elif x==s:
        s+=28
    else:
        m+=19
print(e)