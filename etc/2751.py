from sys import stdin
n = int(sys.stdin.readline())
a = sorted(list(map(int,sys.stdin.read().split())))
print('\n'.join(map(str,a)))