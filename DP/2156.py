# 최근 3개 항을 어떻게 고려할 것인가..
# 끝모양이 110인 경우, 101인 경우 011인 경우가 있다...
# 축적되는 정답의 dp를 따로 만들 것.
# n=1이 되는 경우 분류

import sys
input=sys.stdin.readline
n=int(input())
if n>=2:
    a=[0]*(n+1)
    dp=[0]*(n+1)
    for i in range(n):
        a[i+1]=int(input())
    dp[1]=a[1]
    dp[2]=a[1]+a[2]
    for n in range(3,n+1):
        dp[n]=max(dp[n-1],dp[n-3]+a[n-1]+a[n],dp[n-2]+a[n])
    print(dp[n])
else:
    print(input())