#1차시도: 왜틀렸는지 모르겠음

import sys
from bisect import bisect_left
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
anslist=[]
def bisect(arr,target):
    start=0
    end=len(arr)-1
    while(start<end):
        mid=(start+end)//2
        if target>arr[mid]:
            end=mid
        else:
            start=mid+1
    return end
for i in range(n):
    left=arr[:i+1]
    right=arr[i:]
    leftlen=len(left)
    rightlen=len(right)
    leftlist=[]
    rightlist=[]
    for j in range(0,leftlen):
        if j==0:
            leftlist.append(left[j])
        elif left[j]>leftlist[-1]:
            leftlist.append(left[j])
        else:
            if left[j] in leftlist:
                continue
            leftlist[bisect_left(leftlist,left[j])]=left[j]
    for k in range(0,rightlen):
        if k==0:
            rightlist.append(right[k])
        elif right[k]<rightlist[-1]:
            rightlist.append(right[k])
        else:
            if right[k] in rightlist:
                continue
            rightlist[bisect(rightlist,right[k])]=right[k]
    if leftlist[-1]==leftlist[-1] and rightlist[0]==right[0] and leftlist[-1]==right[0]:
        anslist.append(len(rightlist)+len(leftlist)-1)
    else:
        anslist.append(len(rightlist)+len(leftlist))
    #print(leftlist, rightlist, anslist)

print(max(anslist))
