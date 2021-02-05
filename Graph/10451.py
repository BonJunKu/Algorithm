import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    arr=[0]+list(map(int,input().split()))
    count=0
    visited=[False]*(N+1)
    for i in range(1,N+1):
        if visited[i]==False:
            visited[i]=True
            next=arr[i]
            while next!=i:
                visited[next]=True
                next=arr[next]
            count+=1
    print(count)