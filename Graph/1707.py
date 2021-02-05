import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
def bfs(v):
    q=deque()
    bi[v]=1
    q.append(v)
    while q:
        a=q.popleft()
        for i in graph[a]:
            if bi[i]==0:
                bi[i]=-bi[a]
                q.append(i)
            else:
                if bi[i]==bi[a]:
                    return False
    return True




for _ in range(n):
    V,E=map(int,input().split())
    graph = [[] for _ in range(V+1)]
    bi=[0]*(V+1)
    isTure=True
    for  _ in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(V+1):
        if bi[i]==0:
            isTrue=bfs(i)
        if bfs(i)==False:
            break
    print("YES" if isTrue else "NO")