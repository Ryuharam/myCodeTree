import sys

input = sys.stdin.readline

n = int(input())

alba = []
for _ in range(n):
    s, e, p = list(map(int, input().split()))
    alba.append((s, e, p))

sorted_alba = sorted(alba, key=lambda x: x[1])

dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = sorted_alba[i][2]
    for j in range(i):
        if sorted_alba[i][0] > sorted_alba[j][1]:
            dp[i] = max(dp[i], dp[j] + sorted_alba[i][2])

print(max(dp))
