import sys
input=sys.stdin.readline
h,w = list(map(int,input().split()))
block=list(map(int,input().split()))
answer=[]
for i in range(w):
    if block[:i]:
        left=block.index(max(block[:i]))
    else:
        left=i
    if block[i+1:]:
        right=block.index(max(block[i+1:]))
    else:
        right=i
    if block[left]<=block[right]:
        small=left
    else:
        small=right
    if block[small]>block[i]:
        answer.append(block[small]-block[i])
    else:
        answer.append(0)
print(sum(answer))