import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [[-1,1,0,0],[0,0,1,-1],[0,0,-1,1]]
dc = [[0,0,-1,1],[1,-1,0,0],[-1,1,0,0]]
cd = [[0,1,2,3],[3,2,1,0],[2,3,0,1]]

max_time = 0

for i in range(4*N):
    time = 1
    if i // N == 3:
        r, c, d = N - 1 - i % N, 0, 3
    elif i // N == 2:
        r, c, d = N - 1, N - 1 - i % N, 0
    elif i // N == 1:
        r, c, d = i % N, N-1, 2
    else:
        r, c, d = 0, i % N, 1
    
    
    while 0 <= r and r < N and 0 <= c and c < N:
        nr = r + dr[board[r][c]][d]
        nc = c + dc[board[r][c]][d]
        d = cd[board[r][c]][d]
        r, c = nr, nc
        time += 1
    max_time = max(max_time, time)

print(max_time)