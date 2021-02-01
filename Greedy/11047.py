import sys
N,K=map(int,sys.stdin.readline().strip().split())
list=[]
count=0
for i in sys.stdin:
    list.append(int(i.strip()))
for _ in range(len(list)):
    a=list.pop()
    if a>K:
        continue
    else:
        count+=K//a
        K%=a
print(count)