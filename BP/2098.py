import sys

INF = float('inf')
N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (1 << N) for _ in range(N)]

def dfs(now, memo):
    if dp[now][memo]:
        return dp[now][memo]
    if memo == (1 << N) - 1:
        return costs[now][0] if costs[now][0] else INF

    min_cost = INF
    for i in range(1, N):
        if (memo >> i) % 2 == 0 and costs[now][i]:
            temp = dfs(i, memo | 1 << i)
            min_cost = min(min_cost, temp + costs[now][i])
    dp[now][memo] = min_cost
    return min_cost


print(dfs(0, 1))
