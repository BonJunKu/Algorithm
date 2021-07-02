import sys

input = sys.stdin.readline

n, s = map(int, input().split())
length = 100001

summary = 0
arr = list(map(int, input().split()))
end = 0
cnt = 0

for start in range(n):
    while summary < s and end < n:
        summary += arr[end]

        end += 1
        cnt += 1

    if summary >= s:
        length = min(length, cnt)

    summary -= arr[start]
    cnt -= 1

if (cnt == 10001):
    print(0)
else:
    print(length)