#DP를 빠르게 푸는 법: 점화식을 어떻게 세울 것인가?
#직전 몇 개의 정보로 어떻게 현재 항을 만들 것인가?

#새로 들어가는 수가 9인경우, 이전자리까지 1로 끝난 경우+...+9로 끝난경우
#n으로 끝난 경우에 해당하는 걸 리스트로 잡는다.
import sys
input=sys.stdin.readline
N=int(input())
anslist=[[0]*10,[1]*10]
for k in range(2,N+1):
    currentlist=[]
    for i in range(10):
        currentlist.append(sum(anslist[k-1][:i+1]))
    anslist.append(currentlist)
print(sum(anslist[N])%10007)