#sys.setrecursion limit 안하면 에러뜸!!
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i,j):
    if 0<=i<h and 0<=j<w and graph[i][j]==1:
        graph[i][j]=0
        dfs(i-1,j-1)
        dfs(i-1,j)
        dfs(i-1,j+1)
        dfs(i,j-1)
        dfs(i,j+1)
        dfs(i+1,j-1)
        dfs(i+1,j)
        dfs(i+1,j+1)
        return True
    return False

w,h=map(int,input().split())
while not (w==0 and h==0):
    graph=[]
    count=0
    for i in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                count+=1
    print(count)
    w,h=map(int, input().split())