import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
a=[A[0]]
# #풀이 1: dp로 풀기
# dp=[1 for _ in range(N)]
# for i in range(1,N):
#     for j in range(0,i):
#         if A[j]>A[i]:
#             dp[i]=max(dp[j]+1,dp[i])
# print(max(dp))

#풀이 2: 이진탐색으로 풀기
def lower_bound(arr,target):
    start=0
    end=len(arr)-1
    while(start<end):
        mid=(start+end)//2
        if target>=arr[mid]: #등호 처리 안하면 시간 에러
            end=mid
        elif target<arr[mid]:
            start=mid+1
    return end

for i in range(1,N):
    if A[i]<a[-1]:
        a.append(A[i])
    else:
        a[lower_bound(a,A[i])]=A[i]
print(len(a))