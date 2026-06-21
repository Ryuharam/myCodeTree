N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

r = c = N//2

dr = [-1,0,1,0]
dc = [0,1,0,-1]
d = 0
sum = board[r][c]

for s in str:
    if s == 'L':
        d = (d + 3) % 4
    elif s == 'R':
        d = (d + 1) % 4
    elif s == 'F':
        nr = r + dr[d]
        nc = c + dc[d]
        if nr>=0 and nr<N and nc>=0 and nc<N:
            r = nr
            c = nc
            sum += board[r][c]

print(sum) 
