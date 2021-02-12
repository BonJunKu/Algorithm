import sys
from bisect import bisect_right
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
a=[]
# #풀이 1: dp로 풀기
# dp=[1 for _ in range(N)]
# for i in range(1,N):
#     for j in range(0,i):
#         if A[j]>A[i]:
#             dp[i]=max(dp[j]+1,dp[i])
# print(max(dp))

#풀이 2: 이진탐색으로 풀기
def lower_bound(start,end,target):
    while start<end:
        mid=(start+end)//2
        if a[mid]>target:
            start=mid+1
        else:
            end=mid
        return end
for i in range(N):
    if i==0:
        a.append(A[i])
        continue
    if a[-1]>A[i]: #더 작은 값 발견시
        a.append(A[i])
    else:
        tmp=lower_bound(0,len(a),A[i])
        a[tmp]=A[i]
print(len(a))