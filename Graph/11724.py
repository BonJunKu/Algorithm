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
def dfs(i,G,V,M):
    V[i]=True
    for j in range(1,N+1):
        if V[j]==True or G[i][j]==0:
            continue
            dfs(j,G,V,N)

N = 1001
graph = [[0] * N for i in range(N)]
visited = [0] * N
U, V = map(int,input().split(' '))
for i in range(V):
    u, v = map(int, sys.stdin.readline().split())

    graph[u][v] = 1
    graph[v][u] = 1

count = 0
for i in range (1, U+1):
    if visited[i] == 0:
        dfs(i, graph, visited, U)
        count += 1

print(count)