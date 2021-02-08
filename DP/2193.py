import sys
input=sys.stdin.readline
N=int(input())
anslist=[[0,0],[0,1],[1,0],[1,1]]
for i in range(4,N+1):
    anslist.append([sum(anslist[i-1]),anslist[i-1][0]])
print(sum(anslist[N]))