#BOJ 2667 시작시간 13:40
#아이디어 요약: dfs 와 카운팅
#visited를 따로 만들지 않아도, 0을 1로 또는 1을 0으로 바꿔가며 체크 가능
#DFS에서 ans를 매개변수로 설정하면, 다른 가지로 갈 때 ans가 이전 값으로 회귀한다. 주의할것!!!

# a=5
# print(a)
# b=a
# print(b)
# a=7
# print(a)
# print(b)

# def printgraph():
#     for i in range(N):
#         if i>=1:
#             print()
#         for j in range(N):
#             print(graph[i][j], end='')
#     print()


#풀이 1 : dfs를 이용한 풀이

# import sys
# def dfs(x,y): #True: 덩어리 발견
#     global ans
#     if x<0 or x>=N or y<0 or y>=N:
#         return False
#     if graph[x][y]==1:
#         graph[x][y]=0
#         ans += 1
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y-1)
#         dfs(x,y+1)
#         return True #한번이라도 1을찾으면 결국 True return
#     return False #범위 안에 있기는 한데 0이면 False 반환
#
# input=sys.stdin.readline
# N=int(input())
# graph=[]
# for _ in range(N):
#     graph.append(list(map(int,list(input().strip()))))
# count=0
# global ans
# ans=0
# anslist=[]
# for i in range(N):
#     for j in range(N):
#         if dfs(i,j)==True:
#             count+=1
#             anslist.append(ans)
#             ans=0
# print(count)
# print("\n".join(list(map(str,sorted(anslist)))))


#풀이 2: bfs를 이요한 풀이 (dfs가 더빠름)
#시작시간 18:03
import sys
from  collections import deque
def bfs(i,j):
    global ans
    if graph[i][j]==1:
        q=deque()
        q.append((i,j))
        while q:
            x, y = q.popleft()
            if 0<=x<N and 0<=y<N and graph[x][y]==1: #리스트 인덱스 에러를 방지하기 위해 에러방지 조건을 먼저 제시
                graph[x][y]=0
                ans+=1
                q.append((x-1,y))
                q.append((x+1, y))
                q.append((x ,y-1))
                q.append((x, y+1))

            else:
                continue
        anslist.append(ans)
        return True
    return False
input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,list(input().rstrip()))))
count=0
ans=0
anslist=[]
for i in range(N):
    for j in range(N):
        if bfs(i,j)==True:
            count+=1
            ans=0
print(count)
for i in sorted(anslist):
    print(i)