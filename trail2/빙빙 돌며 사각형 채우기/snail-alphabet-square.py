n, m = map(int, input().split())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c, d, cnt = 0, 0, 0, 0

grid = [[ord('A')] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def is_in(r,c):
    global n, m
    return r >= 0 and r < n and c >= 0 and c < m and not visited[r][c]

while True:
    if cnt == n * m:
        break

    visited[r][c] = True
    grid[r][c] = ord('A') + (cnt % 26)

    nr = r + dr[d]
    nc = c + dc[d]

    if not is_in(nr, nc):
        d = (d + 1) % 4
    
    r = r + dr[d]
    c = c + dc[d]
    cnt += 1

for row in grid:
    for col in row:
        print(chr(col),end=" ")
    print()