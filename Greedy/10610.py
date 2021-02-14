# import sys
# input=sys.stdin.readline
# N=list(map(int,list(input().rstrip())))
# N=sorted(N,reverse=True)
# if N[-1]!=0:
#     print(-1)
# else:
#     if sum(N)%3==0:
#         pass
#     elif sum(N)%3==1:
#         for i in N[len(N)-2:-1:-1]:
#             if i%3==1:
#                 N.remove(i)
#                 break
#     else:
#         for j in N[len(N)-2:-1:-1]:
#             if j%3==2:
#                 N.remove(j)
#                 break
#     N = list(map(str, N))
#     print(''.join(N))
#
#     #출력 초과 에러...


n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))