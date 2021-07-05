import sys
from collections import defaultdict
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
di=[0,0,1,-1]
dj=[1,-1,0,0]
count=0
def dfs(i,j,graph,value):
    global cnt
    graph[i][j]='V'
    cnt+=1
    for x in range(4):
        ni= i + di[x]
        nj= j + dj[x]
        if 0<=ni<m and 0<=nj<n and graph[ni][nj]!='V' and graph[ni][nj]==value:
            dfs(ni,nj,graph,value)

answer=defaultdict(int)

for _ in range(m):
    graph.append(list(input().strip()))

for i in range(m):
    for j in range(n):
        if graph[i][j]!='V':
            cnt=0
            temp=graph[i][j]
            dfs(i,j,graph,graph[i][j])
            answer[temp]+=cnt*cnt
print(answer['W'],answer['B'])