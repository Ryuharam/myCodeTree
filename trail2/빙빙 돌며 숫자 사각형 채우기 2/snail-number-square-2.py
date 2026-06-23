n, m = map(int, input().split())
grid = [[0]*m for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
r,c,d,i = 0,0,0,1
visited = [[False]*m for _ in range(n)]

def is_possible(r,c):
    global n, m, visited
    return r>=0 and r<n and c>=0 and c<m and not visited[r][c]

while True:
    visited[r][c] = True
    grid[r][c] = i

    if i >= n*m:
        break
        
    i += 1
    nr = r + dr[d]
    nc = c + dc[d]
    if not is_possible(nr,nc):
        d = (d+1)%4
    r = r + dr[d]
    c = c + dc[d]

for row in grid:
    print(*row)
