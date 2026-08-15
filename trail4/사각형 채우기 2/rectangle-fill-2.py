import sys

N = int(input())

MOD = 10_007

if N == 1:
    print(1)
    sys.exit()
elif N == 2:
    print(3)
    sys.exit()

dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2
    dp[i] %= MOD

print(dp[N])