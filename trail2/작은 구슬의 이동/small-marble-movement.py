n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

D = {"U":0, "D":2, "R":1, "L":3}
d = D[d]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def in_range(r, c, n):
    return r > 0 and r<=n and c >0 and c<=n

for _ in range(t):
    nr = r + dr[d]
    nc = c + dc[d]
    if in_range(nr, nc, n):
        r = nr
        c = nc
    else:
        d = (d + 2) % 4

print(r,c)

