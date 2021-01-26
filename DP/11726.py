import sys
n=int(sys.stdin.readline())
dict=dict()
dict[1]=1
dict[2]=2
for i in range(3,n+1):
    dict[i]=dict[i-1]+dict[i-2]
print(dict[n]%10007)
