import sys
N = int(input())
coin = [0] + list(map(int, input().split()))

# i번째, j번 한 칸 이동
MIN = -sys.maxsize
dp = [[MIN, MIN, MIN, MIN] for _ in range(N+1)]
dp[1][1] = coin[1]
dp[2][0] = coin[2]
dp[2][2] = dp[1][1] + coin[2]

for i in range(3, N+1):
    dp[i][0] = dp[i-2][0] + coin[i]
    dp[i][1] = max(dp[i-1][0], dp[i-2][1]) + coin[i]
    dp[i][2] = max(dp[i-1][1], dp[i-2][2]) + coin[i]
    dp[i][3] = max(dp[i-1][2], dp[i-2][3]) + coin[i]

print(max(dp[N]))