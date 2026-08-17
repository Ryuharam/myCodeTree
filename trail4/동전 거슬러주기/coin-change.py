import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

coins = list(map(int, input().split()))

dp = [10000 for _ in range(M+1)]
dp[0] = 0

for i in range(M+1):
    for j in range(N):
        if coins[j] > i:
            continue
        dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[M] == 10000:
    print(-1)
else:
    print(dp[M])