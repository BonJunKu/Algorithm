import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    graph=[list(map(int,input().split())) for _ in range(2)]
    graph[0][1]+=graph[1][0]
    graph[1][1]+=graph[0][0]
    for i in range(2,n):
        graph[0][i]+=max(graph[1][i-1],graph[1][i-2])
        graph[1][i]+=max(graph[0][i-1],graph[0][i-2])
    print(max(graph[0][n-1],graph[1][n-1]))

    #누적으로 갱신시킨다는 것이 포인트.