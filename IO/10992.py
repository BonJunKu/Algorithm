import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    if i==1:
        print('*')
    elif i==n:
        print('*'*(2*i-1))
    else:
        print('*',' '*(2*i-3),'*',sep='')