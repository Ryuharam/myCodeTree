import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[1_000_000 for _ in range(N)] for _ in range(N)]


for r in range(N):
    for c in range(N):
        if r == 0 and c == 0:
            dp[r][c] = arr[r][c]
        elif r == 0:
            dp[r][c] = max(dp[r][c-1], arr[r][c])
        elif c == 0:
            dp[r][c] = max(dp[r-1][c], arr[r][c])
        else:
            dp[r][c] = max(min(dp[r-1][c], dp[r][c-1]), arr[r][c])


print(dp[N-1][N-1])