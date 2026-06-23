n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
d, r, c = 0, 0, 0

if k // n == 1:
    d = 1
    r = k - n
    c = n - 1
elif k // n == 2:
    d = 2
    r = n - 1
    c = n - (k%n) - 1
elif k // n == 3:
    d = 3
    r = n - (k%n) - 1
else:
    c = k
#print(r,c)
def is_in(r,c,n):
    return r>=0 and r<n and c>=0 and c<n

cnt = 0
while is_in(r,c,n):
    cnt += 1
    #print(f"r: {r},c: {c}, d: {d}, cnt: {cnt}")
    if grid[r][c] == '\\':
        if d%2==0:
            d = (d+3)%4
        else:
            d = (d+1)%4
    else:
        if d%2==0:
            d = (d+1)%4
        else:
            d = (d+3)%4

    r = r + dr[d]
    c = c + dc[d]
    #print(f"next: {r},{c}")

print(cnt)