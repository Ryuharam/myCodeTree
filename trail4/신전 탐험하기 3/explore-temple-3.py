import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

coins = [[0 for _ in range(M)]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(M)] for _ in range(N+1)]

for i in range(M):
    dp[0][i] = 0

for i in range(1, N+1):
    for j in range(M):
        for k in range(M):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + coins[i][j])

print(max(dp[N]))