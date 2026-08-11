import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

used_cal = [False for _ in range(N)]
min_val = 10000
max_val = 0

def choose(r: int):
    global choose, min_val, max_val

    if r >= N:
        max_val = max(max_val, min_val)
        return
    
    for c in range(N):
        if used_cal[c]:
            continue
        
        tmp = min_val
        min_val = min(min_val, board[r][c])
        used_cal[c] = True
        choose(r+1)
        used_cal[c] = False
        min_val = tmp

choose(0)

print(max_val)