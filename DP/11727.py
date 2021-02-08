import sys
input=sys.stdin.readline
n=int(input())
anslist=[0,1,3]+[0]*(n-2)
for i in range(3,len(anslist)):
    anslist[i]=anslist[i-1]+anslist[i-2]*2
print(anslist[n]%10007)