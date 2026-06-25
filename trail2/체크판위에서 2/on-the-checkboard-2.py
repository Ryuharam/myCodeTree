R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

cnt = 0

for i in range(1, R-1):
    for j in range(1, C-1):
        if grid[0][0] != grid[i][j]:
            for i2 in range(i+1, R-1):
                for j2 in range(j+1, C-1):
                    if grid[i][j] != grid[i2][j2] and grid[i2][j2] != grid[R-1][C-1]:
                        #print(f"({i},{j}) -> ({i2},{j2})")
                        cnt += 1

print(cnt)