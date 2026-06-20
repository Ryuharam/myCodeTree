n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

visited = [[False]*m for _ in range(n)]

def ispossible(r, c):
    global n, m
    return r>=0 and r<n and c>=0 and c<m and not visited[r][c]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
r = 0
c = 0
d = 0

for i in range(1, n*m+1):
    arr[r][c] = i
    visited[r][c] = True
    nr = r + dr[d]
    nc = c + dc[d]
    if ispossible(nr, nc):
        r = nr
        c = nc
    else:
        d = (d+1)%4
        r = r + dr[d]
        c = c + dc[d]

for row in arr:
    print(*row)

