import sys
def factorial(x):
    if x==0:
        return 1
    for i in range (x-1,0,-1):
        x*=i
    return x
def function(n):
    one, two, three = 0, 0, 0
    count = 0
    for i in range(0, n // 3 + 2):
        for j in range(0, n // 2 + 2):
            for k in range(0, n + 1):
                if k + 2 * j + 3 * i == n:
                    count += factorial(i + j + k) / (factorial(i) * factorial(j) * factorial(k))
    return int(count)

N=int(sys.stdin.readline())
for i in range (1,N+1):
    x=int(sys.stdin.readline())
    print(function(x))