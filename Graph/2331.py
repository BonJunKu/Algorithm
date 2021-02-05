import sys
input=sys.stdin.readline
def specialsum(num,P):
    sum=0
    num=list(map(int,list(str(num))))
    for i in range(len(num)):
        sum+=(num[i]**P)
    return sum
# print(specialsum(57,2))
A,P=map(int,input().split())
D=[]
while A not in D:
    D.append(A)
    A=specialsum(A,P)
next=specialsum(D[-1],P)
index=D.index(next)
print(index)
