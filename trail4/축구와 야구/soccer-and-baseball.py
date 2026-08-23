import sys

input = sys.stdin.readline

N = int(input())

ability = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][k] : i번째 학생, j명의 축구팀, k명의 야구팀
dp = [[[-1 for _ in range(10)] for _ in range(12)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    for j in range(12):
        for k in range(10):
            # i를 어느팀에도 안 넣는 경우
            dp[i][j][k] = dp[i-1][j][k]

            # i를 축구팀에 넣는 경우
            if j>0 and dp[i-1][j-1][k] != -1:
                dp[i][j][k] = max(dp[i-1][j-1][k] + ability[i][0], dp[i][j][k])

            # i를 야구팀에 넣는 경우
            if k>0 and dp[i-1][j][k-1] != -1:
                dp[i][j][k] = max(dp[i-1][j][k-1] + ability[i][1], dp[i][j][k])

print(dp[N][11][9])
