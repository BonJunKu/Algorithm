import sys
from itertools import permutations
input=sys.stdin.readline
n=int(input())
graph=[[int(x) for x in input().split()] for y in range(n)]
path=list(permutations([x for x in range(n)]))
minvalue=1000000
for i in path:
    temp=0
    for j in range(len(i)):

        if j==(len(i)-1):

            temp+=graph[i[j]][i[0]]

        elif graph[i[j]][i[j+1]]==0:
            break

        else:
            temp+=graph[i[j]][i[j+1]]
    if temp<minvalue:
        minvalue=temp
print(minvalue)