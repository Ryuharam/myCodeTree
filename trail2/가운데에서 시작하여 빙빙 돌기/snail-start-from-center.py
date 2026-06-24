n = int(input())
grid = [[0] * n for _ in range(n)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
r = c = n - 1
d = 0

cnt = n * n
def is_in(r,c):
    global n
    return r >= 0 and r < n and c >= 0 and c < n and grid[r][c] == 0

while True:
    grid[r][c] = cnt

    if cnt == 1:
        break
        
    nr = r + dr[d]
    nc = c + dc[d]

    if not is_in(nr,nc):
        d = (d + 1) % 4
    
    r = r + dr[d]
    c = c + dc[d]
    cnt -= 1

for row in grid:
    print(*row)