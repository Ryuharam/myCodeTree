import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

INIT = 10000
dp = [INIT] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(M, -1, -1):
        if j >= A[i] and dp[j - A[i]] != INIT:
            dp[j] = min(dp[j], dp[j - A[i]] + 1)


if dp[M] == INIT:
    print(-1)
else:
    print(dp[M])