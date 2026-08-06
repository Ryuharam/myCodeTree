import sys

input = sys.stdin.readline

N, r, c = list(map(int, input().split()))
r, c = r-1, c-1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

board = [list(map(int, input().split())) for _ in range(N)]

move = [board[r][c]]
flag = True
while flag:
    flag = False
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 > nr or N <= nr or 0 > nc or nc >= N:
            continue
        
        if board[r][c] < board[nr][nc]:
            r, c = nr, nc
            move.append(board[nr][nc])
            flag = True
            break

print(*move)