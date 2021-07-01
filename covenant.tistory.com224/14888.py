import sys
sys.setrecursionlimit(100000)
MAX=-1e9-1
MIN=1e9+1
input=sys.stdin.readline
n=int(input())
numbers=list(map(int,input().split()))
op=list(map(int,input().split()))

def divide(m,n):
    if m*n<0:
        return abs(m)//abs(n)*(-1)
    else:
        return m//n

def DFS(plus,minus,mul,div,cnt,sum):
    global MAX
    global MIN
    #print(plus,minus,mul,div)
    #print(sum)
    if (cnt==n):
        MAX=max(MAX,sum)
        MIN=min(MIN,sum)
    if (plus>0):
        DFS(plus-1,minus,mul,div,cnt+1,sum+numbers[cnt])
    if (minus>0):
        DFS(plus,minus-1,mul,div,cnt+1,sum-numbers[cnt])
    if (mul>0):
       DFS(plus,minus,mul-1,div,cnt+1,sum*numbers[cnt])
    if (div>0):
       DFS(plus,minus,mul,div-1,cnt+1,divide(sum,numbers[cnt]))

DFS(op[0],op[1],op[2],op[3],1,numbers[0])

print(MAX)
print(MIN)
