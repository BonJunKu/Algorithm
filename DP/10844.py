import sys
input=sys.stdin.readline
N=int(input())
anslist=[[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,1]]
for i in range(2,N+1):
    nextlist=[]
    for j in range(0,10):
        if j==0:
            nextlist.append(anslist[i-1][1])
        elif j==9:
            nextlist.append(anslist[i-1][8])
        else:
            nextlist.append(anslist[i-1][j-1]+anslist[i-1][j+1])
    anslist.append(nextlist)
print(sum(anslist[N])%(10**9))