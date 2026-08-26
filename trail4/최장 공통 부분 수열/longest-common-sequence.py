import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

N = len(A)
M = len(B)

dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    if A[i] == B[0]:
        dp[i][0] = 1
    elif i > 0:
        dp[i][0] = dp[i-1][0]

for j in range(M):
    if A[0] == B[j]:
        dp[0][j] = 1
    elif j > 0:
        dp[0][j] = dp[0][j-1]

for i in range(1, N):
    for j in range(1, M):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N-1][M-1])