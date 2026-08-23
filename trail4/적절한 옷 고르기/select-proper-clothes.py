N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j], i: i번째 날, j: j번째 옷
dp = [[-1 for _ in range(N)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(N):
        if clothes[j][0] <= i and i <= clothes[j][1]:
            dp[i][j] = 0
            for k in range(N):
                if dp[i-1][k] == -1:
                    continue
                dp[i][j] = max(dp[i][j], abs(clothes[k][2] - clothes[j][2]) + dp[i-1][k])
print(max(dp[M]))