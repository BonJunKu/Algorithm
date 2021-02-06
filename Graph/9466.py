#BOJ 9446
#아이디어 요약: 방문했던 점이 나올 때 까지 반복하는데, 그 방문점이 출발점이랑 다른 경우 그 뗴까지 걸린 횟수 세기
#이렇게 세면 루프 외의 찌꺼기들을 셀 수 있다.
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    num=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)
    count=0
    for i in range(1,n+1):
        save=i
        while visited[i]!=1:
            visited[i]=1
            i=num[i]
        while save!=i:
            save=num[save]
            count+=1
    print(count)
