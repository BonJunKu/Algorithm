import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
per=list(permutations(num))
sumlist=[]
def sol(per):
    for i in per:
        minisum=0
        for j in range(len(i)-1):
            minisum+=abs(i[j]-i[j+1])
        sumlist.append(minisum)
sol(per)
print(max(sumlist))



