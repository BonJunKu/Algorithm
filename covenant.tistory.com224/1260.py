import sys
answer=[]
answer2=[]
from collections import deque
def dfs(v,visited,answer,graph):
    if visited[v]==0:
        visited[v]=1
        answer.append(v)
        for i in graph[v]:
            if visited[i]==0:
                dfs(i,visited,answer,graph)
    else:
        return

def bfs(v,visited,answer2,graph):
    if visited[v]==0:
        visited[v]=1
        q=deque()
        q.append(v)
        while q:
            temp=q.popleft()
            answer2.append(temp)
            for i in graph[temp]:
                if visited[i]==0:
                    q.append(i)
                    visited[i]=1




input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for j in graph:
    j.sort()
visited=[0]*(n+1)
dfs(v,visited,answer,graph)
visited=[0]*(n+1)
bfs(v,visited,answer2,graph)
print(' '.join(map(str,answer)))
print(' '.join(map(str,answer2)))