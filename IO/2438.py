import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print('')

'''
input을 꼭 최상단에 하지 않아도 된다.
문자열에 i를 곱할 수 있다.
'''