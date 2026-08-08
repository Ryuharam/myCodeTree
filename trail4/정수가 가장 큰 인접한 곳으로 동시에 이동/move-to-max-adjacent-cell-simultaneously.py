import sys

input = sys.stdin.readline

N, M, T = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]
balls = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c = list(map(int, input().split()))
    r, c = r-1, c-1
    balls[r][c] = 1

# 상, 하, 좌, 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def is_in(r: int, c: int) -> bool:
    return 0 <= r and r < N and 0 <= c and c < N

for _ in range(T):
    tmp = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if balls[r][c] != 1:
                continue
            max_val = 0
            next_r = r
            next_c = c
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_in(nr, nc) and board[nr][nc] > max_val:
                    max_val = board[nr][nc]
                    next_r = nr
                    next_c = nc
            tmp[next_r][next_c] += 1

    for r in range(N):
        for c in range(N):
            if tmp[r][c] > 1:
                balls[r][c] = 0
            else:
                balls[r][c] = tmp[r][c]

count = 0
for b in balls:
    count += sum(b)

print(count)