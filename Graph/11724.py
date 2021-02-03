'''
1차시도: 시간 초과

import sys
sys.setrecursionlimit(10000)
N,M=map(int,sys.stdin.readline().strip().split())
count=0
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().strip().split())
    if a not in graph[b]:
        graph[b].append(a)
    if b not in graph[a]:
        graph[a].append(b)
#한 점은 한 경로에만 포함될 수 있음

visited=[False for _ in range(N+1)]

def dfs(graph,v,visited):
    if visited[v]==False:
        visited[v]=True
        for i in graph[v]:
            dfs(graph,i,visited) #i랑 v 헷갈려서 틀림
for i in range(1,N+1):
    if visited[i]==False:
        dfs(graph,i,visited)
        count+=1
    else:
        continue
print(count)

'''
import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v]=True
    for i in range(1,N+1):
        if visited[i]==False and graph[v][i]==1:
            dfs(i)
'''
1. visited 에 True 표시,
2. 점 1부터 차례로 돌면서 한번도 온적 없는 점인데 이 점과 i번째 점이 연결되어있을경우

점=[] 별로 만드는 법이 있지만
이중리스트가 더 빠른듯하다. 
'''

N,M=map(int,sys.stdin.readline().strip().split())
graph=[[0]*(N+1) for _ in range(N+1)]
visited=[False]*(N+1) #visited는 False
for i in range(M):
    x,y=map(int,sys.stdin.readline().strip().split())
    graph[x][y]=1
    graph[y][x]=1
count =0
for i in range(1,N+1):
    if visited[i]==False:
        dfs(i)
        count+=1
print(count)


