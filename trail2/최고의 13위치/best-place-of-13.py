n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_val = 0

for i in range(n):
    for j in range(n-2):
        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        max_val = max(max_val, sum)

print(max_val)