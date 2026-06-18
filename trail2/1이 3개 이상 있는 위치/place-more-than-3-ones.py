n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def inrange(x, y, n):
    return x>=0 and x<n and y>=0 and y<n

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

cnt = 0
for i in range(n):
    for j in range(n):
        tmp = 0

        for d in range(4):
            nx = i + dxs[d]
            ny = j + dys[d]

            if inrange(nx,ny,n) and grid[nx][ny] == 1:
                tmp += 1
        if tmp >= 3:
            cnt += 1

print(cnt)