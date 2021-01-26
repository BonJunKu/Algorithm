import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    print(' '*(n-i),'*'*i,sep='')
for i in range(1,n):
    print(' '*i,'*'*(n-i),sep='')
