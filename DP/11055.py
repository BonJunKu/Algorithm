from bisect import bisect_left
import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
dp=[0]*1001
for i in range(N):
    dp[A[i]]=max(dp[:A[i]])+A[i]
print(A)
print(dp)
print(max(dp))
